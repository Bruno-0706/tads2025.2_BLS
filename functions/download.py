import pandas as pd
import yfinance as yf

def download_data(ticker: str = 'TSLA') -> pd.DataFrame:
    """
    Download historical price data for a given ticker using yfinance.

    Parameters
    ----------
    ticker : str, optional
        Stock ticker symbol to download (default: 'TSLA').

    Returns
    -------
    pd.DataFrame
        Historical OHLCV data with a `Date` column. Columns typically include
        'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', and 'Volume'.

    Notes
    -----
    - Uses `yfinance.download(..., period='max')` to fetch the full available history.
    - The returned DataFrame is reset with `.reset_index()` so the date is a regular column.
"""

    df = yf.download(
        ticker,
        period='max',
        multi_level_index=False
    ).reset_index()
    return df