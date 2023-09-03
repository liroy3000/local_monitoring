#!/usr/bin/env python3

def uptime(settings):
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    if uptime_seconds < settings["uptime_limit"]:
        return([{"alert": "uptime", "status": "info", "message": "Server rebooted!"}])
    else:
        return([])
