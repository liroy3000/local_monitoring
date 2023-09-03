#!/usr/bin/env python3

from settings import settings
if settings["sender"] == "telegram":
    from settings import tg
    from modules.alerter-tg import alerter

from modules.du import du
from modules.la import la
from modules.uptime import uptime

for i in du(settings):
    alerter(tg, i)
for i in la(settings):
    alerter(tg, i)
for i in uptime(settings):
    alerter(tg, i)
