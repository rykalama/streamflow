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
    print(f"{'Gauge':<12}{'Max (cfs)':<12}{'Date of max':<21}{'Min (cfs)':<12}{'Avg (cfs)'}") # Prints out the table.

    with open("streamflow_summary.csv", "w", newline="") as f: # Creates the file.
        f.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n") # This is what is being written to the file.

        for i, site in enumerate(sites): # This is a for loop that goes through each site and prints out the max, min, and average values for every site.
            column = flows[:, i] # This variable is the column of data for the site.
            mean_flow = np.mean(column) # np.mean calculates the average of the column.
            max_index = np.argmax(column) # np.argmax finds where the maximum value is at in the column.
            max_flow = np.max(column) # np.max calculates the maximum value in the column.
            min_flow = np.min(column) # np.min calculates the minimum value in the column.
            max_date = np.datetime_as_string(dates[max_index], unit='m').replace('T', ' ') # This function converts the date into a string.

            print(f"{site:<12}{max_flow:<12.1f}{max_date:<21}{min_flow:<12.1f}{mean_flow:.1f}") # This where the table will get printed out from.
            f.write(f"{site},{max_flow},{max_date},{min_flow},{mean_flow:.1f}\n") # This is what will get written to the file.

sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)

plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")

threshold = float(input("Give me a flow threshold in cfs: ")) # This is the input function that has the user type in a flow threshold. It is set to be a variable.

above_threshold = flows[:, 0] > threshold # This variable is set to a True or False array that checks if the flow is above the threshold for the first site.
hours_above_threshold = np.sum(above_threshold) * 0.25 # All of the values that are True in the array are summed up and multipkied by 0.25.

print(f"The flow was above {threshold:.1f} cfs for {hours_above_threshold:.2f} hours in June 2021.") # This line of code prints out the results for the threshold values.
