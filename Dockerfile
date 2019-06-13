FROM python:3.7-alpine

WORKDIR /tmp
COPY Pipfile.lock /tmp/
COPY Pipfile /tmp/

RUN pip install -U pip==18.1 pipenv==2018.10.13 \
&& pipenv install --system --deploy --ignore-pipfile

COPY . /opt/app
WORKDIR /opt/app

CMD ["python", "-m", "maas"]
