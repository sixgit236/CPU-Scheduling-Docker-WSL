FROM python:3.9-slim
WORKDIR /app
RUN pip install flask mysql-connector-python
COPY scheduler.py .
CMD ["python", "scheduler.py"]
