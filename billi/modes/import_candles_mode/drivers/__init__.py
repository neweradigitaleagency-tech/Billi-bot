from billi.enums import exchanges
from billi.modes.import_candles_mode.drivers.Binance.BinanceSpot import BinanceSpot
from billi.modes.import_candles_mode.drivers.Binance.BinanceUSSpot import BinanceUSSpot
from billi.modes.import_candles_mode.drivers.Binance.BinancePerpetualFutures import BinancePerpetualFutures
from billi.modes.import_candles_mode.drivers.Bitfinex.BitfinexSpot import BitfinexSpot
from billi.modes.import_candles_mode.drivers.Coinbase.CoinbaseSpot import CoinbaseSpot
from billi.modes.import_candles_mode.drivers.Binance.BinancePerpetualFuturesTestnet import BinancePerpetualFuturesTestnet
from billi.modes.import_candles_mode.drivers.Bybit.BybitUSDTPerpetual import BybitUSDTPerpetual
from billi.modes.import_candles_mode.drivers.Bybit.BybitUSDTPerpetualTestnet import BybitUSDTPerpetualTestnet
from billi.modes.import_candles_mode.drivers.Bybit.BybitUSDCPerpetual import BybitUSDCPerpetual
from billi.modes.import_candles_mode.drivers.Bybit.BybitUSDCPerpetualTestnet import BybitUSDCPerpetualTestnet
from billi.modes.import_candles_mode.drivers.Bybit.BybitSpotTestnet import BybitSpotTestnet
from billi.modes.import_candles_mode.drivers.Bybit.BybitSpot import BybitSpot
from billi.modes.import_candles_mode.drivers.Apex.ApexOmniPerpetualTestnet import ApexOmniPerpetualTestnet
from billi.modes.import_candles_mode.drivers.Apex.ApexOmniPerpetual import ApexOmniPerpetual
from billi.modes.import_candles_mode.drivers.Gate.GateUSDTPerpetual import GateUSDTPerpetual
from billi.modes.import_candles_mode.drivers.Gate.GateSpot import GateSpot
from billi.modes.import_candles_mode.drivers.Hyperliquid.HyperliquidPerpetual import HyperliquidPerpetual
from billi.modes.import_candles_mode.drivers.Hyperliquid.HyperliquidPerpetualTestnet import HyperliquidPerpetualTestnet


drivers = {
    # Perpetual Futures
    exchanges.BINANCE_PERPETUAL_FUTURES: BinancePerpetualFutures,
    exchanges.BINANCE_PERPETUAL_FUTURES_TESTNET: BinancePerpetualFuturesTestnet,
    exchanges.BITFINEX_SPOT: BitfinexSpot,
    exchanges.COINBASE_SPOT: CoinbaseSpot,
    exchanges.BYBIT_USDT_PERPETUAL: BybitUSDTPerpetual,
    exchanges.BYBIT_USDT_PERPETUAL_TESTNET: BybitUSDTPerpetualTestnet,
    exchanges.BYBIT_USDC_PERPETUAL: BybitUSDCPerpetual,
    exchanges.BYBIT_USDC_PERPETUAL_TESTNET: BybitUSDCPerpetualTestnet,
    exchanges.APEX_OMNI_PERPETUAL_TESTNET: ApexOmniPerpetualTestnet,
    exchanges.APEX_OMNI_PERPETUAL: ApexOmniPerpetual,
    exchanges.GATE_USDT_PERPETUAL: GateUSDTPerpetual,
    exchanges.GATE_SPOT: GateSpot,
    exchanges.HYPERLIQUID_PERPETUAL: HyperliquidPerpetual,
    exchanges.HYPERLIQUID_PERPETUAL_TESTNET: HyperliquidPerpetualTestnet,
    # Spot
    exchanges.BINANCE_SPOT: BinanceSpot,
    exchanges.BINANCE_US_SPOT: BinanceUSSpot,
    exchanges.BYBIT_SPOT_TESTNET: BybitSpotTestnet,
    exchanges.BYBIT_SPOT: BybitSpot,
}


driver_names = list(drivers.keys())
