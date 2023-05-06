import numpy as np
import pandas as pd

# Load the data
data = pd.read_csv('faod_data.csv')

# Extract the relevant columns
fatty_acids = data['fatty_acids']
amino_acids = data['amino_acids']
ammonia = data['ammonia']

# Calculate the mean and standard deviation of each column
fatty_acids_mean = np.mean(fatty_acids)
fatty_acids_std = np.std(fatty_acids)
amino_acids_mean = np.mean(amino_acids)
amino_acids_std = np.std(amino_acids)
ammonia_mean = np.mean(ammonia)
ammonia_std = np.std(ammonia)

# Calculate the z-scores for each column
fatty_acids_zscore = (fatty_acids - fatty_acids_mean) / fatty_acids_std
amino_acids_zscore = (amino_acids - amino_acids_mean) / amino_acids_std
ammonia_zscore = (ammonia - ammonia_mean) / ammonia_std

# Create a new DataFrame with the z-scores
zscores = pd.DataFrame({'fatty_acids_zscore': fatty_acids_zscore,
                          'amino_acids_zscore': amino_acids_zscore,
                          'ammonia_zscore': ammonia_zscore})

# Identify any rows with z-scores that are greater than 2 standard deviations from the mean
outliers = zscores[(zscores['fatty_acids_zscore'] > 2) | (zscores['amino_acids_zscore'] > 2) | (zscores['ammonia_zscore'] > 2)]

# Print the results
print(outliers)
