FROM python:3.10-slim

WORKDIR /coqueiraldevweb2

COPY . /coqueiraldevweb2

ENV PYTHONPATH="/coqueiraldevweb2/coqueiral:${PYTHONPATH}"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python coqueiral/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "coqueiral.wsgi:application"]