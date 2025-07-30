# flask-3tier
# Project Structure
flask-3tier/
├── backend/ /n
│   ├── Dockerfile /n
│   ├── app.py /n
│   ├── requirements.txt /n
│   └── wait-for-db.sh /n
├── nginx/ /n
│   ├── Dockerfile /n
│   └── nginx.conf /n
├── docker-compose.yml /n
└── .sample.env /n

# Build and start the containers
docker-compose up -d --build

# Verify all services are running
docker-compose ps

# Test the application
curl http://localhost /n
curl http://localhost/db /n
curl http://localhost/redis
