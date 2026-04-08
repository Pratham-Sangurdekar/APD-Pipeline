FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install opencv-python-headless numpy

CMD ["python", "app.py"]