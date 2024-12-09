from flask import Flask, request, jsonify
from pymongo import MongoClient,errors
from flask_cors import CORS
from pymongo.errors import DuplicateKeyError

app=Flask(__name__)
CORS(app)
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

# Function to initialize empID at startup
def initialize_emp_id():
    global current_emp_id
    db=client[db_name]
    collection=db[collection_name]
    last_document = collection.find_one(sort=[("empID", -1)])  # Get the highest empID
    current_emp_id = last_document["empID"] + 1 if last_document else 1  # Start from 1 if no records

initialize_emp_id()
@app.route('/insert', methods=['POST'])
def create_database_and_insert_data():
        global current_emp_id
        
        try:    
                db=client[db_name]
                collection=db[collection_name]
                data=request.json
                empData=data.get('emp_data', [])[0]
                if not db_name or not collection_name or not empData:
                    return jsonify({"error": "Database, collection, and empData are required"}), 400
                
                if empData:
                    username = empData.get('username')

        # Check for duplicates
                    existing_employee = collection.find_one({'username': username})
                    if existing_employee:
                        return jsonify({"error": "Employee with this username already exists"}), 400

                    # db=client[db_name]
                    # collection=db[collection_name]
                    collection.create_index("empID",unique=True)
                 
                    empData["empID"] = current_emp_id  # Assign the next available empID
                    current_emp_id += 1 
                    collection.insert_one(empData)
                    return jsonify({"message": f"Inserted {len(empData)} records successfully"}), 201
        except DuplicateKeyError as e:
            return jsonify({"error": "Duplicate data, try again"}), 400
                        

        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/read',methods=['GET'])
def read_database():
        try:
            empId=request.args.get("empID")
            db=client[db_name]
            collecion=db[collection_name]
            if empId:
                result=collecion.find_one({"empID": int(empId)})
                if result:
                        result["_id"] = str(result["_id"])  # Convert ObjectId to string for JSON serialization
                        return jsonify({"message": "Record fetched Successfully","result":result}), 200
                else:
                    return jsonify({"error": "Record Not Found"}),404
            else:
                result=list(collecion.find())
                for record in result:
                    record["_id"] = str(record["_id"])  # Convert ObjectId to string for JSON serialization
                return jsonify({"message": "Record fetched Successfully","result":result}), 200

        except Exception as e:
            return jsonify({"error":str(e)}),500 

@app.route('/update',methods=['PUT'])
def update_database():
    try:
        data=request.json
        empId=data.get("empID")
        updatedData=data.get("updated_data")
        if not empId or not updatedData:
            return jsonify({"error": "empId and updatedData are required"}), 400
        db=client[db_name]
        collection=db[collection_name]
        result=collection.update_one({"empID": int(empId)},{"$set": updatedData})
        if result.matched_count>0:
            return jsonify({"message": "Record Updated Successfully"}), 200
        else:
            return jsonify({"message": "Record not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete', methods=['DELETE'])
def delete_database():
        try:
            empId=request.args.get("empID")
            if not empId:
                  return jsonify({"error":"empId can't be empty"})
            db=client[db_name]
            collecion=db[collection_name]
            result=collecion.delete_one({"empID": int(empId)})
            if result.deleted_count>0:
                  return jsonify({"message": "Record Deleted Successfully"}), 200
            else:
                return jsonify({"error": "Record Not Found"}),404
        except Exception as e:
            return jsonify({"error":str(e)}),500 


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)

