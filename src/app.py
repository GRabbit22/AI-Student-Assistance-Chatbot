from flask import Flask

def create_app():
    app = Flask(__name__)

    from routes.chatbot_routes import chatbot_bp
    app.register_blueprint(chatbot_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
