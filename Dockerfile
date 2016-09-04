FROM python:3.5-alpine

WORKDIR /var/www

COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./kgitb /var/www/kgitb

EXPOSE 5000
CMD ["python3", "-m", "kgitb"]
