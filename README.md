# sciative_assignment_devops1

## Stack
- FastAPI (Backend)
- React (Frontend)
- Nginx (Reverse Proxy)
- Cron Jobs
- AWS S3 (Log Archival)

## Features
- /api1 → Public API
- /api2 → Internal API (blocked via Nginx)
- Cron job calls internal API
- Logs stored + rotated + uploaded to S3

## Setup

### Backend
cd backend
pip install -r requirements.txt
gunicorn -k uvicorn.workers.UvicornWorker   main:app --bind 127.0.0.1:8000

### Frontend
cd frontend
npm install
npm run build

### Nginx
sudo cp nginx/nginx.conf /etc/nginx/nginx.conf
sudo systemctl restart nginx

### Cron
crontab -e
*/5 * * * * python3 /scripts/api2_cron.py
