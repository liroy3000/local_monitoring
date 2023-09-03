#!/usr/bin/env python3

def du(settings):
    from os import statvfs
    from os.path import exists
    from datetime import datetime

    i = 0
    result = []
    for partition in settings["partitions"]:
        st = statvfs(partition[0])
        du = st.f_bsize * st.f_bavail / 1024 / 1024
        new_string = "\n" + datetime.now().strftime("%m.%d.%Y-%H:%M") + " partition: " + partition[0] + " value: " + str(round(du, 2))
        file_path = settings["data_path"] + "/du" + str(i) + ".log"
        trigger_path = settings["data_path"] + "/du-trigger" + str(i)
        with open(file_path, "a") as file:
            file.write(new_string)
        i = i + 1

        # Create trigger-file if not exists
        if exists(trigger_path) == False:
            with open(trigger_path, "w") as file:
                file.write(str(0))

        with open(trigger_path, "r") as file:
            trigger = file.read()

        if trigger == "1" and du > partition[1]:
            result.append({"alert": "du", "status": "success", "partition": partition[0], "value": str(round(du, 2)), "limit": partition[1]})
            with open(trigger_path, "w") as file:
                file.write(str(0))

        if trigger != "1" and du < partition[1]:
            result.append({"alert": "du", "status": "problem", "partition": partition[0], "value": str(round(du, 2)), "limit": partition[1]})
            with open(trigger_path, "w") as file:
                file.write(str(1))

    return(result)
