# Python Google Natural Language Cloud  sample for Google App Engine Flexible Environment

[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open

This sample demonstrates how to use the [Google Cloud Natural Language API](https://cloud.google.com/natural-language), [Google Cloud Storage](https://cloud.google.com/storage/), and [Google Cloud Datastore](https://cloud.google.com/datastore/) on [Google App Engine Flexible Environment](https://cloud.google.com/appengine).

## Setup

Create a new project with the [Google Cloud Platform console](https://console.cloud.google.com/).
Make a note of your project ID, which may be different than your project name.

Make sure to [Enable Billing](https://pantheon.corp.google.com/billing?debugUI=DEVELOPERS)
for your project.

Download the [Google Cloud SDK](https://cloud.google.com/sdk/docs/) to your
local machine. Alternatively, you could use the [Cloud Shell](https://cloud.google.com/shell/docs/quickstart), which comes with the Google Cloud SDK pre-installed.

Initialize the Google Cloud SDK (skip if using Cloud Shell):

    gcloud init

Create your App Engine application:

    gcloud app create

Set an environment variable for your project ID, replacing `[YOUR_PROJECT_ID]`
with your project ID:

    export PROJECT_ID=[YOUR_PROJECT_ID]
## Activate Cloud Shell

Cloud Shell is a virtual machine that is loaded with development tools. It offers a persistent 5GB home directory and runs on the Google Cloud. Cloud Shell provides command-line access to your Google Cloud resources.

In the Cloud Console, in the top right toolbar, click the Activate Cloud Shell button.

[![Open in Cloud Shell][shell_img]][shell_link]


[shell_link]: https://console.cloud.google.com/cloudshell/
[shell_img]: https://cdn.qwiklabs.com/vdY5e%2Fan9ZGXw5a%2FZMb1agpXhRGozsOadHURcR8thAQ%3D


## Launch AI Platform Notebooks 

Click on the Navigation Menu and navigate to AI Platform, then to Notebooks.

[![Open AI Notebooks][notebook_img]][notebook_link]

[notebook_img]: https://cdn.qwiklabs.com/fnUEPKKDGG4Xw1nbWJRpVfg02LTmJLOrel2Ny42JQVk%3D
[notebook_link]: https://console.cloud.google.com/ai-platform/notebooks/list

On the Notebook instances page, click New Instance. Select the Python 3 version

Click Open JupyterLab. A JupyterLab window will open in a new tab.

[![Open Jupyter Notebooks][jupyter_img]][jupyter_link]

[jupyter_img]: https://cdn.qwiklabs.com/fowDLNZLw1WB1zkF9BBSwzNvjBnZyducp45ui%2FBkXTg%3D
[jupyter_link]: https://console.cloud.google.com/ai-platform/notebooks/list


## Getting the sample code

In Cloud Shell Run the following command to clone the Github repository:

    git clone https://github.com/Jiaxen/sample-gcp-nlp-flask.git

Change directory to the sample code location:

    cd sample-gcp-nlp-flask/language_api


## Authentication

Enable the API:

    gcloud services enable language.googleapis.com

Create a Service Account to access the Google Cloud APIs when testing locally:

    gcloud iam service-accounts create qwiklab \
    --display-name "My GEE Service Account"

Give your newly created Service Account appropriate permissions:

    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member serviceAccount:qwiklab@${PROJECT_ID}.iam.gserviceaccount.com \
    --role roles/owner

After creating your Service Account, create a Service Account key:

    gcloud iam service-accounts keys create ~/key.json \
    --iam-account qwiklab@${PROJECT_ID}.iam.gserviceaccount.com

Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to where
you just put your Service Account key:

    export GOOGLE_APPLICATION_CREDENTIALS="/home/${USER}/key.json
    --iam-account gee-module2@${PROJECT_ID}.iam.gserviceaccount.com

This command generates a service account key stored in a JSON file named key.json in your home directory.

Using the absolute path of the generated key, set an environment variable for your service account key:

    export GOOGLE_APPLICATION_CREDENTIALS="/home/${USER}/key.json"
    
    ## Testing the Application Locally

Create a virtual environment and install dependencies:

    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt

## Create an App Engine App

Next, create an Aoo Engine instance by using:

    gcloud app create
    
A prompt will display a list of regions. Select a Region that supports App Engine Flexible for Python then press Enter.

## Create a Storage Bucket

First, set the environment variable CLOUD_STORAGE_BUCKET equal to the name of your PROJECT_ID. (It is generally recommended to name your bucket the same as your PROJECT_ID for convenience purposes).

    export CLOUD_STORAGE_BUCKET=${PROJECT_ID}
       
Now run the following command to create a bucket with the same name as your PROJECT_ID.

    gsutil mb gs://${PROJECT_ID}
## Running the Application

Execute the following command to start your application:

    python main.py
    
Once the application starts, click on the Web Preview icon in the Cloud Shell toolbar and choose "Preview on port 8080."

## Example App Run

The app is hosted using flask. An example solution could involve inputing text and outputing the syntax analysis with either 'positive' or 'negative' outcome.
