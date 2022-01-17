from flask import Blueprint, render_template, json
from werkzeug.exceptions import HTTPException

web = Blueprint("web", __name__)

from . import book, auth, gift, wish


# AOP
# @web.app_errorhandler(404)
# def not_found(e):
#     return render_template("404.html"), 404

# todo need to customize HTTPException response
@web.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
