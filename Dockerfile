FROM python:3.8-slim-buster 
RUN apt-get update && apt-get upgrade -y
WORKDIR /home/capsdevp/Documentos/workspace/docker/my-app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]