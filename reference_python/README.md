# Google Natural Language on a AI Notebook

This sample demonstrates how to use the [Google Cloud Natural Language API](https://cloud.google.com/natural-language) through Google [AI Notebooks](https://cloud.google.com/ai-platform-notebooks).

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