import plotly.express as px
from plotly.graph_objects import Figure
from functions.download import download_data


def plot_ts(ticker:str) -> Figure:
    """
    Plot historical stock data.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol 

    Returns
    -------
    Figure
        A plotly graph.

    Notes
    -----
    
    """

    df = download_data(ticker)

    fig = px.line(
        df, x = 'Date', y = 'Close',
        title = f'{ticker} Stock Price'
    )

    return fig
