from flask import Flask
from redis import Redis, RedisError
import os
import socket


app = Flask(__name__)
redis = Redis(host="redis")


def validate_visits(visits):
    assert visits > 0


@app.route("/")
def hello():
    try:
        visits = redis.incr('counter')
        validate_visits(visits)

    except RedisError:
        visits = "<i>counter disabled. Cannot connect to Redis.</i>"

    html = "<h3>Hola {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}<br/>"

    return html.format(name=os.getenv('NAME', "world"), hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
