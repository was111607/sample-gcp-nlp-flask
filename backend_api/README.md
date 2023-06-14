# Flask + Google NLP API + Datastore (The Backend)
This README demonstrates how to setup a sample back end application that uses the [Google Cloud Natural Language API](https://cloud.google.com/natural-language) and [Google Cloud Datastore](https://cloud.google.com/datastore/), which can be deployed to run on [Google App Engine Flexible Environment](https://cloud.google.com/appengine).

The application is a Python flask API that serves some REST endpoints. The application communicates with GCP's 
NLP API for analysis and Datastore for a NoSQL database. The endpoints created will be accessed by the front end web app running in a Notebook.

You can develop your application locally using the Google Cloud CLI (gcloud).


## First Time Setup
The steps outlined in this section only need to be performed once when setting up the project for the first time. Every team member should perform these steps.


### Using gcloud
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


After you have successfully set up gcloud, you **MUST** obtain a Service Account key as outlined in the following section.

### Creating a Service Account key
Running the back end (either locally or when deployed) requires using App Engine service account assigned to your GCP project. You need to get and store the account key:

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


### Local Development Environment
You should first test new and changed code locally to verify correct functionality before deployment onto GCP, which hosts the 'live', final version of your project. To facilitate this, you are strongly recommended to create a virtual enviroment. This is an environment where we install and manage the specific dependencies needed by the project to run the code, and is isolated away from other environments running projects to prevent conflicts between different dependencies.

After creating the virtual environment, you must 'activate' it to access it. If you need to stop development and leave it e.g. to work on another project, you must 'deactivate' it.


#### Creating a Virtual Environment
There are many different libraries that help create a virtual environment for you. The following steps describe the installation and setup of an environment using the 'Anaconda' library, although you are free to choose whichever environment suits you.

1. Follow Anaconda installation steps for your system [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages)

1. Create the virtual environment, replacing the placeholders with a name of your choice:
    ```
    conda create -n <project-env> python=3.10.10
    ```

1. Activate the virtual environment:
    ```
    conda activate <project-env>
    ```

1. If you haven't already, go to the backend_api folder:
    ```
    cd backend_api
    ```

1. Install project dependencies:
    ```
    pip install -r requirements.txt
    ```

#### Running the Back End Locally

1. Activate the virtual environment:
    ```
    conda activate <project-env>
    ```

1. If you haven't already, go to the backend_api folder:
    ```
    cd backend_api
    ```

1. Start application:
    ```
    python main.py
    ```

1. Visit the link generated ('Running on http://127.0.0.1:8080/') to view your application running locally. Test it out!

You should be presented with a [Swagger UI](https://swagger.io/tools/swagger-ui/) page. This page will allow you to interact with the backend REST API easily. In the examples we have given you can make a post request where we apply sentiment analysis on some given text and then save it to [GCP Datastore](https://cloud.google.com/datastore/docs/quickstart)

Try sending a sentence e.g. "Today is a great day for coding!" in the POST request. Then execute the GET request to view the text analysis results. If you get results, you have now successfully configured the local development environment.

Press `Control-C` on your command line when you are finished to stop the application.

Now it's time to test if you can deploy the back end to Google App Engine. Familiarise yourself with these [steps](#deploying-to-app-engine) and nominate 1 team member to make the first-time deployment and test.


#### Deactivating Your Virtual Environment
If you need to leave your virtual environment:
```
conda deactivate
```


## Deploying to App Engine
Google App Engine is used to host a 'live' version of your back end, accessible publicly through a URL. Unlike your local development environment, which through exploring solutions and testing you will run into bugs and other issues, code that is deployed to App Engine should be bug-free and represent a complete state of your code.

Deploy your application to App Engine with the following command. Please note that this may take several minutes.
```
gcloud app deploy
```

Visit `https://[YOUR_PROJECT_ID].appspot.com` to view your deployed application.

You can continue to make new versions of the application and deploy them with the above command.


### Final Checks
To check that the back end has been deployed correctly, perform the following steps:
1. Access the deployed API by visiting `https://[YOUR_PROJECT_ID].appspot.com`
1. Use the POST endpoint to submit text for analysis.
1. Use the GET endpoint to check that your submitted text has been analysed.

When the above steps have passed, you have now fully completed configuring the back end!

If this is your first time setting up the whole project, please move onto performing the front end [configuration steps](../frontend_notebook/README.md).

When you have fully set up the project, it's time to start developing your entire solution. Take a look at the main.py file to see how the back end functions how it serves your front end web app. Build on this for your solution.

Remember to develop and test everything locally first before making deployments to App Engine!

Also have a look at TopicAnalyser.py as an example of functionality that can become part of the back end API, feel free to experiment and play around with it to get used to the flow of development.

#### Using Jupyter Notebooks
For those curious about Data Science, Jupyter notebooks (.ipynb or iPython Notebook files) are an essential part of experimentation. You can perform tests e.g.different AI/ML models on different data, much quicker using them compared to using regular .py files.

So consider experimenting using notebooks and moving code into the .py files that form your back end. You can create notebooks in the [front end](../frontend_notebook/README.md) environment setup.
