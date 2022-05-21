FROM python:3.10

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY flask-app.py .

CMD [ "python", "./flask-app.py" ]
