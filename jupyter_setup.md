## Running Jupyter Notebook from PyCharm

This project uses Jupyter Notebook for data exploration and analysis.

### 1. Activate the virtual environment

Open the terminal in PyCharm and make sure the project virtual environment is activated:

```bash
.venv\Scripts\activate
```

You should see the environment name in the terminal:

```text
(.venv)
```

### 2. Start Jupyter Notebook

From the project root directory, run:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

A browser window will open with the Jupyter interface.

### 3. Open the notebook

Navigate to the required notebook file, for example:

```text
ch_5/data_discovery.ipynb
```

Run cells from top to bottom using:

* `Shift + Enter` — run current cell and move to the next one
* `Ctrl + Enter` — run current cell and stay on the same cell

### 4. Notebook workflow

The notebooks are used for:

* exploring datasets;
* checking data quality;
* identifying missing values;
* cleaning data;
* testing transformations.

After the data transformation logic is validated in the notebook, it can be moved into Python scripts for the ETL pipeline.

### 5. Stop Jupyter Notebook

To stop the Jupyter server, return to the PyCharm terminal and press:

```text
Ctrl + C
```

Confirm the shutdown if requested.
