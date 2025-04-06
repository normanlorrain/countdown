# A central place to validate and access our configuration,
# merging settings from the config file and the command line.
# Configuration attributes are set as attributes of this module.

import pathlib
import enum
import tomllib
import sys
from types import SimpleNamespace
from countdown import log

this_mod = sys.modules[__name__]



# Configuration file string constants
# These are also used as command-line Click options
# See cli.py
FULLSCREEN = "fullscreen"
SIZE = "size"
TYPEFACE = "typeface"


# General defaults
defaults = {
    FULLSCREEN: False,
    SIZE: 120,
    TYPEFACE: "freesans",
}



class ConfigurationError(Exception):
    pass


def init(ctx):
    # Configuration starts with what was on the command line
    # Convert the parameters into attributes of this module
    for param, value in ctx.params.items():
        setattr(this_mod, param, value)

 