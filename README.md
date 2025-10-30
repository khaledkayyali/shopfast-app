# ShopFast E-Commerce Application

A 3-tier e-commerce application with CI/CD pipeline.

## Architecture

- **Frontend**: Nginx serving static HTML/CSS/JS
- **Backend**: Flask REST API
- **Database**: PostgreSQL

## Components

- `web/` - Nginx frontend
- `api/` - Flask backend API
- `db/` - Database initialization scripts
- `k8s/` - Kubernetes manifests
- `jenkins/` - Jenkins pipeline configuration

## Deployment

This application is deployed on Kubernetes with:
- Docker containers
- Jenkins CI/CD
- Horizontal Pod Autoscaling
- Ingress for external access
