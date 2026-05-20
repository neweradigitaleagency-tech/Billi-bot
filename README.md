# Billi Bot

A trading framework for cryptocurrencies. Forked from [Jesse](https://github.com/jesse-ai/jesse).

Billi is an open-source framework for algorithmic cryptocurrency trading. It supports backtesting, live trading, and strategy development across multiple exchanges.

## Features

- **Backtesting** — Simulate strategies against historical data
- **Live Trading** — Deploy strategies on real exchange accounts
- **Multi-Exchange** — Binance, Coinbase, Kraken, and more via unified API
- **Candles Pipelines** — Flexible data ingestion and processing
- **Research Mode** — Jupyter-friendly research tools for strategy exploration
- **MCP Server** — AI agent integration via Model Context Protocol
- **REST API** — FastAPI-based HTTP API for remote control

## Quick Start

```bash
pip install -r requirements.txt
billi run
```

## Commands

| Command             | Description                          |
|---------------------|--------------------------------------|
| `billi run`         | Run live trading                     |
| `billi backtest`    | Run a backtest                       |
| `billi research`    | Launch research mode                 |
| `billi import`      | Import candles from exchange         |
| `billi list`        | List available strategies            |
| `billi version`     | Show version                         |

## Project Structure

```
billi-bot/
├── billi/              # Main source code
│   ├── cli.py          # CLI entry point
│   ├── config.py       # Configuration
│   ├── strategies/     # Trading strategies
│   ├── exchanges/      # Exchange integrations
│   ├── models/         # Data models
│   ├── routes/         # FastAPI routes
│   └── mcp/            # MCP server (AI agent integration)
├── tests/              # Test suite
├── assets/             # Static assets
└── requirements.txt    # Python dependencies
```

## Configuration

Copy `.env.example` to `.env` and set your exchange API keys and other settings:

```
BILLI_API_URL=http://localhost:9000
BILLI_PASSWORD=your_password
```

## License

MIT
