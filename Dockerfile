FROM python 
WORKDIR /home/natalia/Proyectos/proyecto-terminal/
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]