# flask-3tier
# Project Structure
flask-3tier/
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── wait-for-db.sh
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── docker-compose.yml
└── .sample.env

# Build and start the containers
docker-compose up -d --build

# Verify all services are running
docker-compose ps

# Test the application
curl http://localhost
curl http://localhost/db
curl http://localhost/redis
