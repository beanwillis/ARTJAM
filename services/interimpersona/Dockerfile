FROM python:3.7
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . finalPersona.py
COPY . artjam-287602-c4a440e2da91.json
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["interimPersona.py"]