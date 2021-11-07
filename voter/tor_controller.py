import logging

from stem import Signal
from stem.control import Controller

from voter.settings import TOR_PASSWORD

_log = logging.getLogger(__name__)


class TorController:
    @staticmethod
    def create_new_tor_connection() -> None:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=TOR_PASSWORD)
            _log.info("Success!")
            controller.signal(Signal.NEWNYM)
            _log.info("New Tor connection processed")
