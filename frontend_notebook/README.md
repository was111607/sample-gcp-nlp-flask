# Google AI Notebooks (The Frontend)
This README demonstrates how to setup a sample front end application based in a notebook hosted on GCP's [Vertex AI Workbench Platform](https://cloud.google.com/vertex-ai-workbench).

The application is a Plotly Dash web app that is configured to be run from a Jupyter Notebook. It retrieves data from the [back end](../frontend_notebook/README.md) API and displays it along with other visualisations on a web page accessible through URL.


## First Time Setup
The following steps configures you to be able to run your front end app through the GCP-deployed notebook. These only need to be performed once at the start of the project by 1 member of your team.


### Getting the Authtoken For Accessing the Web App
1. Head to the [ngrok website](https://dashboard.ngrok.com/) and log in. If required, sign up for an account.
    * Ngrok is used in the front end notebook to expose the web app to the internet, allowing access through an auto-generated URL.
1. Get your authtoken [here](https://dashboard.ngrok.com/get-started/your-authtoken).
1. Run the following command to add your authtoken to GCP. This will be used to automatically configure your front end app to be exposed to the internet when the app is run, making it accessible via URL.

    ```
    printf "[YOUR_AUTHTOKEN]" | gcloud secrets versions add ngrok-authtoken --data-file=-
    ```


### Opening the Notebook Instance
1. Search for "Vertex AI Workbench" in GCP (or click the image below), you should arrive on a page that looks something like this:
    [![vertex-ai-view][vertex_img]][jupyter_link]

    [vertex_img]: ../docs/vertex-ai-view.png
    [jupyter_link]: https://console.cloud.google.com/vertex-ai/workbench/list


1. **Only perform when you have been given the go ahead**. If the notebook is currently stopped, click 'Open JupyterLab'. The notebook instance will be created and a JupyterLab window will open in a new tab.

    ![Open Jupyter Notebooks][jupyter_img]

    [jupyter_img]: ../docs/new-jupyterlab-view.png


### Getting the Sample Code
After performing the steps listed in either of the following options, you should see the repo cloned into the navigator on the left side of the page under the 'sample-gcp-nlp-flask' folder. 

#### Option 1: Terminal
1. In the JupyterLab launcher, click 'Terminal'

1. Clone the HTTPS URI of the private repository that you made of the [sample repo](https://github.com/was111607/sample-gcp-nlp-flask.git) in the general setup before using the URI:
    ```
    git clone <your-repository-uri>
    ```

#### Option 2: JupyterLab UI
1. In the top navigation bar of the JupyterLab window, click 'Git' -> 'Clone a Repository' 

1. Enter the URI of the private repository that you made of the [sample repo](https://github.com/was111607/sample-gcp-nlp-flask.git) in the general setup before.
    1. The quickest way to get past authentication is to generate and use a personal access token in place of your GitHub password.


### Demo Notebook Run
1. If you have not already, follow the back end API setup instructions. Access the deployed API by visiting `https://[YOUR_PROJECT_ID].appspot.com` and use the POST endpoint to submit text for analysis.

1. Open Plotly_Data_Visualization_Demo.ipynb from the navigator (under the 'sample-gcp-nlp-flask/frontend_notebook' folders)

1. Run all cells

1. Access the generated URL under the "Web app access" section. If successful, you should be able to see the front end app running locally!


## Next Steps
Now you are ready to develop your entire solution! You can use the demo notebook (especially the Jupyter Dash bits) for inspiration to create your own notebook that connects to your back end API and runs your front end as a web app.

You can find example articles to play around with in the /articles directory to get used to the flow of development.


### Development Flow
As your code inside JupyterLab is connected to your repository, all usual Git actions and operations are applicable to it using the JupyterLab terminal. For example:

* Creating new branches
* Working on different branches
* Committing code changes
* Fetching code changes to update code in JupyterLab (i.e. new commits from local development)
