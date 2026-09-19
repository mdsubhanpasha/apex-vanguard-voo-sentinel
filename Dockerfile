FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Run main analysis engine to generate initial metrics
RUN python src/main.py

EXPOSE 8080 8000

# Default command launches dashboard server
CMD ["python", "dashboard/app.py"]
