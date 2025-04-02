
```
┌────────────────────────────┐
│  1. Payment Sources (POS,  │
│     Web Checkout, etc.)    │
└────────────┬───────────────┘
             |  (Raw Events)
             v
    ┌─────────────────────────────┐
    │  2. Kafka (AWS MSK)        │
    │     Topic: "transactions"   │
    └────────────┬───────────────┘
                 | (Stream Reads)
                 v
     ┌───────────────────────────────────┐
     │ 3. Spark Structured Streaming    │
     │    - Consumes raw "transactions" │
     │    - Joins dimension data        │
     │    - Enriches with UDFs          │
     │    - Writes "transactions_enr."  │
     └────────────┬───────────────┬─────┘
                  |               |
        (Enriched Stream)     (Parallel Write of Raw
                  |           or Enriched data to S3)
                  |               |
                  v               v
      ┌───────────────────┐     ┌────────────────────┐
      │ 4. Kafka (MSK):   │     │ 4A. S3 (Data Lake)  │
      │  "transactions_   │     │  - Historical Raw   │
      │   enriched"       │     │    (or enriched)    │
      └────────────┬──────┘     │  - Partitioned by   │
                   |            │    date/event type   │
                   v            └────────────────────┘
       ┌──────────────────────────────┐
       │  5. DynamoDB / NoSQL         │
       │   - "TransactionIndex"       │
       │   - Fast lookups (API, etc.) │
       └────────────┬─────────────────┘
                    |
                    | (Final Enriched Records)
                    |
        ┌─────────────────────────────────┐
        │6. Batch Spark on EMR (Period.) │
        │  - Reads historical data from  │
        │    S3 ("Raw" or "Enriched")    │
        │  - Loads dimension updates (if │
        │    not already in DB)          │
        │  - Corrects/Reaggregates       │
        │    old transactions            │
        │  - Updates TransactionIndex    │
        └────────────┬───────────────────┘
                     |
      ┌────────────────────────────────────┐
      │7. Python API (FastAPI/Flask),     │
      │   deployed on AWS Fargate         │
      │   - Fetches from DynamoDB         │
      │   - Exposes aggregated queries    │
      └────────────────────────────────────┘
                     |
          ┌─────────────────────────────┐
          │8. Downstream Consumers      │
          │   - Analytics, Reporting,   │
          │     Fraud Systems, etc.     │
          └─────────────────────────────┘
```

### **Flow Explanation**

1. **Payment Sources** send **raw transaction events** into **Kafka** (“transactions” topic).  
2. **Spark Structured Streaming** reads these transactions in near real-time, enriches them with dimension data, applies UDFs, and writes out to a second Kafka topic (“transactions_enriched”).  
3. **Parallel Write to S3**: Often a connector or the same Spark job stores **raw or enriched** data into **S3**. This creates a **historical data lake** for long-term storage and batch reprocessing.  
4. **DynamoDB (or Another NoSQL)** becomes the **fast lookup table** for real-time queries of the enriched “Transaction Index.”  
5. **Periodic Batch Jobs on EMR** read all historical data in **S3** to handle **late-arriving** or **corrected** data, and then **update** the Transaction Index in DynamoDB.  
6. A **Python API** is deployed on **AWS Fargate** (or similar) to **query DynamoDB** for the final enriched records. This service is consumed by **downstream systems** (reports, analytics, dashboards).  

Below is a **comprehensive schema design** covering:

1. **Raw Transaction Events** (input from payment sources)  
2. **Dimension Entities** (user, merchant, payment method, product)  
3. **Enriched Transaction Records** (output from Spark after joining dimensions)  
4. **Transaction Index** (NoSQL storage for final aggregated data)  


---

## 1. **Raw Transaction Schema**  
**Collection/Topic**: `transactions` (Kafka or other ingest layer)  

| Field Name         | Type        | Description                                                          |
|--------------------|------------|----------------------------------------------------------------------|
| `transaction_id`   | String(36) | Unique identifier (UUID).                                            |
| `user_id`          | String(36) | Foreign key to **User Dimension**.                                   |
| `merchant_id`      | String(36) | Foreign key to **Merchant Dimension**.                               |
| `product_id`       | String(36) | (Optional) if referencing a **Product Dimension**.                   |
| `amount`           | Decimal(10,2) or Double | Transaction amount.                                    |
| `currency`         | String(3)   | ISO currency code (e.g., "USD").                                     |
| `transaction_type` | String(20)  | e.g., "purchase", "refund".                                          |
| `payment_method_id`| String(36)  | Links to **Payment Method Dimension** (e.g., card, wallet).          |
| `timestamp`        | Long (epoch ms) or DateTime | Time of the transaction.                          |
| `status`           | String(20)  | e.g., "pending", "completed", "failed".                              |
| `fraud_flag`       | Boolean     | Early detection flag (default false).                                |
| `metadata`         | JSON        | Additional raw info (e.g., location, device fingerprint).            |

---

## 2. **Dimension Schemas**

### A. **User Dimension**  
**Collection/Table**: `users`

| Field Name    | Type        | Description                                                |
|---------------|------------|------------------------------------------------------------|
| `user_id`     | String(36) | **Primary Key**.                                           |
| `first_name`  | String(50) |                                                           |
| `last_name`   | String(50) |                                                           |
| `email`       | String(100)|                                                           |
| `phone`       | String(20) |                                                           |
| `country`     | String(50) |                                                           |
| `segment`     | String(20) | e.g., "premium", "standard", "highRiskSegment".           |
| `risk_score`  | Integer     | Pre-calculated user risk.                                 |
| `date_created`| DateTime    |                                                           |
| `metadata`    | JSON        | Additional details (e.g., preferences).                  |

### B. **Merchant Dimension**  
**Collection/Table**: `merchants`

| Field Name       | Type        | Description                          |
|------------------|------------|--------------------------------------|
| `merchant_id`    | String(36) | **Primary Key**.                     |
| `merchant_name`  | String(100)|                                      |
| `category`       | String(50) | e.g. "electronics", "food".          |
| `location`       | JSON        | e.g., `{city: "NYC", country: "USA"}`|
| `date_onboarded` | DateTime    |                                      |
| `risk_category`  | String(20) | e.g., "low", "medium", "high".       |
| `status`         | String(20) | e.g., "active", "suspended".         |
| `metadata`       | JSON        | Additional info.                     |

### C. **Payment Method Dimension**  
**Collection/Table**: `payment_methods`

| Field Name           | Type        | Description                                     |
|----------------------|------------|-------------------------------------------------|
| `payment_method_id`  | String(36) | **Primary Key**.                                |
| `method_type`        | String(20) | e.g., "credit_card", "paypal", "bank_transfer". |
| `provider_name`      | String(50) | e.g., "VISA", "Mastercard", "PayPal".           |
| `metadata`           | JSON        | Additional details (e.g., last 4 digits).       |

### D. **Product Dimension** (Optional)  
**Collection/Table**: `products`

| Field Name    | Type        | Description                                       |
|---------------|------------|---------------------------------------------------|
| `product_id`  | String(36) | **Primary Key**.                                  |
| `name`        | String(100)|                                                   |
| `category`    | String(50) |                                                   |
| `price`       | Decimal(10,2)| Reference price for the product.                |
| `metadata`    | JSON        | Additional data (e.g., brand, shipping details). |

---

## 3. **Enriched Transaction Schema**  
**Collection/Topic**: `transactions_enriched` (Spark output or second Kafka topic)  

| Field Name          | Type        | Description                                                   |
|---------------------|------------|---------------------------------------------------------------|
| `transaction_id`    | String(36) | Copied from raw.                                              |
| `user_id`           | String(36) | From raw.                                                     |
| `user_segment`      | String(20) | Pulled from **User Dimension**.                               |
| `merchant_id`       | String(36) | From raw.                                                     |
| `merchant_category` | String(50) | From **Merchant Dimension**.                                  |
| `payment_method_id` | String(36) | From raw.                                                     |
| `payment_method_type` | String(20) | e.g., "credit_card".                                        |
| `amount`            | Decimal(10,2) | Same as raw.                                              |
| `currency`          | String(3)   | Same as raw.                                                 |
| `timestamp`         | DateTime    | Original transaction time.                                   |
| `transaction_type`  | String(20)  | e.g., "purchase".                                            |
| `enriched_time`     | DateTime    | When the enrichment job processed this record.               |
| `risk_score`        | Integer     | Computed by Spark UDF (e.g., based on user & merchant risk). |
| `metadata`          | JSON        | Merged raw + dimension data (optional).                      |

**Notes**:  
- This schema is typically **written** to a second Kafka topic or directly to NoSQL.  
- Contains combined dimension info + raw transaction fields.

---

## 4. **Transaction Index Schema** (Final NoSQL Storage)

**Table**: `TransactionIndex` (DynamoDB or Cassandra)

- **Option A**: Key by `transaction_id` (simple lookups).  
- **Option B**: Key by `user_id` + date partition for analytics queries.  
- **Option C**: Additional indices for flexible queries.

Below is an **example** DynamoDB design using a **composite key**:

| Field Name          | Type        | Key Type                           | Description                                                     |
|---------------------|------------|------------------------------------|-----------------------------------------------------------------|
| `user_id`           | String(36) | **Partition Key**                  |                                                                |
| `transaction_day`   | String(10) | **Sort Key** (e.g., YYYY-MM-DD)    |                                                                |
| `transaction_id`    | String(36) | Secondary attribute                |                                                                |
| `merchant_id`       | String(36) |                                    |                                                                |
| `amount`            | Decimal(10,2)|                                   |                                                                |
| `currency`          | String(3)   |                                    |                                                                |
| `transaction_type`  | String(20)  |                                    |                                                                |
| `risk_score`        | Integer     |                                    |                                                                |
| `merchant_category` | String(50)  |                                    |                                                                |
| `timestamp`         | DateTime    | Or Long epoch.                     |
| `payment_method_type`| String(20) |                                    |
| `metadata`          | JSON        | Additional enriched data.          |

**Notes**:  
- A *Global Secondary Index (GSI)* might be added on `merchant_id` or `transaction_id` for direct lookups.  
- *Alternatively*, you can keep it simpler and key solely by `transaction_id` if single-record lookups are your main usage. For complex analytics, you might store daily/weekly aggregates with `(user_id, date)` as keys.

---

## 5. **Aggregated Tables** (Optional)

To handle high-level analytics (e.g., total spend per day, top merchants), you might maintain:

**Example**: `DailyUserStats` (NoSQL or a separate OLAP store)
| Field Name       | Type        | Key Type        | Description                             |
|------------------|------------|-----------------|-----------------------------------------|
| `user_id`        | String(36) | Partition Key   |                                         |
| `date`           | String(10) | Sort Key        | e.g., "YYYY-MM-DD"                      |
| `total_spend`    | Decimal(10,2)|               | Sum of user’s transactions that day.    |
| `transaction_count` | Integer  |                 | How many transactions that day.         |
| `max_risk_score` | Integer    |                 | Highest risk score for that day.        |

---

### Relationships Recap

- **Raw Transaction** \(\)-> *1..N*\) => **Dimension** (user, merchant, payment method, etc.).  
- **Enriched Transaction** extends **Raw Transaction** fields + dimension lookups.  
- **Transaction Index** references the same IDs but is stored with final aggregated or enriched attributes.  
