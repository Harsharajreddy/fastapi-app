FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all your application files into the container
COPY . /app

# Install dependencies from requirements.txt, including pytest for tests
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the FastAPI app
EXPOSE 80

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
