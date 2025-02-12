How to Develop and Run

    Install the Shared Module Locally (Optional):
    From the project root, you can install the shared module in editable mode:

cd modules
pip install -e .
cd ..

Run a Processor Locally:
For example, to run the Orchestrator processor:

cd processors/Orchestrator
python OrchestratorMain.py

Build Docker Images:
Build each processor’s Docker image from its folder. For example, for Orchestrator:

cd processors/Orchestrator
docker build -t orchestrator_processor .

Deploy Each Processor:
Each processor runs as its own Docker container and imports the shared module from the global installation or via the copied files.
