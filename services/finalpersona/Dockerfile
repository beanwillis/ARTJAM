FROM python:3.7
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . finalPersona.py
COPY . artjam-287602-690502438d19.json
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["main.py"]