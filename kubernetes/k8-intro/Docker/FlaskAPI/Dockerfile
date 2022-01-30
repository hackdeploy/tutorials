FROM python:3.8-slim

# creates a dir for our application
WORKDIR /app

# copy our requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of our application
COPY . .

CMD gunicorn --worker-class sync --workers 4 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 120 --keep-alive 20 --log-level info