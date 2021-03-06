from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from werkzeug.security import generate_password_hash
from models.logs import LoggerObject
# from application import db

logger = LoggerObject()

server_log = Blueprint('server_log', __name__)

@server_log.route('/getlog', methods=['GET'])
def get_log_json():
    logger_for_json = LoggerObject()
    logger_for_json.logrequest(request, jsonify({'return':'success'}))
    return jsonify(logger_for_json.getAllLogs())

@server_log.route('/deletelogs', methods=['GET'])
def delete_log():
    logger.deleteAllLogs()
    return "cleared all logs"
