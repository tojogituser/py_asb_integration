from setuptools import setup, find_packages

setup(
    name="servicebus_consumer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "azure-servicebus>=7.0.0",
    ],
)
