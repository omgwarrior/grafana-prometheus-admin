#!/bin/bash
echo "Deploying updated configuration..."
docker-compose down
docker-compose up -d
echo "Deployment complete."
