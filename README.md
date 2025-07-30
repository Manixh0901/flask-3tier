
Thank you for pointing that out! Let's ensure that the formatting for all steps is consistent throughout the README. Here’s the revised version with uniform formatting for all steps:

## 📄 Revised README File

```markdown
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
   ```

2. Configure environment variables:
   ```bash
   cp .env.sample .env
   nano .env  # Edit with your credentials
   ```

3. Start the services:
   ```bash
   docker-compose up -d --build
   ```

4. Verify:
   ```bash
   curl http://localhost
   ```

## 🌐 Service Endpoints
| Endpoint         | Description                     |
|------------------|---------------------------------|
| GET /            | Hello World                    |
| GET /db         | Test PostgreSQL connection      |
| GET /redis      | Test Redis connection           |

## 🛠️ Project Structure
```
flask-3tier/
├── backend/          # Flask application
├── nginx/            # Nginx configuration
├── docker-compose.yml # Orchestration
├── .env.sample       # Environment template
├── .dockerignore     # Docker ignore rules
└── .gitignore        # Git ignore rules
```

## 🔧 Troubleshooting
- **502 Bad Gateway**: Check if the backend is running:
   ```bash
   docker-compose logs backend
   ```

- **Database issues**: Verify PostgreSQL health:
   ```bash
   docker-compose exec db pg_isready
   ```

```

### Key Adjustments:
- Ensured that all steps in the **Installation** section have consistent formatting with code blocks clearly defined.
- Maintained uniformity in the presentation of commands and instructions.

Feel free to modify any specific details, such as the GitHub repository link, to match your actual project. If you need further adjustments or have additional content to include, just let me know!
