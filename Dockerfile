# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define environment variables
ENV SLACK_API_TOKEN=${SLACK_API_TOKEN}
ENV SLACK_SIGNING_SECRET=${SLACK_SIGNING_SECRET}
ENV GROQ_API_TOKEN=${GROQ_API_TOKEN}
ENV FLASK_DEBUG=${FLASK_DEBUG}

# Run the application
CMD ["python", "app.py"]
