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

# Max for 10163000 is 131. Average is 56.95236.
def summarize(dates, flows, sites):
    print(f"{'Gauge':<12}{'Max (cfs)':<12}{'Date of max':<21}{'Min (cfs)':<12}{'Avg (cfs)'}")

    with open("streamflow_summary.csv", "w", newline="") as f:
        f.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

        for i, site in enumerate(sites):
            column = flows[:, i]
            mean_flow = np.mean(column)
            max_index = np.argmax(column)
            max_flow = np.max(column)
            min_flow = np.min(column)
            max_date = np.datetime_as_string(dates[max_index], unit='m').replace('T', ' ')

            print(f"{site:<12}{max_flow:<12.1f}{max_date:<21}{min_flow:<12.1f}{mean_flow:.1f}")
            f.write(f"{site},{max_flow},{max_date},{min_flow},{mean_flow:.1f}\n")

sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)

plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")