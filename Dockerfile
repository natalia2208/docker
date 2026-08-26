FROM python
WORKDIR /app

RUN apt-get update && apt-get upgrade -y 

COPY requirements.txt .

RUN pip install  -r requirements.txt

COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]