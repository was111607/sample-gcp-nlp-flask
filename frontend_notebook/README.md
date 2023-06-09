# Google AI Notebooks (The Frontend)

This README contains instructions on how to use Google [AI Notebooks](https://cloud.google.com/ai-platform-notebooks).


## First time setup
The following steps configures you to be able to run your front end app through the GCP-deployed notebook. These only need to be performed once at the start of the project by 1 member of your team.

1. Head to the [ngrok website](https://dashboard.ngrok.com/) and log in. If required, sign up for an account.
    * Ngrok is used in the front end notebook to expose the web app to the internet, allowing access through an auto-generated URL.
1. Get your authtoken [here](https://dashboard.ngrok.com/get-started/your-authtoken).
1. Run the following command to add your authtoken to GCP. This will be used to automatically configure your front end app to be exposed to the internet when the app is run, making it accessible via URL.

    ```
    printf "[YOUR_AUTHTOKEN]" | gcloud secrets versions add ngrok-authtoken --data-file=-
    ```


## Launch AI Platform Notebooks 

Click on the Navigation Menu and navigate to AI Platform, then to Notebooks.

[![Open AI Notebooks][notebook_img]][notebook_link]

[notebook_img]: https://cdn.qwiklabs.com/fnUEPKKDGG4Xw1nbWJRpVfg02LTmJLOrel2Ny42JQVk%3D
[notebook_link]: https://console.cloud.google.com/ai-platform/notebooks/list

## Creating the Notebook Instance (Done for you already)
**We have done this for you, so feel free to just read through it**

Enable the Notebooks API:

    gcloud services enable notebooks.googleapis.com

On the Notebook instances page, click New Instance. Select the Python 3 version. 
For these demo notebooks, the default configuration should do the trick.

This creates a Jupyter Notebook instance (which, behind the scenes, is actually just running on Google Compute Engine). 


## Open the Notebook Instance
Once the notebook has been provisioned, click 'Open JupyterLab'. A JupyterLab window will open in a new tab. 

[![Open Jupyter Notebooks][jupyter_img]][jupyter_link]

[jupyter_img]: https://cdn.qwiklabs.com/fowDLNZLw1WB1zkF9BBSwzNvjBnZyducp45ui%2FBkXTg%3D
[jupyter_link]: https://console.cloud.google.com/ai-platform/notebooks/list


## Getting the sample code

In the JupyterLab window that opens, click 'Git' -> 'Clone a Repository' in the top menu and clone the private repository that you made of the [sample repo](https://github.com/was111607/sample-gcp-nlp-flask.git) in the general setup before, providing the HTTPS URL of the repository. The quickest way to get past authentication is to generate and use a personal access token in place of your GitHub password.

You should see the repo cloned into the navigator on the left side of the page under the 'sample-gcp-nlp-flask' folder. 


## Demo notebook run

1. If you have not already, first access the deployed backend API by visiting `https://[PROJECT_ID].appspot.com` to view your deployed application. and use the POST endpoint to submit text for analysis.
1. Open Plotly_Data_Visualization_Demo.ipynb from the navigator (under the 'sample-gcp-nlp-flask/frontend_notebook' folders)
1. Run all cells
1. Access the generated URL under the "Web app access" section. If successful, you should be able to see the front end app running locally!

## Next steps

Now you are ready to develop your entire solution! You can use the demo notebook (especially the Jupyter Dash bits) for inspiration to create your own notebook that connects to your back end API and runs your front end as a web app.

You can find example articles to play around with in the /articles directory to get used to the flow of development.
