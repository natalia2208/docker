FROM python:3.14-slim
RUN apt-get update && apt-get upgrade -y
WORKDIR /home/capsdevp/Documentos/workspace/docker/my-app/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --upgrade "jaraco.context>=6.1.0" "wheel>=0.46.2"
COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]