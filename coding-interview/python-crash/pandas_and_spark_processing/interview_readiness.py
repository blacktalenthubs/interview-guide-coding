"""
  #transactions?currency = EUR & min_amount = 10 & max_amount = 500 & page = 2 & limit = 10

  how to make api calls with special params
  endtime
  starttime

  get calls
  params = {
  "currency": "EUR",

  }

  response = requests.get(url,params=params)



Glue ----> ICEBERG,ATHENA,HIVE
Glue---
Metadata
data catalogs
Glue craws your uderlying S3 buckets
schema inference

ICEBERG---> WHAT problems does ICEBERG solves:
Schema Evolutions
Schema changes ----> dimensions changes(adding new fiels)
partitions
ACID Transactions
    (uPDATES,MERGE,DELETES)

Streams later consume or write to Iceberg

Performance Monitoring
    How would you debug a spark issues
    how would you debug data skew, network shuffling
    what are your spark configurations -- how does this matter for performance

Lazy Evaluation
    transformations
    actions


Python tricks:
date and time tranformations
    strftime


"""