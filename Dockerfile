FROM python:3.8-slim

#WORKDIR /app

COPY . .

#RUN pip install --upgrade pip -- only first time

RUN pip install -r requirements.txt

CMD ["python", "app.py"]