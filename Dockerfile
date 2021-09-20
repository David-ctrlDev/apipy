FROM alpine:latest
RUN apk update \
&& apk add --virtual build-dependencies


RUN apk add --no-cache python3
RUN  apk add py3-pip \
    && pip3 install --upgrade pip \
    && pip install google-crc32c

WORKDIR /app

COPY . /app/

RUN pip install FLASK

CMD ["py","servidor/servidor.py"]