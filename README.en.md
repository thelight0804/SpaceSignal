# 🛰️ SpaceSignal

[한국어](README.md) | [日本語](README.ja.md)

**SpaceSignal** is a web service that allows you to intuitively explore real-time satellite positions and ground station communication logs on an interactive map.

> **Current Status:** Phase 1 in development (Location-based Satellite Tracking & Deployment)

## Project Goal
- **Real-time Satellite Tracking:** Calculate and visualize satellites passing over the user's current location in real-time.
- **Communication Log Analysis:** Monitor communication status based on satellite signal data received from ground stations worldwide.
- **Ground Station Visualization:** Provide map-based observation history of ground stations around the world.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### How to Run

1. Clone the project
```bash
git clone https://github.com/thelight0804/SpaceSignal
cd SpaceSignal
```

2. Run all services with Docker Compose
```bash
docker compose up
```

3. Access services
- **Backend API:** http://localhost:8000
- **Frontend:** http://localhost:5173
- **API Documentation (Swagger):** http://localhost:8000/docs

### Stopping Services
```bash
docker compose down
```

## Tech Stack

### Backend
- **Language:** Python 3.13+
- **Framework:** FastAPI
- **Database:** Amazon RDS for PostgreSQL 14+

### Frontend
- **Framework:** Svelte (Vite)

### Infrastructure
- **Container:** Docker & Docker Compose
- **Cloud:** AWS
- **IaC:** Terraform
- **CI/CD:** GitHub Actions

## Roadmap

### Phase 1: Location-based Satellite Tracking & Deployment (Current)
- [ ] Develop satellite position API based on user location
- [ ] Implement automatic TLE (Two-Line Element) data synchronization
- [ ] Build map UI with Svelte
- [ ] Containerize with Docker and configure docker-compose
- [ ] Deploy to AWS EC2 and configure network settings

### Phase 2: Satellite-specific Communication Log Query
- [ ] Design satellite communication log database
- [ ] Develop API for querying reception logs by satellite
- [ ] Visualize frequency bands by satellite

### Phase 3: Ground Station-specific Communication Log Query
- [ ] Develop API for querying global ground station locations and observation history
- [ ] Implement ground station filtering by country/region
