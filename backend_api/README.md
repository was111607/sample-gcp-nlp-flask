# Flask + Google NLP API + Datastore (The Backend)

This sample demonstrates how to use the [Google Cloud Natural Language API](https://cloud.google.com/natural-language) and [Google Cloud Datastore](https://cloud.google.com/datastore/) inside a Flask application, all running on [Google App Engine Flexible Environment](https://cloud.google.com/appengine).

It will create a simple Python flask app that serves some REST endpoints. The application will communicate with GCP's 
NLP API for analysis and Datastore for a NoSQL database. The endpoints created will later be used by the Notebook 
frontend.

Please note: when ran locally, the backend API uses Python 3.9 but when deployed to GCP, it uses Python 3.10.

You can develop your application locally using the Google Cloud CLI (gcloud) or through the web browser using the Cloud Shell.

Although the Cloud Shell is pre-installed with gcloud (and other libraries), you are STRONGLY recommended to install and use gcloud locally to undertake development.

Our suggestion is to follow the steps to use gcloud as given below and if, in the end, you feel the application is not set up as outlined, you can use the [Cloud Shell](#using-the-cloud-shell) to make sure.

## Using gcloud
You are required to set up the Cloud SDK on your local machine to use gcloud.

1. Download the Cloud SDK [here](https://cloud.google.com/sdk/docs/downloads-interactive). ONLY follow the steps to download and install.
1. Log in using gcloud:

    ```
    gcloud auth login
    ```

1. Link to the correct project (using the wrong project might accidently bill you instead). [Extra documentation](https://cloud.google.com/sdk/docs/initializing)

    ```
    gcloud init
    ```

To ensure that you are using the latest versions of all installed components, update gcloud regularly:

```
gcloud components update
```

If you get an error on Windows similar to this: `running scripts is disabled on this system` then run the following command:

```
Set-ExecutionPolicy Unrestricted -Scope Process
```

## First Time Setup


## App Engine and API Setup (done for you already)
**Note: We have done this step for you, so feel free to just read through it.** 

Create your App Engine application:

```
gcloud app create
```

You will have to select a region. Choose one that is close to your location.

Next, we will enable the two GCP APIs needed to run our application. The first is the Natural Language API. The second is Datastore.

You can do all of this directly in the Cloud Shell or you setup Cloud SDK on your local machine as well (see below on how to do that)

```
gcloud services enable language.googleapis.com
gcloud services enable datastore.googleapis.com
```

**Okay, back to your part!**

After you have successfully set up gcloud, you **MUST** obtain a Service Account key as outlined in the following section.

## Creating a Service Account key

Running the back end both locally and when deployed requires using App Engine service account assigned to your GCP project. You need to get its account key:

1. Get the project ID and save it into an environment variable:
    1. macOS/UNIX:

    ```
    export PROJECT_ID=$(gcloud config get-value core/project)
    ```

    2. Windows:

    ```
    set PROJECT_ID=$(gcloud config get-value core/project)
    ```

1. If you are not already, make sure that you are in the "backend_api" folder

    ```
    cd backend_api
    ```

1. Get the App Engine service account key and save into key.json. **Keep key.json a secret. You should never commit this file ever**:

    ```
    gcloud iam service-accounts keys create key.json --iam-account \
    ${PROJECT_ID}@appspot.gserviceaccount.com
    ```

## Running the backend
To just run your app (that is, not deploying it just yet), you are recommended to create a virtual enviroment. This is just an environment where we install the specific dependencies needed by the project and can run the code. You can, of course, run the app without a virtual environment but it is usually easier to use one during the course of development as it allows you to effectively manage and isolate dependencies for different projects.

If you wish to use a virtual environment, you are required to create it just once: before you run the app for the first time, after which, you have to simply activate/deactivate your virtual environment. Not to worry, the following steps will walk you through it!

### Creating a Virtual Environment:

### For macOS/Unix systems

Install virtualenv:

    pip install virtualenv

Create a virtual environment and install dependencies:

    virtualenv -p python3 env

If you do `ls` now, you will see an `/env` folder created which contains the virtual environment. 

Start your virtual environment:

    source env/bin/activate

Install the dependencies:

    pip install -r requirements.txt

Start your application via cloud shell using your virtual environment:

    python main.py


### For Windows

Install virtualenv:

    pip install virtualenv

Create a virtual environment and install dependencies:

    python -m virtualenv .

If you do `ls` now, you will see an `/Scripts` folder created which contains the virtual environment. 

Start your virtual environment:

     .\Scripts\activate

Install the dependencies:

    pip install -r requirements.txt

Start your application via cloud shell using your virtual environment:

    python main.py

Visit the link generated ('Running on http://127.0.0.1:8080/') to view your application running locally. Test it out!

You should be presented with a [Swagger UI](https://swagger.io/tools/swagger-ui/) page. This page will allow you to interact with the backend REST API easily. In the examples we have given you can make a post request where we apply sentiment analysis on some given text and then save it to [GCP Datastore](https://cloud.google.com/datastore/docs/quickstart)
Try sending the sentence "Today is a great day for coding!" in the post request. Then execute the get request.

Press `Control-C` on your command line when you are finished to stop the application.

The next time you want to run your 
 
### Deactivating your virtual environment
When you are ready to leave your virtual environment:

    deactivate

Note: activate your virtual environment when you wish to resume development and deactivate it when you wish to stop development for the time being.

## Deploying to App Engine

Deploy your application to App Engine with the following command. Please note that this may
take several minutes.

    gcloud app deploy

Visit `https://[YOUR_PROJECT_ID].appspot.com` to view your deployed application.

You can continue to make new versions of the application and deploy them with the above command. If you are not using the Cloud Shell, head to [Get Started Coding](#get-started-coding)!

## Using the Cloud Shell
Head over to the [Google Cloud Platform console](https://console.cloud.google.com/) and make sure you are in the desired project.

Open the Cloud Shell by clicking this button on the top right of the console:

![img.png](../docs/img.png)

Here, you can enter commands to interact with GCP.

## App Engine and API Setup
This step has been done for you already (outlined earlier [here](#app-engine-and-api-setup-done-for-you-already)).

## Cloning the code into Cloud Shell

If you use a private repository, you will need to [log in to GitHub](../README-private-clone.md) first. \
Run the following commands to clone the GitHub repository to your cloud shell (replace it with your clone/fork url):

    gh auth login (follow the steps to connect to your GitHub)
    git clone https://github.com/was111607/sample-gcp-nlp-flask.git (replace with your forked version)

Change directory to the backend directory:

    cd sample-gcp-nlp-flask/backend_api

## Creating a Service Account key (very important!)
Before you proceed any further, create a Service Account key as explained [here](#creating-a-service-account-key). Skip this step if you have already created one for your project - **YOU ONLY NEED TO DO THIS ONCE!**.

## Running the backend using the Cloud Shell

To run your app through the cloud shell, create a virtual environment. Follow the instructions outlined above [here](#creating-a-virtual-environment) and [here](#deactivating-your-virtual-environment).

## Deploying app on App Engine with Cloud Shell

Once again, follow the steps outlined earlier [here](#deploying-to-app-engine) to deploy your application.


## First Time Setup
To check that the back end has been deployed correctly, perform the following steps:
1. Access the deployed API by visiting `https://[YOUR_PROJECT_ID].appspot.com`
1. Use the POST endpoint to submit text for analysis.
1. Use the GET endpoint to check that your submitted text has been analysed.


## Next Steps
If this is your first time setting up the project, you can now move onto performing the front end [configuration steps](../frontend_notebook/README.md).

When you have fully set up the project, it's your time to develop your entire solution. Take a look at the main.py file to see how the back end works and build on this for your solution, serving your front end web app!

For those curious about Data Science, jupyter notebooks (.ipynb or iPython Notebook files) are an essential part of experimentation. You can test out different AI/ML models on different data much quicker using them, compared to using regular .py files. Feel free to experiment with different methods of topic analysis in TopicAnalyser.ipynb, or try using different data. 
When you're finished experimenting, consider making your experimented code available in TopicAnalyser.py, and make TopicAnalyser.py part of your API in main.py.
(NOTE: this is only one optional path you can take with your project)
