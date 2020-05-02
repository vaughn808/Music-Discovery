from flask import Flask, render_template, url_for, request, make_response, jsonify
from variable import billboard_list
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", message="Hello Flask!  I am on the Home page")


@app.route("/playlist")
def playlist():
    billboard_sort = sorted(billboard_list)
    return render_template("playlist.html", title="Playlist", message="Hello Flask!  I am on the learning page", len = len(billboard_list), billboards=billboard_sort, current_dte=datetime.today().strftime('%Y-%m-%d'))


@app.route("/playlist/get-list", methods=["POST"])
def create_entry():

    req = request.get_json()

    print(req)

    #res = make_response(jsonify({"message": "OK"}), 200)

    return req


@app.route("/resources")
def resources():
    return render_template("resources.html", title="Resources", message="Hello Flask!  I am on the resources page")


@app.errorhandler(404)
def not_found():
    """Page not found."""
    return render_template("error.html", title="Error", error_type="Page Not Found"), 404


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return render_template("error.html", title="Error", error_type="Bad Request"), 400


@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return render_template("error.html", title="Error", error_type="Server Error"), 500


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)

