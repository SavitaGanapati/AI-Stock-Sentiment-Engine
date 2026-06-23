"""
Global project settings.
"""

# -----------------------------
# Database
# -----------------------------

DATABASE_NAME = "stock_sentiment.db"

# -----------------------------
# Data folders
# -----------------------------

RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"
MODEL_PATH = "data/models/"

# -----------------------------
# Default stock universe
# -----------------------------

DEFAULT_TICKER = "RELIANCE.NS"

# -----------------------------
# News collection
# -----------------------------

MAX_NEWS_ARTICLES = 100

# -----------------------------
# Portfolio
# -----------------------------

INITIAL_CAPITAL = 1_000_000

# -----------------------------
# Technical indicators
# -----------------------------

MOVING_AVERAGE_PERIOD = 50
RSI_PERIOD = 14
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# -----------------------------
# Time decay
# -----------------------------

DECAY_FACTOR = 0.95

# -----------------------------
# Dashboard
# -----------------------------

TOP_N_STOCKS = 10

# -----------------------------
# Logging
# -----------------------------

LOG_FILE = "stock_engine.log"

# -----------------------------
# Future API Keys
# -----------------------------

TELEGRAM_BOT_TOKEN = ""
TWITTER_API_KEY = ""
OPENAI_API_KEY = ""