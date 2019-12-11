import airflow
from datetime import datetime, timedelta
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from sqlalchemy import create_engine, text
import dateutil
import logging

logger = logging.getLogger(__name__)

DEFAULT_ARGS = {
    "owner": "integrichain",
    "depends_on_past": True,
    "start_date": datetime(2015, 6, 1),
    "email": ["test_dag@integrichain.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5)
}



## remote sources
fireballs = "https://data.nasa.gov/api/views/mc52-syum/rows.csv?accessType=DOWNLOAD"
homes_sold_in_detroit = "https://query.data.world/s/kis545i26nonrfb4mzl6msyjqn4rdc"

## database
conn_string = f"postgresql://airflow:airflow@integrichain_postgres_1/airflow"
con = create_engine(conn_string)

dag = airflow.DAG('do_all_the_things',
          default_args=DEFAULT_ARGS, schedule_interval=None)


def get_and_load_the_fire_data():
    fire_data = pd.read_csv(fireballs)
    fire_data = fire_data.rename( columns= {'Date/Time - Peak Brightness (UT)':'peak_brightness', 'Latitude (Deg)':'latitiude', 'Longitude (Deg)':'longitude',
       'Altitude (km)':'altitude', 'Velocity (km/s)':'velocity', 'Velocity Components (km/s): vx':'velocity_components_x',
       'Velocity Components (km/s): vy':'velocity_components_y', 'Velocity Components (km/s): vz':'velocity_components_z',
       'Total Radiated Energy (J)':'total_jules_radiated', 'Calculated Total Impact Energy (kt)':'calculated_impact_energy'})

    fire_data.to_sql(   name='fireballs',
                        con = con,
                        schema='datalake',
                        if_exists='replace')
    logger.info('loaded fire data')     

def get_and_load_the_detroit_data():
    detroit_data = pd.read_csv(homes_sold_in_detroit, low_memory=False)
    detroit_data['date_typed'] = [dateutil.parser.parse(x) for x in detroit_data['SALEDATE']]
    filtered_data = detroit_data.loc[detroit_data['date_typed'] >= datetime(2009,1,1)]
    filtered_data.to_sql(   name='detroit',
                        con = con,
                        schema='datalake',
                        if_exists='replace',
                        chunksize=20000)
    logger.info('loaded detroit data')

def run_summary_metric():
    to_run = """DROP TABLE IF EXISTS datawarehouse.summary_metric; CREATE TABLE datawarehouse.summary_metric AS
    WITH
    houses_by_date AS (

        SELECT
            date_typed AS DATE,
            COUNT(*) AS HOUSES_SOLD
        FROM
            datalake.detroit
        GROUP BY 1
    ),
    fireballs AS (
        SELECT
            peak_brightness::date AS DATE,
            COUNT(*) AS fireballs
        FROM
            datalake.fireballs
        GROUP BY 1
    )
    SELECT
        COALESCE(h.DATE,f.DATE) AS DATE,
        COALESCE(fireballs::int,0) AS fireballs,
        COALESCE(houses_sold::int,0) AS houses_sold
    FROM
        houses_by_date h
    FULL OUTER JOIN
        fireballs f
    ON
        h.DATE = f.DATE
"""    
    con.execute(to_run)
    logger.info("Generated metric summary.")

task_1 = PythonOperator(
    task_id='get_and_load_the_fire_data',
    dag=dag,
    python_callable=get_and_load_the_fire_data     
)

task_2 = PythonOperator(
    task_id='get_and_load_the_detroit_data',
    dag=dag,
    python_callable=get_and_load_the_detroit_data     
)

task_3 = PythonOperator(
    task_id='create_metric',
    dag=dag,
    python_callable=run_summary_metric)

task_2 >> task_3
task_1 >> task_3
