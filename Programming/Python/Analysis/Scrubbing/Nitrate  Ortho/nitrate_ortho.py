import pandas as pd
import scipy.stats as sci
import matplotlib.pyplot as plt

frame = pd.read_csv('Harbor_Water_Quality.csv', low_memory = False)

# Columns that will only appear
labels = frame.columns
labInd = [51, 55]

# keep used labels
keep = []
for i in labInd:
    keep.append(labels[i])

# drop unused labels
for i in labels:
    if i not in keep:
        frame.drop(i, axis = 1, inplace = True)

### Constant Variables
ALPHA = 0.05
size = len(frame)

for i in range (0, size):
    try:
        frame.iat[i, 0] = float(frame.iat[i, 0])
        frame.iat[i, 1] = float(frame.iat[i, 1])
    except ValueError:
        frame.iat[i, 0] = None
        frame.iat[i, 1] = None

frame.dropna(axis = 0, thresh = None, subset = None, inplace = True)
newSize = len(frame)

# declare a series
nitrate_series = frame['Top Nitrate/Nitrite (mg/L)']
ortho_series = frame['Top Ortho-Phosphorus (mg/L)']

# scatter plot
plt.scatter(nitrate_series, ortho_series)

# Tests results
pearson_test = sci.pearsonr(nitrate_series, ortho_series)
spearman_test = sci.spearmanr(nitrate_series, ortho_series)

# Pearson test results
print('\nCorrelation Value:', pearson_test[0], '\nP-Value:', pearson_test[1])
if pearson_test[0] > 0.3 and pearson_test[0] < 1.0 and pearson_test[1] < ALPHA:
    print("The test supports the possibility that the variable values are colinear.")
else:
    print("The test does not support the possibility that the variable values are colinear.")
    
# Spearman test results
print('\nCorrelation Value:', spearman_test[0], '\nP-Value:', spearman_test[1])
if spearman_test[0] > 0.3 and spearman_test[0] < 1.0 and spearman_test[1] < ALPHA:
    print("The test supports the possibility that the variable values are monotonic, and not linear.")
else:
    print("The test does not support the possibility that the variable values are monotonic.")

### Output Streams RQ
print(f"\nOriginal size: {size}\nNew size: {newSize}")
print("\nThe two levels are colinearly related.")