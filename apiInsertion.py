from flask import Flask, request, jsonify
from pymongo import MongoClient,errors
from pymongo.errors import DuplicateKeyError

app=Flask(__name__)
db_name="employee"
collection_name="information"

def connect_to_mongodb():
        try:
                client= MongoClient("mongodb://localhost:27017/")
                print("connected to mongodb successfullt")
                return client
        except errors.ConnectionError as e:
                print(f"Error connecting to mongodb: {e}")
                exit(1)
client=connect_to_mongodb()

@app.route('/insert', methods=['POST'])
def create_database_and_insert_data():
        try:
                data=request.json
                empData=data.get("emp_data")
                if not db_name or not collection_name or not empData:
                    return jsonify({"error": "Database, collection, and empData are required"}), 400
                db=client[db_name]
                collection=db[collection_name]
                collection.create_index("empID",unique=True)
                for Data in empData:
                    try:
                        collection.insert_one(Data)
                    except DuplicateKeyError as e:
                        return jsonify({"error": "Duplicate data, try again"}), 400
                return jsonify({"message": f"Inserted {len(empData)} records successfully"}), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
