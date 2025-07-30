
# Flask 3-Tier Architecture with Docker

![Docker](https://img.shields.io/badge/Docker-3-tier%20architecture-blue)
![Flask](https://img.shields.io/badge/Backend-Flask-green)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blueviolet)

A scalable 3-tier web application with:
- **Presentation Tier**: Nginx reverse proxy
- **Application Tier**: Flask backend
- **Data Tier**: PostgreSQL (persistent) + Redis (caching)

## 🚀 Quick Start

### Prerequisites
- Docker 20.10+
- Docker Compose 2.0+

### Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/flask-3tier.git
   cd flask-3tier

    Configure environment variables:
    bash

cp .env.sample .env
nano .env  # Edit with your credentials

Start the services:
bash

docker-compose up -d --build

Verify:
bash

    curl http://localhost

🌐 Service Endpoints
Endpoint	Description
GET /	Hello World
GET /db	Test PostgreSQL connection
GET /redis	Test Redis connection
🛠️ Project Structure
text

flask-3tier/
├── backend/          # Flask application
├── nginx/            # Nginx configuration
├── docker-compose.yml # Orchestration
├── .env.sample       # Environment template
├── .dockerignore     # Docker ignore rules
└── .gitignore        # Git ignore rules

🔧 Troubleshooting

    502 Bad Gateway: Check if backend is running:
    bash

docker-compose logs backend

Database issues: Verify PostgreSQL health:
bash

docker-compose exec db pg_isready
