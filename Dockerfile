FROM python:3.9-slim-buster

RUN pip install fettuccine

COPY action_script.py /action_script.py

CMD ["python", "/action_script.py"]
