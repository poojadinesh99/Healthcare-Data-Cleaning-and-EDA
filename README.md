# Healthcare Data Cleaning and Analysis

## Overview
This project focuses on cleaning and analyzing a healthcare dataset. The analysis includes handling missing data, removing duplicates, and visualizing important features of the dataset. The cleaned dataset is then saved for future use.

## Files Included:
1. **`data_cleaning_and_analysis.py`**: Python script for data cleaning and exploratory data analysis (EDA).
2. **`healthcare_dataset.csv`**: The original healthcare dataset used in the analysis.
3. **`cleaned_healthcare_dataset.csv`**: The cleaned version of the dataset after performing data preprocessing.
4. **Figures/Visualizations**: **`Figure_1.png`**, **`Figure_2.png`**, **`Figure_3.png`**, **`Figure_4.png`**, **`Figure_5.png`**: Generated plots from the analysis (e.g., Age Distribution, Gender Count, Billing Amount Distribution).

## Data Cleaning Process:
The data cleaning script performs the following tasks:
- Handles missing data:
    - **Age**: Replaces missing age values with the average age.
    - **Gender**: Replaces missing gender values with the most frequent gender (mode).
    - **Billing Amount**: Removes rows with missing billing amounts.
- Removes duplicates to ensure data integrity.
- Generates basic statistical summaries.
- Performs visualizations to better understand the distribution of data.

## Analysis & Visualizations:
The following visualizations are generated during the analysis:
1. **Age Distribution**: A histogram showing the distribution of patient ages.
2. **Gender Count**: A countplot showing the number of male and female patients.
3. **Billing Amount Distribution**: A histogram showing the distribution of billing amounts.
4. **Age Distribution by Gender**: A boxplot showing the distribution of age for each gender.
5. **Admission Type Count**: A countplot showing the distribution of admission types.

## Requirements:
To run this project locally, you need Python 3.x and the following libraries:
- **pandas**
- **matplotlib**
- **seaborn**

You can install the necessary packages using `pip`:

```bash
pip install pandas matplotlib seaborn
```

## How to Run:
Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/Healthcare-Data-Cleaning-and-EDA.git
```

Navigate to the project directory:

```bash
cd Healthcare-Data-Cleaning-and-EDA
```

Run the Python script to clean the data and generate visualizations:

```bash
python data_cleaning_and_analysis.py
```

The cleaned dataset will be saved as `cleaned_healthcare_dataset.csv` in the same directory.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
