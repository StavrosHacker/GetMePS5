def logger(msg, status):
    send = "[GetMePS5] " + msg

    if status == 0:
        print(send)
    else:
        return send