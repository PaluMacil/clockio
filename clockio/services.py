import psycopg2
from psycopg2.extras import RealDictCursor
import json
import os
from datetime import datetime, time, date
from flask import Blueprint, Response


main = Blueprint('main', __name__)
connString = os.getenv('DB_ALARM_OWNER')


# Example: When running locally, use api to get a specific alarm. For instance, alarm 1 would be available at
# curl 127.0.0.1:8000/sub/alarm/alarm.io/get/1
@main.route('/get/<int:alarm_id>')
def test(alarm_id):
    try:
        conn = psycopg2.connect(connString)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM alarm.alarm alarm WHERE alarm.id=%(requested_id)s",
                    {'requested_id': str(alarm_id)})
        alarms = json.dumps(cur.fetchall(), cls=DateEncoder, indent=2)

        return Response(response=alarms,
                        status=200,
                        mimetype="application/json")
    except Exception as e:
        print("Error {0}".format(str(e.args[0])).encode("utf-8"))
        return 'Oops...'


class DateEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime) or isinstance(obj, date) or isinstance(obj, time):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


@main.before_request
def first():
    print('before anything')
