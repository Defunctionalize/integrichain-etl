# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSetUpDremio():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1111createuser(self):
    self.driver.get("http://localhost:9047/signup")
    self.driver.set_window_size(726, 508)
    self.driver.find_element(By.NAME, "firstName").send_keys("integrichain")
    self.driver.find_element(By.NAME, "lastName").send_keys("integrichain")
    self.driver.find_element(By.NAME, "userName").send_keys("integrichain")
    self.driver.find_element(By.NAME, "email").send_keys("integrichain@mailinator.com")
    self.driver.find_element(By.NAME, "password").send_keys("integrichain1")
    self.driver.find_element(By.NAME, "passwordVerify").send_keys("integrichain1")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
  
  def test_1211addElasticSearch(self):
    self.driver.get("http://localhost:9047/")
    self.driver.set_window_size(1096, 508)
    self.driver.find_element(By.CSS_SELECTOR, "span[title=\"Add Source\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".SelectConnectionButton__button-base___1T4sz:nth-child(6) > img").click()
    self.driver.find_element(By.NAME, "name").send_keys("ElasticSearch__fireball_data")
    self.driver.find_element(By.NAME, "config.hostList[0].hostname").click()
    self.driver.find_element(By.NAME, "config.hostList[0].hostname").send_keys("elasticsearch")
    self.driver.find_element(By.NAME, "config.username").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(1) > .Radio__dummy___1QfaS").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
  
  def test_1211addS3(self):
    self.driver.get("localhost:9047localhost:9047")
    self.driver.find_element(By.CSS_SELECTOR, "span[title=\"Add Source\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".SelectConnectionButton__button-base___1T4sz:nth-child(3)").click()
    self.driver.find_element(By.NAME, "name").click()
    self.driver.find_element(By.NAME, "name").send_keys("S3__property_data")
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(3) > .Radio__dummy___1QfaS").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".add-item > img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".add-item > img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".add-item > img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".add-item > img").click()
    element = self.driver.find_element(By.NAME, "config.externalBucketList[0]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "config.externalBucketList[0]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "config.externalBucketList[0]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "config.externalBucketList[0]").click()
    self.driver.find_element(By.NAME, "config.externalBucketList[0]").send_keys("defunctionalize.integrichain.data")
    element = self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
  
  def test_1311formatS3file(self):
    self.driver.get("http://localhost:9047/")
    self.driver.set_window_size(726, 508)
    self.driver.find_element(By.CSS_SELECTOR, ".finder-nav-item:nth-child(2) .EllipsedText").click()
    self.driver.find_element(By.CSS_SELECTOR, ".last-File").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".last-File").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".last-File").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".last-File").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .field:nth-child(1) > .Checkbox__dummy___2J_HV").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .field-with-error:nth-child(1) .Select__label___22HmC").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".Select__item-wrapper___1Mzh0:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
  
  def test_1321filterdetroitdata(self):
    self.driver.get("http://localhost:9047/")
    self.driver.set_window_size(1339, 830)
    self.driver.find_element(By.CSS_SELECTOR, ".finder-nav-item:nth-child(2) .EllipsedText").click()
    self.driver.find_element(By.CSS_SELECTOR, ".last-File").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".last-File").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".last-File").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".TextHighlight").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".sql-toggle > img").click()
    self.driver.find_element(By.CSS_SELECTOR, "#SALEDATE\\ \\+\\ type > .icon-type").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-item:nth-child(5) > span").click()
    element = self.driver.find_element(By.LINK_TEXT, "Learn more…")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(6) .Radio__dot___FiThB").click()
    self.driver.find_element(By.NAME, "customValue").click()
    self.driver.find_element(By.NAME, "newFieldName").click()
    self.driver.find_element(By.NAME, "newFieldName").send_keys("date_typed")
    self.driver.find_element(By.CSS_SELECTOR, ".Checkbox__dummy___2J_HV").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".wizard-apply-button").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".fixedDataTableCellLayout_main:nth-child(4) .SelectView__select___3fnvj:nth-child(2) .fa:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(9) > .dropdown-menu-item:nth-child(1) > span").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .field > .Checkbox__label-content___3DNjs input").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .field > .Checkbox__label-content___3DNjs input").send_keys("2009-01-01")
    self.driver.find_element(By.CSS_SELECTOR, ".subTitles").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".wizard-apply-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".wizard-apply-button").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".explore-save-button > .fa").click()
    self.driver.find_element(By.CSS_SELECTOR, ".save-as-menu-item > span").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.NAME, "name").send_keys("filtered_detroit_houses_sold")
    self.driver.find_element(By.CSS_SELECTOR, ".confirm-cancel-footer > button:nth-child(3)").click()
  
  def test_1411formatfireballdata(self):
    self.driver.get("http://localhost:9047/")
    self.driver.set_window_size(800, 600)
    self.driver.find_element(By.CSS_SELECTOR, ".visible-items > .finder-nav-item:nth-child(1) .EllipsedText").click()
    self.driver.find_element(By.CSS_SELECTOR, ".last-File").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".TextHighlight").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".sql-toggle > img").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cursor")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".lines-content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".lines-content")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cursor")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".mtk6:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".lines-content").click()
    self.driver.find_element(By.CSS_SELECTOR, ".inputarea").send_keys("SELECT \"Velocity Components (km/s): vz\" AS velocity_components_z, \\n\"Longitude (Deg)\" AS longitude, \\n\"Velocity Components (km/s): vx\" AS velocity_components_x, \\n\"Velocity Components (km/s): vy\" AS velocity_components_y, \\n\"Latitude (Deg)\" AS latitude, \\n\"Calculated Total Impact Energy (kt)\" AS calculated_impact_energy, \\n\"Date/Time - Peak Brightness (UT)\" AS peak_brightness, \\n\"Velocity (km/s)\" AS velocity, \\n\"Altitude (km)\" AS altitude, \\n\"Total Radiated Energy (J)\" AS total_jules_radiated\\nFROM ElasticSearch__fireball_data.nasa.fireballs")
    self.driver.find_element(By.CSS_SELECTOR, ".preview-button > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".preview-button > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".explore-save-button > .fa").click()
    self.driver.find_element(By.CSS_SELECTOR, ".save-as-menu-item > span").click()
    self.driver.find_element(By.NAME, "name").send_keys("fire_data")
    self.driver.find_element(By.CSS_SELECTOR, ".confirm-cancel-footer > button:nth-child(3)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".LoaderWhite")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  
  def test_1511createsummaryextract(self):
    self.driver.get("http://localhost:9047/")
    self.driver.set_window_size(800, 600)
    self.driver.find_element(By.CSS_SELECTOR, "a > span:nth-child(2)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "a > span:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".view-lines").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".inputarea").send_keys("WITH houses_by_date AS ( SELECT date_typed AS \"DATE\", COUNT(*) AS HOUSES_SOLD FROM \"@integrichain\".\"filtered_detroit_houses_sold\" GROUP BY 1), fireballs AS ( SELECT TO_DATE(peak_brightness, \'MM/DD/YYYY\', 1) AS \"DATE\", COUNT(*) AS fireballs FROM \"@integrichain\".\"fire_data\" GROUP BY 1) SELECT COALESCE(h.\"DATE\",f.\"DATE\") AS \"DATE\", COALESCE(CAST(fireballs AS int),0) AS fireballs, COALESCE(CAST(houses_sold AS int),0) AS houses_sold FROM houses_by_date h FULL OUTER JOIN fireballs f ON h.\"DATE\" = f.\"DATE\"")
    self.driver.find_element(By.CSS_SELECTOR, ".preview-button > span").click()
    self.driver.execute_script("window.scrollTo(0,25.33333396911621)")
    element = self.driver.find_element(By.CSS_SELECTOR, ".explore-save-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".explore-save-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".explore-save-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".explore-save-button").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".save-as-menu-item > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".save-as-menu-item > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".save-as-menu-item > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".save-as-menu-item > span").click()
    self.driver.find_element(By.NAME, "name").send_keys("summary_metric")
    self.driver.find_element(By.NAME, "name").send_keys("summary_metric")
    self.driver.find_element(By.CSS_SELECTOR, ".confirm-cancel-footer > button:nth-child(3)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".confirm-cancel-footer .font-icon")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  