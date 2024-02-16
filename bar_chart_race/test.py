import pandas as pd
import matplotlib.pyplot as plt
import bar_chart_race as bcr

# Load the data
data = pd.read_csv('test.csv')

# Set the index to the starting capital of A
data = data.set_index('start')

# Create the animated bar chart race
bcr.bar_chart_race(
    df=data,
    filename='race.gif',
    orientation='h',
    sort='desc',
    n_bars=3,
    steps_per_period=10,
    interpolate_period=False,
    bar_size=.95,
    period_length=500,
    title='Race',
    writer='pillow',
    bar_texttemplate="{x:,.2f}",
    tick_template="{x:,.2f}"
)

plt.show()
