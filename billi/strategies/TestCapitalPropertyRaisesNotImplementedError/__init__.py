from billi.strategies import Strategy
import billi.helpers as jh
from billi import utils


class TestCapitalPropertyRaisesNotImplementedError(Strategy):
    def should_long(self) -> bool:
        self.capital
        return False

    def go_long(self) -> None:
        pass

    def should_cancel_entry(self):
        return False
