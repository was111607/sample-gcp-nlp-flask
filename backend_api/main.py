from datetime import datetime
import logging
from flask import Flask
from flask_restx import Resource, Api
from google.cloud import datastore
from google.cloud import language_v1 as language
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

"""
This Flask app shows some examples of the types of requests you could build.
There is currently a GET request that will return all the data in GCP Datastore
There is also a POST request that will analyse some given text then store the text and its sentiment in GCP Datastore


Some ideas of things to build:
- GET Request that returns a single entity based on its ID
- POST Request that will take a list of text items and give it a sentiment then store it in GCP Datastore
- DELETE Request to delete an entity from Datastore based on its ID

We are using Flask: https://flask.palletsprojects.com/en/2.0.x/
Flask RESTX is an extension of Flask that allows us to document the API with Swagger: https://flask-restx.readthedocs.io/en/latest/
"""

app = Flask(__name__)
api = Api(app)

parser = api.parser()
parser.add_argument("text", type=str, help="Text", location="form")


@api.route("/api/text")
class Text(Resource):
    def get(self):
        # Create a Cloud Datastore client.
        datastore_client = datastore.Client()
        query = datastore_client.query(kind="Sentences")
        text_entities = list(query.fetch())

        # Parse the data into a dictionary format
        result = {}
        for text_entity in text_entities:
            result[str(text_entity.id)] = {
                "text": str(text_entity["text"]),
                "timestamp": str(text_entity["timestamp"]),
                "sentiment": str(text_entity["sentiment"]),
            }

        return result

    @api.expect(parser)
    def post(self):
        datastore_client = datastore.Client()

        args = parser.parse_args()
        text = args["text"]

        sentiment = analyze_text_sentiment(text)[0].get("sentiment score")

        # Assign a label based on the score
        overall_sentiment = "unknown"
        if sentiment > 0:
            overall_sentiment = "positive"
        if sentiment < 0:
            overall_sentiment = "negative"
        if sentiment == 0:
            overall_sentiment = "neutral"

        current_datetime = datetime.now()

        # The kind for the new entity. This is so all 'Sentences' can be queried.
        kind = "Sentences"

        # If a key is not specified then datastore will automatically generate one
        # key = datastore_client.key(kind, 'sample_task')
        key = datastore_client.key(kind)

        # Construct the new entity using the key. Set dictionary values for entity
        entity = datastore.Entity(key)
        entity["text"] = text
        entity["timestamp"] = current_datetime
        entity["sentiment"] = overall_sentiment

        # Save the new entity to Datastore.
        datastore_client.put(entity)

        result = {}
        result[str(entity.key.id)] = {
            "text": text,
            "timestamp": str(current_datetime),
            "sentiment": overall_sentiment,
        }
        return result


@app.errorhandler(500)
def server_error(e):
    logging.exception("An error occurred during a request.")
    return (
        """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(
            e
        ),
        500,
    )


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")

    # Get sentiment for all sentences in the document
    sentence_sentiment = []
    for sentence in response.sentences:
        item = {}
        item["text"] = sentence.text.content
        item["sentiment score"] = sentence.sentiment.score
        item["sentiment magnitude"] = sentence.sentiment.magnitude
        sentence_sentiment.append(item)

    return sentence_sentiment


if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
