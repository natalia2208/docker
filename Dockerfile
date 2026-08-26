FROM python 
WORKDIR /home/natalia/Proyectos/proyecto-terminal/
COPY requirements.txt .


# Actualiza el sistema base y fuerza la actualización de herramientas globales
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1"

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]