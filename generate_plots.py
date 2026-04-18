"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
def generate_data(seed: int | None = None):
    """Generate synthetic temperature readings for two sensors.

    Parameters
    ----------
    seed : int or None
        Seed for the random number generator. Use an integer (e.g. the last
        4 digits of a Drexel ID) to make results reproducible. If ``None``,
        the RNG will be unpredictable.

    Returns
    -------
    sensor_a : numpy.ndarray, shape (200,)
        Temperature readings (degrees Celsius) from Sensor A. Drawn from a
        normal distribution with mean 25.0 and standard deviation 3.0.

    sensor_b : numpy.ndarray, shape (200,)
        Temperature readings (degrees Celsius) from Sensor B. Drawn from a
        normal distribution with mean 27.0 and standard deviation 4.5.

    timestamps : numpy.ndarray, shape (200,)
        Timestamp values (seconds) uniformly distributed between 0 and 10,
        sorted in ascending order so the three arrays line up chronologically.
    """
    rng = np.random.default_rng(seed)

    n_readings = 200
    # timestamps uniformly distributed between 0 and 10 seconds
    timestamps = rng.uniform(0.0, 10.0, size=n_readings).astype(np.float64)

    # Sensor distributions
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n_readings).astype(np.float64)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n_readings).astype(np.float64)

    # Sort by time so data appear chronologically (useful for plotting)
    sort_idx = np.argsort(timestamps)
    timestamps = timestamps[sort_idx]
    sensor_a = sensor_a[sort_idx]
    sensor_b = sensor_b[sort_idx]

    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_scatter(ax: Axes, timestamps: np.ndarray, sensor_a: np.ndarray, sensor_b: np.ndarray) -> None:
    """Draw the scatter plot of two sensors on an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes object to draw the scatter plot on. Modified in place.

    timestamps : numpy.ndarray, shape (N,)
        Time values in seconds (x-axis).

    sensor_a : numpy.ndarray, shape (N,)
        Temperature readings from Sensor A (y values for the first series).

    sensor_b : numpy.ndarray, shape (N,)
        Temperature readings from Sensor B (y values for the second series).

    Returns
    -------
    None
        The function modifies ``ax`` in place and returns nothing.
    """
    # Plot raw samples with distinct markers and colors
    ax.scatter(timestamps, sensor_a, s=40, c='tab:blue', alpha=0.7,
               label='Sensor A', edgecolors='k')
    ax.scatter(timestamps, sensor_b, s=40, c='tab:orange', alpha=0.7,
               marker='s', label='Sensor B', edgecolors='k')

    # Labels, title and grid
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Scatter Plot: Temperature vs Time for Two Sensors')

    # Legend and grid help with readability
    ax.legend()
    ax.grid(alpha=0.3)

    # Function intentionally returns None (modifies ax in place)
    return None

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main(seed: int | None = 1234) -> None:
    """Generate data, create plots, and save PNG files.

    Parameters
    ----------
    seed : int or None, optional
        Seed for reproducible data generation. If ``None``, randomness is
        uncontrolled. Default is 1234.

    Returns
    -------
    None
        Creates and saves three PNG files in the current working directory:
        'scatter.png', 'histogram.png', and 'boxplot.png'.
    """
    # Generate data
    sensor_a, sensor_b, timestamps = generate_data(seed)

    # Scatter plot
    fig, ax = plt.subplots(figsize=(10, 5))
    plot_scatter(ax, timestamps, sensor_a, sensor_b)
    fig.tight_layout()
    fig.savefig('scatter.png', dpi=200)
    plt.close(fig)

    # Histogram
    fig, ax = plt.subplots(figsize=(8, 5))
    bins = np.linspace(min(sensor_a.min(), sensor_b.min()) - 1,
                       max(sensor_a.max(), sensor_b.max()) + 1, 30)
    ax.hist(sensor_a, bins=bins, alpha=0.6, label='Sensor A', color='tab:blue', edgecolor='k')
    ax.hist(sensor_b, bins=bins, alpha=0.6, label='Sensor B', color='tab:orange', edgecolor='k')
    ax.axvline(sensor_a.mean(), color='tab:blue', linestyle='--', linewidth=2, label='Sensor A mean')
    ax.axvline(sensor_b.mean(), color='tab:orange', linestyle='--', linewidth=2, label='Sensor B mean')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Histogram: Sensor Temperature Readings')
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig('histogram.png', dpi=200)
    plt.close(fig)

    # Box plot
    fig, ax = plt.subplots(figsize=(6, 6))
    data = [sensor_a, sensor_b]
    bp = ax.boxplot(data, labels=['Sensor A', 'Sensor B'], patch_artist=True, showmeans=True)
    colors = ['tab:blue', 'tab:orange']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    for median in bp['medians']:
        median.set(color='black', linewidth=2)
    if 'means' in bp:
        for mean in bp['means']:
            mean.set(marker='D', markerfacecolor='white', markeredgecolor='black')
    overall_mean = np.concatenate(data).mean()
    ax.axhline(overall_mean, color='gray', linestyle='--', linewidth=1.5,
               label=f'Overall mean ({overall_mean:.2f} °C)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Box Plot: Sensor Temperature Distributions')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    fig.tight_layout()
    fig.savefig('boxplot.png', dpi=200)
    plt.close(fig)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate sensor plots and save as PNG files.')
    parser.add_argument('--seed', type=str, default='1234',
                        help='Integer seed for RNG (default: 1234). Use None for non-deterministic outputs by passing the string "None".')
    args = parser.parse_args()

    seed_arg = args.seed
    # Allow the user to pass the literal string 'None' to disable seeding
    if isinstance(seed_arg, str) and seed_arg.lower() == 'none':
        seed = None
    else:
        try:
            seed = int(seed_arg)
        except ValueError:
            seed = 1234

    main(seed)

