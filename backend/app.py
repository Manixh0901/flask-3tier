from flask import Flask, jsonify
import os
import psycopg2
import redis

app = Flask(__name__)

# Get environment variables
DB_HOST = os.getenv('POSTGRES_HOST')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
REDIS_HOST = os.getenv('REDIS_HOST')

@app.route('/')
def hello():
    return jsonify(message="Hello from Flask!")

@app.route('/db')
def db_check():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        conn.close()
        return jsonify(status="Database connection successful")
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/redis')
def redis_check():
    try:
        r = redis.Redis(host=REDIS_HOST, port=6379)
        r.ping()
        return jsonify(status="Redis connection successful")
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
