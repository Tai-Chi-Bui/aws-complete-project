# aws-complete-project
A realistic and complex AWS project that covers all aspects of a professional application.

This project is based on the instructional series provided by Andrew Brown on the ExamPro YouTube channel


## Prerequisite Technologies

[1] Gipod Account:
Gitpod will be used as our Cloud Developer Environment (CDE).
We will be writing code in Gitpod as we integrate cloud services to our application.

Note: we need to install Gitpod Chrome extension to have its Gipod button attached to our Github repository.

[2] Github Codespaces Account:
Github Codespaces will be used as our alternative CDE in case we use up Gitpod's free tier.

[3] AWS Account:
AWS will be our Cloud Service Provider (CSPs).

[4] Momento Account:
Momento offers serverless cache.

To keep the costs down, we will cache DynamoDB requests using Momento Serverless Cache service.

[5] Lucid Charts:
Lucid Charts will be used to build Architecture diagram.

[6] HoneyComb.io:
HoenyComb will be used for distributed tracing.

[7] Rollbar Account:
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

```
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_SESSION_TOKEN=""
export AWS_DEFAULT_REGION="us-east-1"
```

To confirm the config is working, run: ```aws sts get-caller-identity```

Note: after the session token expires, you have to get new one.

If you want, you can tell Gitpod to remember these tokens so the next time we relaunch our workspace, we won't have to enter again (if the session token is still valid):

```
gp env AWS_ACCESS_KEY_ID=""
gp env AWS_SECRET_ACCESS_KEY=""
gp env AWS_DEFAULT_REGION="us-east-1"
```



## Step 3: use ```.gitpod.yml``` for gitpod to automatically install aws the next time you launch Gitpod workspace

```
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```


## Step 4: Setup billing, billing alarm and AWS budget

### 4.1: Enable billing
We need to turn on Billing Alerts to recieve alerts.
Instruction: go to root account -> go to Billing Management Console -> choose 'Receive Billing Alerts' under 'Billing Preferences'.

### 4.2: Create a billing alarm
a) We need to create SNS topic, which will deliver us the message when we are overbilled.

```
aws sns create-topic --name <your topic name>
```
After we run this command, it will return a TopicARN, which will be used in our next command.

We'll subscribe an email address to the SNS topic. So that when there are messages or notifications sent to the specified SNS topic, they will be delivered to the provided email address.

```
aws sns subscribe \
    --topic-arn <TopicARN> \
    --protocol email \
    --notification-endpoint <your email>
```

After the command succeeds, you'll need to check your email and confirm the subscription.


b) After we have our SNS topic, we can create our alarm with CloudWatch.
- First, you need to create a json file; specifically, ```aws/json/alarm_config.json``` in my codebase (remember to input your valid region, account id and sns name)
- Second, you run this command: ```aws cloudwatch put-metric-alarm --cli-input-json file://<absolute path of the json file>```


### 4.3: Create a budget

- First, you need to create json config files; specifically, ```aws/json/budget.json``` and ```aws/json/budget-notifications-with-subscribers.json``` in my codebase.
- Second, you run this command:

```
aws budgets create-budget \
    --account-id <AccountID> \
    --budget file://<absolute path of budget.json> \
    --notifications-with-subscribers file://<absolute path of budget-notifications-with-subscribers.json>
```


## Step 5: Try running backend-flask on local
- ```cd backend-flask```
- Create virtual environment: ```python3 -m venv venv```
- Activate virtual environment: ```source venv/bin/activate``` 
- Install required dependencies: ```pip3 install -r requirements.txt```
- Run the app: ```python3 -m flask run --host=0.0.0.0 --port=4567```
- Append this to the URL to get back a json: ```/api/activities/home```
- When you're done, you can run command ```deactivate``` to deactivate the virtual environment

## Step 6: Add ```Dockerfile``` to ```backend-flask``` and try running it.
- Create a file here: ```backend-flask/Dockerfile```

```
FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
```

- Build Image

```docker build -t  backend-flask ./backend-flask```

- Create and Run Container

```docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask```


## Step 7: Try running ```frontend-react-js``` on local
- ```cd frontend-react-js```
- ```npm install```
- ```npm run start```


## Step 8: Add ```Dockerfile``` to ```frontend-react-js``` and try running it.

- Create a file here: ```frontend-react-js/Dockerfile```

```
FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
```

- Build Image

```docker build -t  frontend-react-js ./frontend-react-js```

- Create and Run Container

```docker run --rm -p 3000:3000 -it -e REACT_APP_BACKEND_URL="https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}" frontend-react-js```