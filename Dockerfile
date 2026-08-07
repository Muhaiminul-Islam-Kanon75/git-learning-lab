FROM python:3.12-slim

RUN mkdir /logs

WORKDIR /apps

COPY . /apps/

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python3", "-m", "app.main" ]


#FROM python:3.12-slim

#WORKDIR /apps
#
#COPY . ./apps 
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#EXPOSE 8000
#
#ENTRYPOINT ["python3", "-m", "app.main"]


