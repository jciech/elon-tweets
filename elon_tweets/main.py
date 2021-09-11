from app.app import create_app
import os, sys

sys.path.append(os.path.dirname(__file__))


app = create_app(None)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
