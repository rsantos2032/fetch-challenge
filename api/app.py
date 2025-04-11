from models import Item, Receipt
from collections import defaultdict
from werkzeug.exceptions import BadRequest
import uuid
import math
from datetime import datetime, time

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

receipts_cache = defaultdict(Receipt)

@app.route("/receipts/process", methods=["POST"])
def process_receipts():
    try:
        data = request.get_json()
        id = str(uuid.uuid4())
        receipt = Receipt()
        receipt.set_retailer(data["retailer"])
        receipt.set_purchase_date(data["purchaseDate"])
        receipt.set_purchase_time(data["purchaseTime"])
        receipt.set_total(data["total"])
        for i in data["items"]:
            item = Item(short_description=i["shortDescription"], price=i["price"])
            receipt.add_item(item)
        receipts_cache[id] = receipt
        return jsonify({"id": id}), 200
    except (BadRequest, KeyError) as e:
        return jsonify({"error": "The receipt is invalid"})
    
@app.route("/receipts/<id>/points", methods=["GET"])
def get_points(id: str):
    if id not in receipts_cache:
        return jsonify({"error": "No receipt found for that ID."})
    points = 0
    receipt = receipts_cache[id]
    
    # One point for every alphanumeric character in retailer
    retailer = receipt.get_retailer()
    for c in retailer:
        if c.isalnum():
            points += 1
            
    # 50 points if total has no cents (no decimals)
    total = float(receipt.get_total())
    if total % 1 == 0:
        points += 50
        
    # 25 points if total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25
        
    # 5 points for every two items on the receipt
    items = receipt.get_items()
    num_items = len(items)
    points += 5 * (num_items // 2)
    
    # Trimming item descriptions
    for item in items:
        desc = item.get_short_description()
        len_desc = len(desc.strip())
        # Check if multiple of 3
        if len_desc % 3 == 0:
            price = float(item.get_price())
            points += math.ceil(price * 0.2)
    
    # 6 points if pruchase date is odd
    purchase_date = receipt.get_purchase_date()
    day = int(purchase_date[8:10])
    if day % 2 == 1:
        points += 6
        
    # 10 points if purchase time is after 2:00pm and before 4:00pm
    purchase_time = receipt.get_purchase_time()
    purchase_time = datetime.strptime(purchase_time, "%H:%M").time()
    start_time = datetime.strptime("14:00", "%H:%M").time()
    end_time = datetime.strptime("18:00", "%H:%M").time()
    if start_time <= purchase_time <= end_time:
        points += 10
    
    return jsonify({"points": points})
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)