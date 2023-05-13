import pandas as pd
import numpy as np

# Load the SODA Chicago dataset
soda_chicago_df = pd.read_csv("soda_chicago.csv")

# Identify the homeless individuals in the SODA Chicago dataset who are at risk for E. coli O157:H7
at_risk_homeless_df = soda_chicago_df[
    soda_chicago_df["health_status"] == "At Risk"
    & soda_chicago_df["location"] == "Chicago"
    & soda_chicago_df["recent_activities"].str.contains("camping|hiking|animals")
]

# Collect samples from the at-risk homeless individuals
samples = []
for homeless_individual in at_risk_homeless_df.iterrows():
    sample = homeless_individual[1]["id"]
    samples.append(sample)

# Analyze the samples using PFGE
pfge_results = []
for sample in samples:
    pfge_result = pfge(sample)
    pfge_results.append(pfge_result)

# Identify the homeless individuals who are infected with E. coli O157:H7
infected_homeless_df = at_risk_homeless_df[
    at_risk_homeless_df["id"].isin(pfge_results)
    & pfge_results.apply(lambda x: x == "E. coli O157:H7")
]

# Print the results
print(infected_homeless_df)
