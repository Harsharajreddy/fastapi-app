# FastAPI Order Service  

A simple backend service built using FastAPI that allows users to place trade orders and retrieve submitted orders. The application is containerized using Docker and deployed on AWS EC2 with a CI/CD pipeline using GitHub Actions.  

## Features  
- REST API with `POST /orders` and `GET /orders`  
- SQLite Database for order storage  
- Dockerized Application for easy deployment  
- AWS EC2 Deployment (Ubuntu)  
- GitHub Actions CI/CD Pipeline for automation  
- Swagger UI for API documentation  

## Tech Stack  
- FastAPI (Python)  
- SQLite  
- Docker  
- GitHub Actions  
- AWS EC2 (Ubuntu)  

## Installation  

### Prerequisites  
- Python 3.9+  
- Docker and Docker Compose  

### Clone the Repository  
```sh
git clone https://github.com/Harsharajreddy/fastapi-app.git
cd fastapi-app
```

### Install Dependencies  
```sh
pip install -r requirements.txt
```

### Run the Application Locally  
```sh
uvicorn main:app --reload
```
Access the API at: `http://127.0.0.1:8000/docs`  

## Docker Setup  

### Build and Run the Docker Container  
```sh
docker build -t fastapi-app .
docker run -p 80:80 fastapi-app
```
The API will be accessible at: `http://localhost/docs`  

### Using Docker Compose  
```sh
docker-compose up -d --build
```

## Running Tests  
```sh
pytest
```

## Deployment on AWS EC2  

1. Launch an EC2 instance (Ubuntu).  
2. Install Docker and Docker Compose:  
   ```sh
   sudo apt update && sudo apt install -y docker.io docker-compose
   ```
3. Clone the repository on EC2:  
   ```sh
   git clone https://github.com/Harsharajreddy/fastapi-app.git
   cd fastapi-app
   ```
4. Run the application using Docker Compose:  
   ```sh
   docker-compose up -d --build
   ```
5. Access the API at `http://<EC2-IP>/docs`  

## CI/CD with GitHub Actions  

The GitHub Actions workflow is configured to:  
- Run tests on pull requests  
- Build and push the Docker image  
- Deploy the latest version to the EC2 instance on merge to the master branch  

### Setting up Secrets in GitHub  
Ensure the following secrets are added to your repository:  
- `EC2_SSH_KEY`: Base64-encoded private key for SSH access  
- `EC2_IP`: Public IP of the EC2 instance  

## API Endpoints  

### Create an Order  
**POST /orders/**  
```json
{
  "symbol": "AAPL",
  "price": 150.50,
  "quantity": 10,
  "order_type": "buy"
}
```
Response:  
```json
{
  "id": 1,
  "symbol": "AAPL",
  "price": 150.50,
  "quantity": 10,
  "order_type": "buy"
}
```

### Get All Orders  
**GET /orders/**  
Response:  
```json
[
  {
    "id": 1,
    "symbol": "AAPL",
    "price": 150.50,
    "quantity": 10,
    "order_type": "buy"
  }
]
```
```
