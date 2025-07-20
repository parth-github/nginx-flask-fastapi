# NGINX + Flask + FastAPI Microservices Gateway

This project demonstrates a microservices architecture with:

- **Flask** for legacy or synchronous APIs
- **FastAPI** for modern asynchronous APIs
- **NGINX** as a reverse proxy/API Gateway
- **Docker Compose** for orchestration

## Endpoints

- `GET /flask/hello` → Flask microservice
- `GET /fastapi/hello` → FastAPI microservice
- `GET /` → Welcome from NGINX

## Getting Started

```bash
docker-compose up --build

## 📌 Optional Add-ons
- Add **unit tests** for both apps using `pytest`
- Add **JWT authentication** and rate limiting via NGINX
- Use **Gunicorn** for Flask instead of built-in server
- Add CI via **GitHub Actions**

Would you like me to:
- ✅ Generate a GitHub repo template for this project?
- 🚀 Extend this for Kubernetes (Helm + Ingress + Services)?
- 🔐 Add OAuth2/JWT authentication middleware?

Let me know what direction you’d like to go next!
