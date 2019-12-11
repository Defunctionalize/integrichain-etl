#! /bin/bash

cat fireballs.json | jq -c '.[] | {"index": {"_index": "nasa", "_type": "fireballs", "_id": .id}}, .' | curl -XPOST localhost:9200/_bulk -H 'Content-Type: application/json' --data-binary @-

