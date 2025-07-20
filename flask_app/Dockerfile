FROM python:3.11-slim

WORKDIR /app
COPY app.py .

# Install Flask and Gunicorn
RUN pip install flask gunicorn pytest pytest-cov

# Use Gunicorn to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
EXPOSE 5000