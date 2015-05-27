from setuptools import setup

setup(
    name="signingworker",
    version="0.1",
    description="TaskCluster Signing Worker",
    author="Mozilla Release Engineering",
    packages=["signingworker"],
    entry_points={
        "console_scripts": [
            "signing-worker = signingworker.consumer:main",
        ],
    },
    install_requires=[
        "arrow",
        "configman",
        "jsonschema",
        "kombu",
        "redo",
        "requests==2.4.3",  # Because taskcluster hard pins this version...
        "sh",
        "taskcluster>=0.0.16",
    ],
)
