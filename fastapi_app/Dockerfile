FROM python:3.11-slim

WORKDIR /app
COPY main.py .
COPY tests/ ./tests/
ENV PYTHONPATH=/app
RUN pip install fastapi uvicorn pytest pytest-cov httpx

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#EXPOSE 8000

# add test command
# CMD ["pytest", "tests/"]