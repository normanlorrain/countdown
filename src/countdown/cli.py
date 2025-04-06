# Command Line Interface
# click is pretty cool

import click
import pathlib

from countdown import log, config, controller


@click.command(
    epilog="""To reload the configuration, send it the USR1 signal:

    pkill -USR1 countdown
\b

hi Isaac

See https://github.com/normanlorrain/countdown for more details."""
)
@click.version_option()

@click.option(
    "-f", f"--{config.FULLSCREEN}", is_flag=True, 
    default=config.defaults[config.FULLSCREEN], 
    help="Full screen mode"
)


@click.option(
    "-s",
    f"--{config.SIZE}",
    type=click.IntRange(min=1, max=None),
    required=False,
    default=config.defaults[config.SIZE],
    help="Size of font.",
)
@click.option(
    "-t",
    f"--{config.TYPEFACE}",
    multiple=False,
    required=False,
    default=config.defaults[config.TYPEFACE],
    help="Font.",
)

@click.pass_context
def countdown(
    ctx, fullscreen, size, typeface
):
    """A countdown clock."""

    # At this point switches --version and --help have been dealt with by click.
    # Therefore we can initialize our log (which we start with an enpty file)
    log.init()


    runState = True
    while runState:
        config.init(ctx)
        controller.init()
        runState = controller.run()


def cli():
    try:
        countdown()
    except SystemExit:
        log.info("Application ended normally (System Exit)")
    except KeyboardInterrupt:
        log.warning("Application ended (KeyboardInterrupt)")
    except Exception:
        log.exception(
            "Application ended. (UNCAUGHT EXCEPTION)",
        )
