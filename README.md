# Grafana & Prometheus Admin

This repository demonstrates a complete **Grafana and Prometheus monitoring stack** for real-world observability, built for **SRE, DevOps, and Infrastructure teams**.

It includes:
- Pre-configured **Prometheus server** with alerts
- **Grafana dashboards** for infrastructure and Kubernetes
- **Node Exporter** and **custom Python exporter** for app metrics
- **Docker Compose deployment** for local testing

## Features
- ✅ Prometheus scraping and alerting rules
- ✅ Grafana dashboards for Linux servers, containers, and apps
- ✅ Pre-configured data sources
- ✅ Easy local deployment using Docker
- ✅ Custom metrics exporter example

## Folder Structure
```
grafana-prometheus-admin/
├── grafana/            # Grafana dashboards and config
├── prometheus/         # Prometheus configs & alerts
├── exporters/          # Exporters for system and app metrics
├── scripts/            # Setup and deployment scripts
└── docker-compose.yml  # Local deployment
```

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/omgwarrior/grafana-prometheus-admin.git
cd grafana-prometheus-admin
```

### 2. Start the Stack
```bash
docker-compose up -d
```

### 3. Access Web Interfaces
- **Grafana** → http://localhost:3000  
  Username: `admin` | Password: `admin`

- **Prometheus** → http://localhost:9090

## Example Dashboards
- Linux server monitoring
- Kubernetes cluster overview
- Application-level metrics

## License
MIT License
