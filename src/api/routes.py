from flask import request, jsonify
import validator

ERROR_INVALID_JSON = "Invalid JSON Format [{}]"


def apiError(msg):
    return {"error": msg}


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
        "/lifegroup",
        methods=["GET"])
    def getLifegroups():
        return jsonify(studentLogicController.getLifegroups())

    @app.route(
        "/exams",
        methods=["POST"])
    def addStudentExamTimetable():
        requestJson = request.get_json()
        if not validator\
                .validateAddStudentExamScheduleJson(requestJson):
            return jsonify(apiError(ERROR_INVALID_JSON))

        successes, failures = studentLogicController\
            .addStudentExamSchedule(requestJson)
        return jsonify(successes=successes, failures=failures)

    @app.route("/prayers", methods=["POST"])
    def addPrayerSlotWarrior():
        requestJson = request.get_json()
        if not validator\
                .validateAddPrayerWarriorSubscriptionJson(requestJson):
            return jsonify(apiError(ERROR_INVALID_JSON))
        successes, failures = warriorLogicController\
            .addPrayerWarriorSubscription(requestJson)
        return jsonify(successes=successes, failures=failures)

    @app.route("/prayers/delete", methods=["POST"])
    def deletePrayerSlotWarrior():
        requestJson = request.get_json()
        if not validator\
                .validateDeletePrayerWarriorSubscriptionJson(requestJson):
            return jsonify(apiError(ERROR_INVALID_JSON))
        if warriorLogicController\
                .deletePrayerWarriorSubscription(requestJson):
            return "Deleted"
        return "Failed"
