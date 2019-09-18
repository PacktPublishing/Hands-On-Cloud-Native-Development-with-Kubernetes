FROM python:3.6-alpine3.10
COPY requirements.txt /requirements.txt
COPY main.py /main.py

RUN pip install -r /requirements.txt
RUN chmod +x /main.py

ENTRYPOINT ["python", "main.py"]

