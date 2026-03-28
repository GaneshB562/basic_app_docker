FROM python:3.10

WORKDIR /app

COPY backend/ /app/backend/
COPY frontend/ /app/frontend/

WORKDIR /app/backend

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
