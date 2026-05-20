from billi.strategies import Strategy
import billi.helpers as jh
from billi import utils


class TestPositionExchangeTypeProperty2(Strategy):
    def before(self) -> None:
        if self.index == 0:
            assert self.exchange_type == 'spot'

    def should_long(self):
        return False

    def go_long(self):
        pass

    def should_cancel_entry(self):
        return False
