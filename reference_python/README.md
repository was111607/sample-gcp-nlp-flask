# Google Natural Language on a Google AI Notebook

This sample demonstrates how to use the [Google Cloud Natural Language API](https://cloud.google.com/natural-language) through Google [AI Notebooks](https://cloud.google.com/ai-platform-notebooks).
## Set up

If you have already set up the flask app in the language_api, then no further set up is required. 
Otherwise, do the below instructions to enable billing, enable APIs, and set up a service account.

Make sure to [Enable Billing](https://pantheon.corp.google.com/billing?debugUI=DEVELOPERS)
for your project.


Open the Cloud Shell (top right of console, or click the following button)

[![Cloud Shell][shell_img]][shell_link]
         
[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/home/dashboard?cloudshell=true

Set an environment variable for your project ID:

    export PROJECT_ID=$(gcloud config get-value core/project)

Enable the Cloud natural language API: (You can also do these through Navigation Menu -> APIs & Services)

    gcloud services enable language.googleapis.com

Create a Service Account to access the Google Cloud APIs when testing locally:

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


## Launch AI Platform Notebooks 

Click on the Navigation Menu and navigate to AI Platform, then to Notebooks.

[![Open AI Notebooks][notebook_img]][notebook_link]

[notebook_img]: https://cdn.qwiklabs.com/fnUEPKKDGG4Xw1nbWJRpVfg02LTmJLOrel2Ny42JQVk%3D
[notebook_link]: https://console.cloud.google.com/ai-platform/notebooks/list

Enable the Notebooks API if it asks you to.

On the Notebook instances page, click New Instance. Select the Python 3 version. 
For these demo notebooks, the default configuration should do the trick.

Once the notebook has been provisioned (click refresh to update), click 'Open JupyterLab'. A JupyterLab window will open in a new tab. 

[![Open Jupyter Notebooks][jupyter_img]][jupyter_link]

[jupyter_img]: https://cdn.qwiklabs.com/fowDLNZLw1WB1zkF9BBSwzNvjBnZyducp45ui%2FBkXTg%3D
[jupyter_link]: https://console.cloud.google.com/ai-platform/notebooks/list


## Getting the sample code

In the JupyterLab window that opens, click 'Git' in the top menu and clone the repository:

    https://github.com/Jiaxen/sample-gcp-nlp-flask.git

You should see the repo cloned into the navigator on the left side of the page. Navigate into the sample notebooks:

    sample-gcp-nlp-flask/reference_python
    
You can now read through the notebooks and the sample outputs.
You can also try to run the notebooks yourself. 

If you run into any errors, ensure that you have the Natural Language API enabled (shell command below): 

    gcloud services enable language.googleapis.com
    
And then restart the notebook kernel ('Kernel' option in the JupyterLab top menu).

Find more documentation on the API calls used here at [https://cloud.google.com/natural-language/docs/basics].
