# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.10-slim
# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code to the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8001

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
