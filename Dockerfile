FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (to leverage Docker cache)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose the port that your app will be running on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
