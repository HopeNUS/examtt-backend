import os
from flask import Flask, request, json, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

project_dir = os.path.dirname(os.path.abspath(__file__))
dbfile = os.path.join(project_dir, "..", "..", "database", "examtt.db")
DATABASE_URI = {
    "key": "SQLALCHEMY_DATABASE_URI",
    "filepath": "sqlite:///{}".format(dbfile)
}
app = Flask(__name__)
CORS(app, resources={"/api/examtt/*": {"origins": "*"}})
app.config[DATABASE_URI['key']] = DATABASE_URI['filepath']
db = SQLAlchemy(app)


from ..controller.controller import Controller
controller = Controller(db)


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add(
        'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add(
        'Access-Control-Allow-Credentials', 'true')
    return response


@app.route("/api/examtt", methods=['GET'])
def home():
    return controller.help()


@app.route(
    "/api/examtt/parse", methods=['POST'], defaults={'parser_choice': None})
@app.route("/api/examtt/parse/<parser_choice>", methods=['POST'])
def parse_examtt(parser_choice):
    jsonObj = request.get_json()
    examtt_str = jsonObj['examtt']
    lifegroup = jsonObj['lifegroup']
    return json.jsonify(
        controller.parse_and_add_examtt_obj(
            examtt_str, lifegroup, parser_choice))


@app.route("/api/examtt/slot", methods=['GET'])
def get_examtt_by_slot():
    day = request.args.get('day', default=None, type=str)
    time = request.args.get('time', default=None, type=str)
    venue = request.args.get('venue', default=None, type=str)
    return json.jsonify(controller.get_examtt_by_slot(day, time, venue))


@app.route("/api/examtt/student/<student_name>", methods=['GET'])
def get_examtt_by_student(student_name):
    return json.jsonify(controller.get_examtt_by_student(student_name))


@app.route("/api/examtt/csv", methods=['GET'])
def get_examtt_as_csv():
    csv = controller.get_examtt_as_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=examtt.csv"})


@app.route("/api/examtt/delete/student/<student_name>", methods=['GET'])
def delete_examtt_by_student_name(student_name):
    return controller.delete_examtt_by_student_name(student_name)


@app.route("/api/examtt/lgs", methods=['GET'])
def get_all_lg():
    return json.jsonify(controller.get_all_lg())


@app.errorhandler(404)
def page_not_found(err):
    return controller.page_not_found()


if __name__ == '__main__':
    app.run()
