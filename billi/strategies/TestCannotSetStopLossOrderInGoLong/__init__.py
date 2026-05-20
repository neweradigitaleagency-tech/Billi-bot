from billi.strategies import Strategy
import billi.helpers as jh
from billi import utils


class TestCannotSetStopLossOrderInGoLong(Strategy):
    def should_long(self) -> bool:
        return self.price == 10

    def go_long(self) -> None:
        self.buy = 1, self.price
        self.stop_loss = 1, self.price - 1

    def should_cancel_entry(self):
        return False
