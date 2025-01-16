# Data Preprocessing and Correlation Matrix for NSL-KDD Dataset  
This repository contains Python code for preprocessing the NSL-KDD dataset and generating a correlation matrix to analyze feature relationships. This project was useful for understanding feature interactions and preparing the dataset for machine learning or visualization tasks.  

## Overview  
The NSL-KDD dataset is a commonly used benchmark dataset for intrusion detection systems. The preprocessing script in this repository:  
1. Loads and cleans the raw dataset.  
2. Encodes labels for binary classification (normal vs. malicious).  
3. Generates a correlation matrix to identify relationships between numerical features.  

## Features  
- **Data Cleaning**: Handles missing values and reformats the dataset for analysis.  
- **Label Encoding**: Maps attack labels to binary categories (`normal` or `malicious`).  
- **Correlation Analysis**: Creates a correlation matrix to visualize feature relationships.  

## Files  
- **`preprocess_data.py`**: The main Python script for data preprocessing and correlation matrix generation.  
- **`KDDTrain+.txt`**: The raw NSL-KDD dataset file (not included, replace with your own).  
- **`KDDTrain_Cleaned.csv`**: The cleaned and processed dataset.  
- **`correlation_matrix.csv`**: The computed correlation matrix for numerical features.
- **`corr_reshaped.csv`**: The reshaped correlation matrix for easier use in Tableau.

## Requirements  
- Python 3.7+  
- Libraries:  
  - pandas  
  - numpy  

Install required libraries using:  
```bash
pip install pandas numpy
```
**## Output**
* Cleaned Dataset: Ready-to-use CSV file for further analysis or modeling.
* Correlation Matrix: A CSV file representing the correlation coefficients between numerical features.
* Reshaped Correlation Matrix: A CSV file containing the reshaped correlation matrix. 

**## Example**
* The visualised data using tableau public:
  
  ![image](https://github.com/user-attachments/assets/833b5349-1f43-4aa1-824c-4d799c05bc4a)

  link: https://public.tableau.com/views/TDDforNSL-KDDDatabase/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

* Sample correlation matrix:
  
  ![image](https://github.com/user-attachments/assets/e4b66662-1040-4a57-b809-be1663661e36)


* Sample reshaped correlation matrix:

  ![image](https://github.com/user-attachments/assets/60d7c3dd-48b2-4dfb-ad0b-a3927a771852)

