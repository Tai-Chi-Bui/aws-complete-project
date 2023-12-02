# aws-complete-project
A realistic and complex AWS project that covers all aspects of a professional application.


## Prerequisite Technologies

[1] Github Account
Github will be used to store our application code.

[2] Gipod Account
Gitpod will be used as our Cloud Developer Environment (CDE).
We will be writing code in Gitpod as we integrate cloud services to our application.

Note: we need to install Gitpod Chrome extension to have its Gipod button attached to our Github repository.

[3] Github Codespaces Account
Github Codespaces will be used as our alternative CDE in case we use up Gitpod's free tier.

[4] AWS Account
AWS will be our Cloud Service Provider (CSPs).

[5] Momento Account
Momento offers serverless cache.

To keep the costs down, we will cache DynamoDB requests using Momento Serverless Cache service.

[6] Lucid Charts
Lucid Charts will be used to build Architecture diagram.

[7] HoneyComb.io
HoenyComb will be used for distributed tracing.

[8] Rollbar Account
Rollbar is a bug tracking tool for production application. It will help us capture uncaught errors, application crashes and slow response.


## Architecture Diagram

### Conceptual Diagram

![conceptual](https://github.com/Tai-Chi-Bui/aws-complete-project/assets/75408677/1ddb0dc7-f695-44bb-8603-3d26c68f6873)

### Logical Diagram

![logical](https://github.com/Tai-Chi-Bui/aws-complete-project/assets/75408677/9ff29aa7-c7cc-40a3-b2b3-26e666321ca0)



## Step 1: Create user in IAM Identity Center

After you create a user and grant it permissions, you can use its credentials to access AWS resources from your IDE.

## Step 2: Install AWS CLI and add user's credentials to its configuration

The command to config credentials would look like this:
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_SESSION_TOKEN=""

