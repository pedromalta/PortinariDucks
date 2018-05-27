FROM python:3.5.5-alpine3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install requests
RUN pip install pymongo
RUN pip install pytz

COPY . ./

CMD ["python", "app.py"]
