# cisco-assignment

### Working with this project

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

```bash
└── ./
    ├── events
    ├── src
    │   ├── app.py
    │   └── network_analyzer.py
    └── tests
        ├── mock
        └── unit
```

- **src** - Code for the application's Lambda function. *app.py* file contains Lambda function for AWS. *network_analyzer.py* contains Kruskal's algorithm implementation for finding cheapest route through every node in a graph.
- **tests** - Unit tests for the application code.
- **mock** - Contains different txt files to check pipeline on unusual inputs. You can upload these files in S3 bucket that was deployed and check the whole flow process from S3 bucket to Lambda function to SQS output.
- **template.yaml** - A template that defines the application's AWS resources.

### Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications.

To use the SAM CLI, you need the following tools.

- SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Python 3 installed](https://www.python.org/downloads/)
To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

### Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
pip install -r tests/requirements.txt --user
# unit tests
python -m pytest tests/unit -v
```
