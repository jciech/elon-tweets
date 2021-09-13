import google.auth
from flask import Flask
from google.cloud import secretmanager_v1 as secretmanager


def get_secret_value(client, project, secret, version="latest"):
    name = f"projects/{project}/secrets/{secret}/versions/{version}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")


def load_secrets(project_id, secrets):
    client = secretmanager.SecretManagerServiceClient()
    secret_vars = {}

    for secret in secrets:
        secret_vars[secret] = get_secret_value(client, project_id, secret)

    return secret_vars


class App(Flask):
    def __init__(self, project_id, *args, **kwargs):
        self.project_id = project_id
        super().__init__(*args, **kwargs)


def create_app(project_id):
    if project_id is None:
        _, project_id = google.auth.default()

    app = App(project_id, __name__)

    secret_keys = ["TWITTER_API_BEARER_TOKEN", "TWITTER_API_KEY", "TWITTER_API_SECRET"]
    secrets = load_secrets(
        project_id,
        secret_keys,
    )

    for key, secret in secrets.items():
        app.config[key] = secret

    @app.route("/debug")
    def debugging():
        return "<p> Hello World! </p>"

    return app
