from datetime import datetime

TIME = datetime.now().replace(microsecond=0).isoformat(sep=' ')

RESPONSE = {
    "response": None,
    "time": str(TIME),
    "alert": None,
    "from": None,
    "contacts": None
}

PRESENCE = {
    "action": "presence",
    "time": str(TIME),
    "type": "status",
    "user": {
        "account_name": None,
        "status": "Yep, I am here!"
    }
}

MESSAGE = {
    "action": "msg",
    "time": str(TIME),
    "to": None,
    "from": None,
    "message": None,
}
