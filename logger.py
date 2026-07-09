# logger.py

from datetime import datetime
import platform

# ==========================
# Game Info
# ==========================

GAME_NAME = "Little Miss Witch"
GAME_VERSION = "v0.2 DevPreview"
BUILD = "00001"

# ==========================
# Logger
# ==========================

def log(module: str,
        function: str,
        error: str,
        command: str | None = None):
    """
    Appends an error entry to errorlogs.txt.

    Parameters
    ----------
    module : str
        Module where the error occurred.
    function : str
        Function where the error occurred.
    error : str
        Error message or traceback.
    command : str | None
        Last command entered by the player (optional).
    """

    now = datetime.now().astimezone()

    with open("errorlogs.txt", "a", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")

        file.write(f"Game       : {GAME_NAME}\n")
        file.write(f"Version    : {GAME_VERSION}\n")
        file.write(f"Build      : {BUILD}\n")
        file.write("\n")

        file.write(
            f"Timestamp  : "
            f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write(
            f"Timezone   : "
            f"{now.tzname()} ({now.strftime('%z')})\n"
        )
        file.write("\n")

        file.write(
            f"OS         : "
            f"{platform.system()} {platform.release()}\n"
        )
        file.write(
            f"Architecture: {platform.machine()}\n"
        )
        file.write(
            f"Python     : {platform.python_version()}\n"
        )
        file.write("\n")

        file.write(f"Module     : {module}\n")
        file.write(f"Function   : {function}\n")

        if command is not None:
            file.write(f"Command    : {command}\n")

        file.write("\n")

        file.write("Error\n")
        file.write("-" * 60 + "\n")
        file.write(str(error))
        file.write("\n")

        file.write("=" * 60 + "\n\n")