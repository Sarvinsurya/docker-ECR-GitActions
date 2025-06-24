# Flask Docker + ECR Example

This project demonstrates a simple Flask application that is containerized with Docker and can be pushed to AWS ECR using GitHub Actions.

## Running Locally

```bash
docker build -t flask-ecr-demo .
docker run -p 5000:5000 flask-ecr-demo
```
Visit http://localhost:5000 to see the app.

## GitHub Actions Workflow
- Builds the Docker image
- Scans for vulnerabilities
- Pushes to ECR if no high/critical vulnerabilities are found

## Requirements
- AWS ECR repository
- GitHub repository secrets for AWS credentials

## Flask App
The app will respond with `Hello from docker+ecr` at the root endpoint (`/`).
# docker-ECR-GitActions
