FROM python:3.7-slim

ADD . /carbon
WORKDIR /carbon

RUN pip install -r requirements.txt

CMD [ "python", "run.py" ]


