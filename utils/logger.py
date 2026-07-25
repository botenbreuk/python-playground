import logging
import sys


class _ColorFormatter(logging.Formatter):
    """Adapted from the logback pattern:
    %magenta(%d{dd-MM-yyyy HH:mm:ss.SSS}) %highlight(%-5p) %yellow([%-10.10t]) %green(%60.60c:%-3L) %m%n
    The origin width is narrowed to 20 (from Java's 60) since Python module names are much shorter.
    Colors are only applied when writing to a real terminal.
    """

    _MAGENTA = "\033[35m"
    _YELLOW = "\033[33m"
    _GREEN = "\033[32m"
    _RESET = "\033[0m"
    _LEVEL_COLORS = {
        logging.DEBUG: "\033[39m",  # default fg, matches logback's fallback for TRACE/DEBUG
        logging.INFO: "\033[34m",  # blue
        logging.WARNING: "\033[31m",  # red
        logging.ERROR: "\033[1;31m",  # bold red
        logging.CRITICAL: "\033[1;4;31m",  # bold underline red; no logback equivalent, escalates past ERROR
    }

    def format(self, record: logging.LogRecord) -> str:
        if not sys.stderr.isatty():
            return super().format(record)

        timestamp = f"{self.formatTime(record, self.datefmt)}.{int(record.msecs):03d}"
        level = f"{record.levelname:<5}"
        thread = f"[{record.threadName:<10.10}]"
        origin = f"{record.module:>20.20}:{record.lineno:<3}"
        level_color = self._LEVEL_COLORS.get(record.levelno, "\033[39m")

        date_part = f"{self._MAGENTA}{timestamp}{self._RESET}"
        level_part = f"{level_color}{level}{self._RESET}"
        thread_part = f"{self._YELLOW}{thread}{self._RESET}"
        origin_part = f"{self._GREEN}{origin}{self._RESET}"
        return f"{date_part} {level_part} {thread_part} {origin_part} {record.getMessage()}"


# Logger config
_handler = logging.StreamHandler()
_handler.setFormatter(
    _ColorFormatter(
        fmt="%(asctime)s.%(msecs)03d %(levelname)-5s [%(threadName)-10.10s] %(module)20.20s:%(lineno)-3d %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
    )
)
logging.basicConfig(level=logging.DEBUG, handlers=[_handler])
log = logging.getLogger(__name__)
