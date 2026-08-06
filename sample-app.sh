#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp sample-app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/natalia/Proyectos/proyecto-terminal/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/natalia/Proyectos/proyecto-terminal/templates/" >> tempdir/Dockerfile
echo "COPY sample-app.py /home/natalia/Proyectos/proyecto-terminal" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile

echo "CMD python3 /home/natalia/Proyectos/proyecto-terminal/sample-app.py" >> tempdir/Dockerfile

