FROM python:3.15.0rc2-alpine3.24
LABEL maintainer='Emamul Haque Manna'

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY . /django-tutorial
WORKDIR /django-tutorial

ARG DEV=false
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        manna

ENV PATH="/venv/bin:$PATH"
USER manna
