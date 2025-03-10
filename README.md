# cisco-assignment

Congratulations, you have just created a Serverless "Hello World" application using the AWS Serverless Application Model (AWS SAM) for the `python3.12` runtime, and options to bootstrap it with [**AWS Lambda Powertools for Python**](https://awslabs.github.io/aws-lambda-powertools-python/latest/) (Lambda Powertools) utilities for Logging, Tracing and Metrics.

Powertools is a developer toolkit to implement Serverless best practices and increase developer velocity.

## Powertools features

Powertools provides three core utilities:

- **[Tracing](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/)** - Decorators and utilities to trace Lambda function handlers, and both synchronous and asynchronous functions
- **[Logging](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/)** - Structured logging made easier, and decorator to enrich structured logging with key Lambda context details
- **[Metrics](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/)** - Custom Metrics created asynchronously via CloudWatch Embedded Metric Format (EMF)

Find the complete project's [documentation here](https://awslabs.github.io/aws-lambda-powertools-python).

### Installing AWS Lambda Powertools for Python

With [pip](https://pip.pypa.io/en/latest/index.html) installed, run:

```bash
pip install aws-lambda-powertools
```

### Powertools Examples

- [Tutorial](https://awslabs.github.io/aws-lambda-powertools-python/latest/tutorial)
- [Serverless Shopping cart](https://github.com/aws-samples/aws-serverless-shopping-cart)
- [Serverless Airline](https://github.com/aws-samples/aws-serverless-airline-booking)
- [Serverless E-commerce platform](https://github.com/aws-samples/aws-serverless-ecommerce-platform)
- [Serverless GraphQL Nanny Booking Api](https://github.com/trey-rosius/babysitter_api)

## Working with this project

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code.
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.  
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

- [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
- [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

### Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

- SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Python 3 installed](https://www.python.org/downloads/)
To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

### Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
cisco-assignment$ pip install -r tests/requirements.txt --user
# unit test
cisco-assignment$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
cisco-assignment$ AWS_SAM_STACK_NAME="cisco-assignment" python -m pytest tests/integration -v
```