FROM python:3.9-slim-buster

RUN pip install fettuccine

COPY action_script.py /action_script.py

ENTRYPOINT ["python", "/action_script.py"]