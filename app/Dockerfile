FROM python:3.11.9-slim-bookworm

LABEL MAINTAINER="phipsi@gmx.ch"

# ENV GROUP_ID=1000 \
#     USER_ID=1000

WORKDIR /var/www/

ADD . /var/www/
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Add user for flask application
# RUN addgroup -g $GROUP_ID www
# RUN adduser -D -u $USER_ID -G www www -s /bin/sh

# Change current user to www
# USER www

EXPOSE 5020

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5020", "wsgi"]