# Python Google Natural Language Cloud sample for Google App Engine Flexible Environment

This sample demonstrates how to use the [Google Cloud Natural Language API](https://cloud.google.com/natural-language) and [Google Cloud Datastore](https://cloud.google.com/datastore/) on [Google App Engine Flexible Environment](https://cloud.google.com/appengine).


## Setup
Head over to the [Google Cloud Platform console](https://console.cloud.google.com/) and make sure you are in the desired project.

Open the Cloud Shell by clicking this button on the top right of the console:

![img.png](../docs/img.png)

Create your App Engine application by typing:

    gcloud app create

You will have to select a region. Choose one that is close to your location.

Next, set an environment variable for your project ID:

    export PROJECT_ID=$(gcloud config get-value core/project)

## Enable APIs and create a service account
Next, we will enable the two GCP APIs needed to run our application. The first is the Natural Language API. The second is Datastore.

    gcloud services enable language.googleapis.com
    gcloud services enable datastore.googleapis.com

Next, we want to create a Service Account to access the Google Cloud APIs when testing locally:

    gcloud iam service-accounts create example \
    --display-name "My Service Account"

Give your newly created Service Account appropriate permissions:

    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member serviceAccount:example@${PROJECT_ID}.iam.gserviceaccount.com \
    --role roles/owner

After creating your Service Account, create a Service Account key:

    gcloud iam service-accounts keys create ~/key.json --iam-account \
    example@${PROJECT_ID}.iam.gserviceaccount.com

Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to where
you just put your Service Account key:

    export GOOGLE_APPLICATION_CREDENTIALS="/home/${USER}/key.json"

**IMPORTANT:** Keep this key.json a secret. You should not commit this file ever.

## Getting the sample code

Run the following command to clone the Github repository:

    git clone https://github.com/Jiaxen/sample-gcp-nlp-flask.git

Change directory to the backend directory:

    cd sample-gcp-nlp-flask/backend_api

## Running "locally"
To run our app "locally" through the cloud shell (that is, not deploying it just yet), we should create a virtual 
environment. This is just an environment where we install the specific dependencies needed by the project and
can run the code.

Install virtualenv:

    pip install virtualenv

Create a virtual environment and install dependencies:

    virtualenv -p python3 env

If you do `ls` now, you will see an `/env` folder created which contains the virtual environment. 

Start your virtual environment (mac and linux):

    source env/bin/activate

Start your virtual environment (windows):

    env\Scripts\activate

Note: If you get an error from windows about not being able to run scripts as it is disabled on this system then run the following command:

    Set-ExecutionPolicy Unrestricted -Scope Process

Install the dependencies:

    pip install -r requirements.txt

Start your application locally using your virtual environment:

    python main.py

Visit the link generated ('Running on http://localhost:8080/') to view your application running locally. Test it out!

Press `Control-C`on your command line when you are finished to stop the application.

    
## Running tests

To run tests, install the requirements for your test
    
    pip install -r requirements-test.txt

Then run pytest by doing  
    
    python -m pytest

## Deactivating your virtual environment
When you are ready to leave your virtual environment:

    deactivate

## Deploying to App Engine

Deploy your application to App Engine with the following command. Please note that this may
take several minutes.

    gcloud app deploy

Visit `https://[YOUR_PROJECT_ID].appspot.com` to view your deployed application.

You can continue to make new versions of the application and deploy them with the above command.