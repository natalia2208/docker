FROM python:3.12-slim
WORKDIR /app

# Actualiza el sistema base y fuerza la actualización de herramientas vulnerables
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --force-reinstall -r requirements.txt

COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]