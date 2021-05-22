FROM python: 3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements



