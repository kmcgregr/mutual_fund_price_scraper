# Use an official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements directly into container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY mutual_fund_price_scrapper.py .
COPY my_mutual_funds.csv .

# Default command to run the scraper
CMD ["python", "mutual_fund_price_scrapper.py"]
