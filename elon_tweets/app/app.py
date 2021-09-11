import logging
import google.auth
from flask import Flask
from google.cloud import secretmanager_v1 as secretmanager


def get_secret_value(client, project, secret, version='latest'):
    name = f'projects/{project}/secrets/{secret}/versions/{version}'
    response = client.access_secret_version(request={'name': name})
    return response.payload.data.decode('UTF-8')


def load_secrets(project_id, secrets):
    client = secretmanager.SecretManagerServiceClient()
    secret_vars = {}

    for secret in secrets:
        secret_vars[secret] = get_secret_value(client, project_id, secret)

    return secret_vars



def create_app():
    app = Flask(__name__)
    _ ,project_id = google.auth.default()

    logging.info(f'Running app for project {project_id}.')


    secret_keys = [
    "TWITTER_API_BEARER_TOKEN",
    "TWITTER_API_KEY",
    "TWITTER_API_SECRET"
    ]
    secrets = load_secrets(
        project_id,
        secret_keys,
    )

    for key, secret in secrets.items():
        app.config[key] = secret

    logging.info('Secrets loaded.')

    return app