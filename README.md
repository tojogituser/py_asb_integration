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
If installing in editable mode still doesn't work, here are some additional troubleshooting steps:

    Verify Your Setup File and Package Structure:
        In your modules/setup.py, ensure that your package is discovered correctly. For example, your setup.py should look something like:

from setuptools import setup, find_packages

setup(
    name="servicebus_consumer",
    version="0.1.0",
    packages=find_packages(),  # This should find servicebus_consumer
    install_requires=[
        "azure-servicebus>=7.0.0",
    ],
)

    Make sure that modules/servicebus_consumer/__init__.py exists (even an empty file is enough).

Reinstall the Module:

    From your project root (the directory containing both modules/ and processors/), run:

    pip uninstall servicebus_consumer
    pip install -e modules

    This forces a reinstall. Verify that the installation output shows that the package is installed in editable mode.

Check the Installation:

    Run the following command to see if Python can locate the package:

    python -c "import servicebus_consumer; print(servicebus_consumer.__file__)"

    This should print the path to your servicebus_consumer package. If it raises an error, then the module isn't being found.

PYTHONPATH Issue:

    Sometimes the editable install may not work as expected if there are environment issues. You can try manually adding the modules folder to your PYTHONPATH. In your project root, run:
        On Unix/macOS:

export PYTHONPATH=$(pwd)/modules:$PYTHONPATH
python processors/Orchestrator/OrchestratorMain.py

On Windows (Command Prompt):

        set PYTHONPATH=%cd%\modules;%PYTHONPATH%
        python processors\Orchestrator\OrchestratorMain.py

Virtual Environment Considerations:

    Ensure you're working in the correct virtual environment (if using one). Sometimes the editable install happens in one environment while you're running the script in another.

Double-Check Import Statements:

    In your processor code (e.g., OrchestratorMain.py), the import should be:

from servicebus_consumer.consumer import ServiceBusConsumer
docker build -f processors/Orchestrator/Dockerfile -t orchestrator_processor .
docker build -f processors/Orchestrator/Dockerfile -t orchestrator_processor .

docker build -f processors/TaskX/Dockerfile -t taskx_processor .
