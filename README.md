# Microservices DevOps Application

This project is a simple microservices-based e-commerce application built with modern DevOps practices.

---

## Technologies Used

- **Languages:** Python, Node.js  
- **Containerization:** Docker, Docker Compose  
- **Orchestration:** Kubernetes, Helm  
- **Monitoring:** Prometheus, Grafana  
- **CI/CD:** GitHub Actions  
- **Version Control:** Git, GitHub  
- **Platform Support:** Windows, Linux, macOS  

---

## Architecture Overview

The application consists of three microservices:

- **product-service:** Manages product data  
- **cart-service:** Handles shopping cart operations  
- **order-service:** Processes orders  

These services communicate with each other to complete typical e-commerce workflows.

---

## How to Run Locally

### Prerequisites

- Install Docker and Docker Compose

### Steps

1. Clone the repository:

  
git clone https://github.com/yourusername/microservices-devops.git
   
Start the application:

Open powershell

docker-compose up --build -d
Access services:

Product Service: http://localhost:5002

Cart Service: http://localhost:5003

Order Service: http://localhost:5004

Access monitoring dashboards:

Prometheus: http://localhost:9090

Grafana: http://localhost:3000 

Monitoring
Prometheus collects metrics from all services, while Grafana provides dashboards to visualize service health and performance.

CI/CD Pipeline
GitHub Actions automates the build, test, and deployment process by:

Building Docker images on code changes

Pushing images to Docker Hub

Deploying services to Kubernetes using Github actions

Steps to Install
Add the Helm repository and update:

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
Install Prometheus:


helm install prometheus prometheus-community/prometheus
Install Grafana:


helm install grafana prometheus-community/grafana
Get the Grafana admin password:


kubectl get secret grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
Forward Grafana port to localhost:


kubectl port-forward svc/grafana 3000:80
Open your browser and go to:

http://localhost:3000
