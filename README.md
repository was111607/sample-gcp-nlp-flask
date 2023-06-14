# Sample GCP Flask App using Cloud Natural Language API

Welcome! This is the stub project for building your Natural Language Analysis Platform using GCP.

## Prerequisites
1. Ability in or desire to learn Python!  
1.1 Python version: 3.10
2. Ability in or desire to learn Google Cloud Platform!

## Team Setup
1) One person in your team should create a private GitHub clone of this repository. See [here](README-private-clone.md) for instructions to make a private clone of this repository.
2) The same person should add your team members' GitHub accounts into the private GitHub clone that you have made.
3) This repo can then be used by your team to do the development.

## The Goal
The goal is to set up a platform to analyse text data using GCP Services.

## The Architecture
![The architecture](docs/architecture.png)

### The Back End
The back end is a REST endpoint service using the Flask framework in Python. This will be deployed in GCP App Engine.
This component will talk to GCP's [Natural Language API](https://cloud.google.com/natural-language) service to analyse 
our text, and use GCP Datastore as a NoSQL database for storage. 

The code for the backend is in the **/backend_api** folder.

### The Front End
The front end is a Jupyter notebook which interacts with the backend REST service to obtain the analysed data, and then
creates visualisations. 

The code for the frontend is in the **/frontend_notebook** folder, as well as some coded examples of visualisation.
 
## Get started
1. Perform the back end [configuration steps](backend_api/README.md)
1. Perform the front end [configuration steps](frontend_notebook/README.md) 

If you'd like run your code locally first (before publishing to GCP), you can have a look into [Local setup with VS Code & DevContainer](README-vscode.md).

If you are interested, you can also give Github Codespaces a try - please have a look into [Remote development with Github Codespaces](README-github-codespace.md).
