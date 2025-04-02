from flask import Flask, request, jsonify
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

# In-memory storage of fake transactions
transactions_data = []


def generate_fake_transactions(num=50):
    """
    Generate 'num' transaction records using Faker and random logic.
    """
    possible_currencies = ["USD", "EUR", "GBP", "CAD", "AUD"]
    transaction_types = ["purchase", "refund", "withdrawal", "deposit"]
    for _ in range(num):
        record = {
            "transaction_id": str(fake.uuid4()),
            "user_id": str(fake.uuid4()),
            "currency": random.choice(possible_currencies),
            "amount": round(random.uniform(5, 1000), 2),
            "transaction_type": random.choice(transaction_types),
            "timestamp": fake.date_time_between("-1y", "now").isoformat(),
        }
        transactions_data.append(record)


# Generate initial data
generate_fake_transactions(100)


@app.route("/transactions", methods=["GET"])
def get_transactions():
    """
    Example usage:
      GET /transactions?currency=USD&min_amount=10&max_amount=500&page=2&limit=10
    Returns filtered & paginated transactions in JSON.
    """
    # Copy the data so we can filter it
    filtered_data = transactions_data.copy()

    # Parse query params
    currency = request.args.get("currency")  # e.g. /transactions?currency=USD
    min_amount = request.args.get("min_amount")  # e.g. /transactions?min_amount=10
    max_amount = request.args.get("max_amount")  # e.g. /transactions?max_amount=500
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=20, type=int)

    # Filter by currency
    if currency:
        filtered_data = [tx for tx in filtered_data if tx["currency"] == currency]

    # Filter by min_amount
    if min_amount is not None:
        try:
            min_val = float(min_amount)
            filtered_data = [tx for tx in filtered_data if tx["amount"] >= min_val]
        except ValueError:
            pass  # ignore if not numeric

    # Filter by max_amount
    if max_amount is not None:
        try:
            max_val = float(max_amount)
            filtered_data = [tx for tx in filtered_data if tx["amount"] <= max_val]
        except ValueError:
            pass

    # Pagination
    start_idx = (page - 1) * limit
    end_idx = start_idx + limit
    paged_data = filtered_data[start_idx:end_idx]

    # Create response
    response = {
        "page": page,
        "limit": limit,
        "total_records": len(filtered_data),
        "returned_records": len(paged_data),
        "data": paged_data
    }
    return jsonify(response), 200


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True, port=5000)