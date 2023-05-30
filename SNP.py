import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Import the data
df = pd.read_csv("data.csv")

# Identify the SNP
snp = "rs123456789"

# Create a contingency table
table = pd.crosstab(df["diabetes"], df[snp])

# Run the chi-squared test
chi2, pvalue, df, expected = chi2_contingency(table)

# Print the results
print("Chi-squared test:", chi2)
print("p-value:", pvalue)

# Interpretation
if pvalue < 0.05:
    print("The SNP is significantly associated with Type 2 Diabetes.")
else:
    print("The SNP is not significantly associated with Type 2 Diabetes.")
