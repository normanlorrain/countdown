# A central place to validate and access our configuration,
# merging settings from the config file and the command line.
# Configuration attributes are set as attributes of this module.


import sys
from datetime import datetime
from countdown import log

this_mod = sys.modules[__name__]

EXPIRATION = None  # Placeholder for the countdown datetime

# Configuration file string constants
# These are also used as command-line Click options
# See cli.py
FULLSCREEN = "fullscreen"
POINTSIZE = "pointsize"
TYPEFACE = "typeface"
EXPIRATION = "expiration"

YEAR = "year"
MONTH = "month"
DAY = "day"     
HOUR = "hour"
MINUTE = "minute"
SECOND = "second"



class ConfigurationError(Exception):
    pass


def init(ctx):
    # Configuration starts with what was on the command line
    # Convert the parameters into attributes of this module
    for param, value in ctx.params.items():
        setattr(this_mod, param, value)

    global EXPIRATION
    EXPIRATION = datetime(
        year=getattr(this_mod, YEAR),
        month=getattr(this_mod, MONTH),
        day=getattr(this_mod, DAY),
        hour=getattr(this_mod, HOUR),
        minute=getattr(this_mod, MINUTE),
        second=getattr(this_mod, SECOND))
    log.info(f"Countdown End: {EXPIRATION}")