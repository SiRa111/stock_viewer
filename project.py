import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

def fetch_stock_data(symbol: str, start_date: str, end_date: str):
    if symbol.upper() in ["NSE", "INDIA"]:
        symbol = symbol + ".NS"
    df = yf.download(symbol, start=start_date, end=end_date)
    if df.empty:
        raise ValueError(f"No data found for {symbol}")
    return df.reset_index()

def prepare_chart_data(df):
    dates = [d.strftime('%Y-%m-%d') for d in df['Date']]
    prices = list(df['Close'])
    volumes = list(df['Volume'])
    return dates, prices, volumes



def create_stock_animation(dates, prices, volumes, symbol, region):
    fig = go.Figure(
        data=[go.Scatter(x=[dates[0]], y=[prices[0]], mode='lines+markers', name='Price')],
        layout=go.Layout(
            title=f"{symbol} Stock Price ({region})",
            xaxis_title="Date",
            yaxis_title="Price",
            updatemenus=[dict(type="buttons",
                              buttons=[dict(label="Play",
                                            method="animate",
                                            args=[None, {"frame": {"duration": 100, "redraw": True},
                                                         "fromcurrent": True}])])]
        ),
        frames=[go.Frame(data=[go.Scatter(x=dates[:k+1], y=prices[:k+1], mode='lines+markers')],
                         name=str(k)) for k in range(1, len(dates))]
    )
    fig.show()

def main():
    print("Welcome to Stock Animator!")
    region = input("Enter region (US or India): ").strip().lower()
    symbol = input("Enter stock symbol: ").strip().upper()
    start_date = input("Start date (YYYY-MM-DD): ").strip()
    end_date = input("End date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    try:
        df = fetch_stock_data(symbol, start_date, end_date)
    except ValueError as e:
        print(e)
        return
    dates, prices, volumes = prepare_chart_data(df)
    create_stock_animation(dates, prices, volumes, symbol, region.capitalize())

if __name__ == "__main__":
    main()
