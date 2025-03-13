
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 

EXPOSE 5000

ENV FLASK_APP=app.py

##CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]
