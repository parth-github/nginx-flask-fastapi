FROM python:3.11-slim

WORKDIR /app
COPY app.py .
COPY tests/ ./tests/

# Install Flask and Gunicorn
RUN pip install flask gunicorn pytest pytest-cov
ENV PYTHONPATH=/app
# Use Gunicorn to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
EXPOSE 5000

# add test command
# CMD ["pytest", "tests/"]
