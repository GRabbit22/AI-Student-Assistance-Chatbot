from flask import Blueprint, jsonify

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Chatbot backend is running"})
