from flask import request, jsonify


def defineRoutes(app, studentLogicController, warriorLogicController):
    @app.route("/")
    def home():
        return "Hello World!"

    @app.route("/exams/<date>/<month>", methods=["GET"])
    def getStudentExamTimetable(date, month):
        return warriorLogicController\
            .getExamTimeTable(date, month)\
            .serialise()

    @app.route(
        "/prayers/<date>/<month>",
        methods=["GET"],
        defaults={'meetingPoint': None, 'hour': None, 'minute': None})
    @app.route(
        "/prayers/<date>/<month>/<meetingPoint>",
        methods=["GET"], defaults={'hour': None, 'minute': None})
    @app.route(
        "/prayers/<date>/<month>/<hour>/<minute>",
        methods=["GET"], defaults={'meetingPoint': None})
    @app.route(
        "/prayers/<date>/<month>/<hour>/<minute>/<meetingPoint>",
        methods=["GET"])
    def getPrayerSlotTimetable(date, month, hour, minute, meetingPoint):
        time = None
        if hour is not None and minute is not None:
            time = (hour, minute)
        return warriorLogicController\
            .getPrayerSlotTimeTable(
                date, month, time, meetingPoint)\
            .serialise()

    @app.route(
        "/exams",
        methods=["POST"])
    def addStudentExamTimetable():
        successes, failures = studentLogicController\
            .addStudentExamSchedule(request.get_json())
        return jsonify(successes=successes, failures=failures)

    @app.route(
        "/lifegroup",
        methods=["GET"])
    def getLifegroups():
        return jsonify(studentLogicController.getLifegroups())

    @app.route("/prayers", methods=["POST"])
    def addPrayerSlotWarrior():
        successes, failures = warriorLogicController\
            .addPrayerWarriorSubscription(request.get_json())
        return jsonify(successes=successes, failures=failures)

    @app.route("/prayers/delete", methods=["POST"])
    def deletePrayerSlotWarrior():
        if warriorLogicController\
                .deletePrayerWarriorSubscription(request.get_json()):
            return "Deleted"
        return "Failed"
