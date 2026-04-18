"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


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

    Notes
    -----
    The function uses :func:`numpy.random.default_rng` to create a reproducible
    random number generator when a seed is provided. Arrays are returned as
    ``float64`` NumPy ndarrays.
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
