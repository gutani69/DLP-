"""Flask application entry point."""


def create_app():
    """Create and configure the Flask application."""
    from flask import Flask

    app = Flask(__name__)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=False)
