# Python Google Natural Language Cloud  sample for Google App Engine Flexible Environment

[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open

This sample demonstrates how to use the [Google Cloud Natural Language API](https://cloud.google.com/natural-language) and [Google Cloud Datastore](https://cloud.google.com/datastore/) on [Google App Engine Flexible Environment](https://cloud.google.com/appengine).

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

You can now try to run the notebooks yourself. If you run into any errors, try restarting the notebook kernel, and also ensure that you have the Natural Language API enabled (through shell): 

    gcloud services enable language.googleapis.com
