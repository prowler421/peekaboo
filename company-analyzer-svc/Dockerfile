# syntax=docker/dockerfile:1.6

FROM python:3.11-slim AS requirements-stage

WORKDIR /tmp
RUN pip install --no-cache-dir poetry==1.5.1
COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --only main

FROM python:3.11-slim

WORKDIR /code
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

EXPOSE 8000
CMD [ "uvicorn", "company_analyzer_svc.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers" ]
