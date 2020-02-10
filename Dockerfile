FROM library/python:3.8.1-alpine
LABEL maintainer="Joan Font <joanfont@gmail.com>"

WORKDIR /app
ADD requirements.txt .

RUN apk add --no-cache --update --virtual .build-deps build-base \
    && pip3 install -r requirements.txt \
    && apk del .build-deps

ADD app.py .
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "app:app"]