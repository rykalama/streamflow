import numpy as np
import matplotlib.pyplot as plt

def load_streamflow(filename):
    data = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',', dtype=str, skip_header=1)
    dates = data[:, 0].astype('datetime64[m]')
    flows = data[:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):

    for i, site in enumerate(sites):
        plt.plot(dates, flows[:, i], label=site)

    plt.title('Provo River Streamflow Data (2021)')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')

    plt.xticks(dates[::240], rotation=45)

    plt.legend(title='Site Numbers', loc='upper right')
    plt.grid(True, linestyle='-')
    plt.tight_layout()
    plt.show()

sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
