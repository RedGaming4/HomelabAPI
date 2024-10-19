# Server Management Dashboard

## Overview

This repository contains a FastAPI application that serves as a management dashboard for monitoring and managing three servers, including a Raspberry Pi and two other servers. The application communicates with Docker containers running on these servers and displays various metrics, allowing for real-time monitoring and management.

## Features

- List all Docker containers across the three servers.
- Display key metrics for each container (e.g., name, ID, status, image).
- Integrate with Prometheus to expose metrics for monitoring.
- Serve a web interface using Jinja2 templates.
- provide minecraft server metrics such as tps etc through opensource plugin.

## Requirements

- Python 3.7+
- FastAPI
- Docker SDK for Python
- Prometheus Client
- Jinja2

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   
## Install dependencies:

It is recommended to create a virtual environment before installing the dependencies.

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt, you can manually install the required packages:

bash
Copy code
pip install fastapi[all] docker prometheus_client
Configure your environment:

If you have any sensitive information (e.g., API keys, database credentials), create a .env file in the project root and add your variables there. This file will be ignored by Git.

Running the Application
Start your FastAPI application:

bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000
Replace main with the name of your Python file if it's different.

Access the Dashboard:

Open your web browser and navigate to http://localhost:8000 to view the dashboard.

Access Prometheus Metrics:

You can access the metrics endpoint at http://localhost:8000/metrics, which Prometheus can scrape for monitoring.

Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements!
