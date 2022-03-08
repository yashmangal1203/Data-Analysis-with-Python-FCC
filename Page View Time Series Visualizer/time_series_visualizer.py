import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    r".\Page View Time Series Visualizer\fcc-forum-pageviews.csv",
    parse_dates=["date"],
)
df = df.set_index("date")

# Clean data
df = df.loc[(df["value"] >= df.quantile(0.025)[0]) & (df["value"] <= df.quantile(0.975)[0])]


def draw_line_plot():
    # Draw line plot

    df2 = df.copy()

    fig, axes = plt.subplots(figsize=(15, 5))
    df2["value"].plot(kind="line", color="firebrick")
    plt.ylabel("Page Views")

    plt.xlabel("Date")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xticks(rotation=360, horizontalalignment="center")

    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df_bar = df.copy()

    # set up grouping by monthly average in chronological ord
    df_bar = df_bar.groupby([df_bar.index.strftime("%Y %b")])["value"].mean().reset_index(name="Month Avg")

    df_bar["date"] = pd.to_datetime(df_bar.date)

    df_bar.set_index("date")

    # create column with just the year, just month
    df_bar["year"] = df_bar["date"].dt.year
    df_bar["month"] = df_bar["date"].dt.month

    df_bar = df_bar.sort_values(by=["date"])

    # Draw bar plot

    fig = df_bar.pivot("year", "month", "Month Avg").plot(kind="bar", figsize=(10, 10)).figure
    plt.ylabel("Average Page Views")
    plt.xlabel("Years")
    plt.legend(
        labels=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        title="Months",
    )

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, sharex=False, figsize=(16, 5))

    # Year-wise
    axes[0] = sns.boxplot(ax=axes[0], data=df_box, x="year", y="value")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_ylabel("Page Views")
    axes[0].set_xlabel("Year")

    # Month-wise
    axes[1] = sns.boxplot(
        ax=axes[1],
        data=df_box,
        x="month",
        y="value",
        order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_ylabel("Page Views")
    axes[1].set_xlabel("Month")

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
