from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error
from fetch_stock_data import fetch_data
from process_data import processed_data
from database_setup import setup_database
from store_data import stored_data

app = Flask(__name__)

def get_stock_data():
    try:
        if fetch_data() == "Success":
            if processed_data() == "Success":
                if setup_database() == "Success":
                    if stored_data() == "Success":
                        
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='Venkataramana1998*',
                            database='stock_data_db'
                        )
                        if connection.is_connected():
                            cursor = connection.cursor(dictionary=True)
                            cursor.execute('SELECT * FROM stock_data')
                            rows = cursor.fetchall()
                            return rows
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/stocks', methods=['GET'])
def stocks():
    data = get_stock_data()
    return jsonify(data)

@app.route("/", methods = ['GET'])
def home():
    return "Welcome to the home page please type '/stocks' in the existing url to see the processed stocks data"

if __name__ == "__main__":
    app.run(debug=True)
    

