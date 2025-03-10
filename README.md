# cisco-assignment

## Working with this project

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

Directory Structure:

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

- **src** - Code for the application's Lambda function.
- **events** - Invocation events that you can use to invoke the lambda function locally.
- **tests** - Unit tests for the application code.
- **mock** - Contains different txt files to check pipeline on unusual inputs. You can upload these files in S3 bucket that was deployed and check the whole flow process from S3 bucket to Lambda function to SQS output.
- **template.yaml** - A template that defines the application's AWS resources.

### Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It can also emulate your application's build environment and API.

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
cisco-assignment$ pip install -r tests/requirements.txt --user
# unit test
cisco-assignment$ python -m pytest tests/unit -v
```
