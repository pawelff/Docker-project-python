FROM python:3.6-alpine
WORKDIR /python-mysql/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir mysql-connector-python
ADD https://raw.githubusercontent.com/pawelff/Docker-project-python/master/app.py ./app.py
CMD ["python app.py"]
