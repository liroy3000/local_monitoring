#!/usr/bin/env python3

def la(settings):
    from os import getloadavg
    from os.path import exists
    from datetime import datetime

    la = getloadavg()
    result = []
    file_path = settings["data_path"] + "/la" + ".log"
    trigger_path = settings["data_path"] + "/la-trigger"
    new_string = "\n" + datetime.now().strftime("%m.%d.%Y-%H:%M") + " LA: " + str(round(la[0], 2)) + " " + str(round(la[1], 2)) + " " + str(round(la[2], 2))
    with open(file_path, "a") as file:
        file.write(new_string)

    # Create trigger-file if not exists
    if exists(trigger_path) == False:
        with open(trigger_path, "w") as file:
            file.write(str(0))

    with open(trigger_path, "r") as file:
        trigger = file.read()

    if trigger == "1" and la[2] < settings["la_limit"]:
        result.append({"alert": "la", "status": "success", "value": str(round(la[2], 2)), "limit": settings["la_limit"]})
        with open(trigger_path, "w") as file:
            file.write(str(0))

    if trigger != "1" and la[2] > settings["la_limit"]:
        result.append({"alert": "la", "status": "problem", "value": str(round(la[2], 2)), "limit": settings["la_limit"]})
        with open(trigger_path, "w") as file:
            file.write(str(1))

    return(result)
