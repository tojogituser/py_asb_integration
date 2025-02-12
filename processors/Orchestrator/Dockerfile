# processors/Orchestrator/Dockerfile
FROM python:3.9-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the global requirements file from the project root.
COPY requirements.txt .

# Upgrade pip and install the global dependencies.
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire modules folder (which includes setup.py and the shared module).
COPY modules ./modules

# Copy the Orchestrator processor project files.
COPY processors/Orchestrator/ .

# Install the shared module in editable mode using the modules folder.
RUN pip install -e ./modules

# Define the default command to run the main application.
CMD ["python", "OrchestratorMain.py"]
