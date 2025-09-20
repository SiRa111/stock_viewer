# project.py

def main():
    region = input("Enter your region (US/India): ").strip().lower()

    if region == "us":
        symbol = input("Enter US stock ticker (e.g., AAPL): ").upper()
        start_date = input("Start date (YYYY-MM-DD): ")
        end_date = input("End date (YYYY-MM-DD): ")
        data = fetch_us_stock_data(symbol, start_date, end_date)

    elif region == "india":
        symbol = input("Enter NSE stock symbol (e.g., RELIANCE): ").upper()
        start_date = input("Start date (YYYY-MM-DD): ")
        end_date = input("End date (YYYY-MM-DD): ")
        data = fetch_indian_stock_data(symbol, start_date, end_date)

    else:
        print("Invalid region. Please enter US or India.")
        return

    price_points, volume_points = process_stock_data(data)
    create_stock_animation(price_points, volume_points, symbol, region)


def fetch_us_stock_data(symbol, start_date, end_date):
    """Fetch US stock data using yfinance."""
    import yfinance as yf
    df = yf.download(symbol, start=start_date, end=end_date)
    if df.empty:
        raise ValueError(f"No data found for {symbol}")
    return df.reset_index()


def fetch_indian_stock_data(symbol, start_date, end_date):
    """Fetch Indian stock data using nsepy."""
    from nsepy import get_history
    from datetime import datetime
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    df = get_history(symbol=symbol, start=start, end=end)
    if df.empty:
        raise ValueError(f"No data found for {symbol}")
    return df.reset_index()


def process_stock_data(df):
    """Convert stock DataFrame to points suitable for Manim plotting."""
    price_points = [(i, row['Close']) for i, row in df.iterrows()]
    volume_points = [(i, row['Volume']) for i, row in df.iterrows()]
    return price_points, volume_points


def create_stock_animation(price_points, volume_points, symbol, region):
    """Use Manim to create a smooth animated stock chart video."""
    from manim import Scene, Axes, VMobject, Dot, Rectangle, Text, config, tempconfig, linear, smooth
    import numpy as np
    from scipy.interpolate import CubicSpline

    class StockChart(Scene):
        def construct(self):
            axes = Axes(
                x_range=[0, len(price_points), max(1, len(price_points)//10)],
                y_range=[min([p[1] for p in price_points])*0.95,
                         max([p[1] for p in price_points])*1.05, 10],
                x_length=10, y_length=5
            )
            self.add(axes)

            # Smooth price curve using CubicSpline
            x = np.array([p[0] for p in price_points])
            y = np.array([p[1] for p in price_points])
            cs = CubicSpline(x, y)
            xs_smooth = np.linspace(x[0], x[-1], 500)
            ys_smooth = cs(xs_smooth)
            points_smooth = [axes.coords_to_point(xi, yi) for xi, yi in zip(xs_smooth, ys_smooth)]

            # Create VMobject path for smooth animation
            path = VMobject(color=BLUE)
            path.set_points_as_corners([points_smooth[0], points_smooth[1]])
            self.add(path)

            for i in range(2, len(points_smooth)):
                path.add_points_as_corners([points_smooth[i]])
                self.play(
                    path.animate.set_points_as_corners(points_smooth[:i]),
                    run_time=0.02,
                    rate_func=linear
                )

            # Moving dot along the curve
            dot = Dot(color=RED).move_to(points_smooth[0])
            self.add(dot)
            self.play(dot.animate.move_to(points_smooth[-1]), run_time=5, rate_func=smooth)

            # Optional: volume bars
            max_vol = max([v for _, v in volume_points])
            for x_idx, vol in volume_points:
                height = vol / max_vol * 2  # scale volume for visualization
                bar = Rectangle(height=height, width=0.1, color=YELLOW).next_to(points_smooth[int(x_idx * len(points_smooth)/len(price_points))], DOWN, buff=0)
                self.add(bar)

            # Title
            title = Text(f"{symbol} Stock Price ({region.upper()})").to_edge(UP)
            self.add(title)

    # Render the video
    with tempconfig({"quality": "low_quality"}):
        StockChart().render()


if __name__ == "__main__":
    main()
