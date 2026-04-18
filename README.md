# Project overview

`generate_plots.py` creates synthetic temperature readings for two sensors, builds a 1x3 Matplotlib figure (scatter plot, histogram, and box plot), and saves the result as a PNG image.

# Repository contents

- `generate_plots.py`: Generates data and saves the combined visualization.
- `lab3_sensor_plots.ipynb`: Notebook version of the analysis workflow.
- `sensor_analysis.png`: Example/generated output image.

# Dependencies and environment setup

Activate your `ece105` conda environment, then install NumPy and Matplotlib:

```bash
conda activate ece105
conda install numpy matplotlib
```

Or with mamba:

```bash
conda activate ece105
mamba install numpy matplotlib
```

# How to run

From this directory, run:

```bash
python generate_plots.py
```

Optional: set a seed for reproducible data or disable seeding:

```bash
python generate_plots.py --seed 1234
python generate_plots.py --seed None
```

# Output files

Running the script writes:

- `sensor_analysis.png`: A single figure containing:
  - scatter plot of Sensor A and Sensor B vs. time,
  - histogram comparison of both sensors with mean lines,
  - box plot comparison with mean markers and overall mean reference line.

# AI tools used and disclosure

I used the copilot cli tool, which was directly integrated into vscode. This allowed it to directly make changes to the files without any assistance from me. 
