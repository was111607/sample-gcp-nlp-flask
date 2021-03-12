import uuid

import backoff
from google.api_core.exceptions import GatewayTimeout
import pytest
import requests
import six

import main



@pytest.fixture
def app():
    main.app.testing = True
    client = main.app.test_client()
    return client


def test_index(app):
    r = app.get('/')
    assert r.status_code == 200


def test_upload_text(app):

    @backoff.on_exception(backoff.expo, GatewayTimeout, max_time=120)
    def run_sample():
        return app.post(
            '/upload',
            data={
                'text': 'Test statement'
            }
        )

    r = run_sample()

    assert r.status_code == 302
