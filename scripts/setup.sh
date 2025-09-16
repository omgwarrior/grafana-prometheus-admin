#!/bin/bash
echo "Setting up Grafana and Prometheus stack..."
docker-compose up -d
echo "Setup complete. Access Grafana at http://localhost:3000 and Prometheus at http://localhost:9090"
