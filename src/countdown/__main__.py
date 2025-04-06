import os
from countdown.cli import cli

# To invoke the profiler, set this environment variable and run as a module
# i.e. python -m countdown ....
if "countdown_PROFILE" in os.environ:
    import cProfile
    from countdown import log

    log.info("Running under profiler")

    cProfile.run("cli()", sort="time")
else:
    cli()
