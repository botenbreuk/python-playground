import logging
import sys


class _ColorFormatter(logging.Formatter):
    """Colors the timestamp, level, and message separately, but only when writing to a real terminal."""

    _DATE_COLOR = "\033[90m"  # gray
    _FILENAME_COLOR = "\033[35m"  # magenta
    _MESSAGE_COLOR = "\033[97m"  # bright white
    _LEVEL_COLORS = {
        logging.DEBUG: "\033[36m",  # cyan
        logging.INFO: "\033[32m",  # green
        logging.WARNING: "\033[33m",  # yellow
        logging.ERROR: "\033[31m",  # red
        logging.CRITICAL: "\033[1;31m",  # bold red
    }
    _RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        if not sys.stderr.isatty():
            return super().format(record)

        record.asctime = self.formatTime(record, self.datefmt)
        level_color = self._LEVEL_COLORS.get(record.levelno, self._RESET)
        date = f"{self._DATE_COLOR}[{record.asctime}]{self._RESET}"
        level = f"{level_color}[{record.levelname}]{self._RESET}"
        filename = f"{self._FILENAME_COLOR}[{record.filename}]{self._RESET}"
        message = f"{self._MESSAGE_COLOR}{record.getMessage()}{self._RESET}"
        return f"{date} {level} {filename}: {message}"


# Logger config
_handler = logging.StreamHandler()
_handler.setFormatter(
    _ColorFormatter(
        fmt="[%(asctime)s] [%(levelname)s] [%(filename)s]: %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
    )
)
logging.basicConfig(level=logging.DEBUG, handlers=[_handler])
log = logging.getLogger(__name__)
