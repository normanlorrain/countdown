# Command Line Interface
# click is pretty cool

import click

import datetime
from countdown import log, config, controller


@click.command(
    epilog="""See https://github.com/normanlorrain/countdown for more details."""
)
@click.version_option()




@click.option(
    f"-{config.YEAR[0]}",
    f"--{config.YEAR}",
    type=click.IntRange(min=datetime.datetime.now().year, max=None),
    required=False,
    default=datetime.datetime.now().year,
    help="Year.",
)

@click.option(
    f"-{config.MONTH[0]}",
    f"--{config.MONTH}",
    type=click.IntRange(min=1, max=12),
    required=False,
    default=datetime.datetime.now().month,
    help="Month.",
)

@click.option(
    f"-{config.DAY[0]}",
    f"--{config.DAY}",
    type=click.IntRange(min=1, max=31),
    required=False,
    default=datetime.datetime.now().day,
    help="Day.",
)

@click.option(
    f"-{config.HOUR[0]}",
    f"--{config.HOUR}",
    type=click.IntRange(min=0, max=23),
    required=False,
    default=datetime.datetime.now().hour,
    help="Hour.",
)

@click.option(
    f"-{config.MINUTE[0]}",
    f"--{config.MINUTE}",
    type=click.IntRange(min=0, max=59),
    required=False,
    default=datetime.datetime.now().minute +1,
    help="Minute.",
)

@click.option(
    f"-{config.SECOND[0]}",
    f"--{config.SECOND}",
    type=click.IntRange(min=0, max=59),
    required=False,
    default=datetime.datetime.now().second,
    help="Second.",
)







@click.option(
    "-f", f"--{config.FULLSCREEN}", is_flag=True, 
    default=False, 
    help="Full screen mode"
)



@click.option(
    f"-{config.TYPEFACE[0]}",
    f"--{config.TYPEFACE}",
    multiple=False,
    required=False,
    default="Arial",
    help="Typeface (font).",
)

@click.option(
    f"-{config.POINTSIZE[0]}",
    f"--{config.POINTSIZE}",
    type=click.IntRange(min=1, max=None),
    required=False,
    default=26,
    help="Size of text (point size).",
)

@click.pass_context
def countdown(
    ctx, year, month, day, hour, minute, second, fullscreen, pointsize, typeface
):
    """A countdown clock."""

    # At this point switches --version and --help have been dealt with by click.
    # Therefore we can initialize our log (which we start with an empty file)
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
