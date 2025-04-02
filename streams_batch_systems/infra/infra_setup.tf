############################################
# 7) DynamoDB Tables
############################################

# Example: Transaction Index Table
resource "aws_dynamodb_table" "transaction_index" {
  name         = "TransactionIndex"
  billing_mode = "PAY_PER_REQUEST"

  # Simple primary key with transaction_id
  hash_key = "transaction_id"

  attribute {
    name = "transaction_id"
    type = "S"
  }

  tags = {
    Name = "transaction-index-table"
  }
}

# Optionally define dimension tables:

# 7A) User Dimension
resource "aws_dynamodb_table" "user_dimension" {
  name         = "UserDimension"
  billing_mode = "PAY_PER_REQUEST"

  # user_id as the PK
  hash_key = "user_id"

  attribute {
    name = "user_id"
    type = "S"
  }

  tags = {
    Name = "user-dimension-table"
  }
}

# 7B) Merchant Dimension
resource "aws_dynamodb_table" "merchant_dimension" {
  name         = "MerchantDimension"
  billing_mode = "PAY_PER_REQUEST"

  # merchant_id as the PK
  hash_key = "merchant_id"

  attribute {
    name = "merchant_id"
    type = "S"
  }

  tags = {
    Name = "merchant-dimension-table"
  }
}

# 7C) Payment Method Dimension
resource "aws_dynamodb_table" "payment_method_dimension" {
  name         = "PaymentMethodDimension"
  billing_mode = "PAY_PER_REQUEST"

  # payment_method_id as the PK
  hash_key = "payment_method_id"

  attribute {
    name = "payment_method_id"
    type = "S"
  }

  tags = {
    Name = "payment-method-dimension-table"
  }
}

