# Use an official Python runtime as a parent image.
FROM python:3.9-slim

# Set working directory in the container.
WORKDIR /app

# Copy the global requirements file and install dependencies.
COPY ../../requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the shared module and the local Orchestrator project files.
COPY ../../modules/servicebus_consumer ./servicebus_consumer
COPY . .

# Define the default command to run the main application.
CMD ["python", "OrchestratorMain.py"]
