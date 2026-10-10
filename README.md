# Predictive-Traffic-for-Cloud-Evironment
A Python-based cloud traffic management system that distributes web requests across multiple servers using Round Robin and resource-aware load balancing. It monitors server resources, predicts traffic, and tracks performance using Flask, MySQL, and Streamlit.
# Predictive traffic for Cloud Environment

Team ID: OSDBMS-V-2026-T238

A simple PBL prototype that compares Round Robin load balancing with
resource-aware routing using CPU, memory and active-request information.

## Workflow
Client Request -> Load Balancer -> Resource Check -> Server Selection
-> Web Server -> Response -> MySQL Logging -> Prediction/Dashboard

## Project Structure
- servers/              Simulated Flask web servers
- load_balancer/        Round Robin and resource-aware routing
- monitoring/           CPU, memory and process monitoring
- database/             MySQL connection and tables
- prediction/           Simple moving-average prediction
- dashboard/            Streamlit dashboard
- run_all.py            Starts the three simulated servers

## Setup
1. Install Python packages:
   pip install -r requirements.txt

2. Create a MySQL database/user, then edit database/db_config.py.

3. Create tables:
   mysql -u root -p < database/schema.sql

4. Start simulated servers:
   python run_all.py

5. In another terminal start the load balancer:
   python load_balancer/app.py

6. Open:
   http://127.0.0.1:5000/test?count=10&method=resource

7. For Round Robin:
   http://127.0.0.1:5000/test?count=10&method=round_robin

8. Start dashboard:
   streamlit run dashboard/app.py

## Routing
Round Robin:
request 1 -> server 1, request 2 -> server 2, request 3 -> server 3...

Resource-aware:
the load balancer checks CPU, memory and active requests and chooses
the server with the lowest calculated load score.

This is a same-machine simulation for academic/PBL demonstration.

