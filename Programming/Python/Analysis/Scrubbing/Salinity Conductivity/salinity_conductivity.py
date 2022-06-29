import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sci

frame = pd.read_csv('Harbor_Water_Quality.csv', low_memory = False)

ALPHA = 0.05
size = len(frame)

# keep two columns
labels = frame.columns
labInd = [10, 12]

keep = []
for i in labInd:
    keep.append(labels[i])

# drop unused columns
for i in labels:
    if i not in keep:
        frame.drop(i, axis = 1, inplace = True)

### Constant Variables
for i in range (0, size):
    try:
        frame.iat[i, 0] = float(frame.iat[i, 0])
        frame.iat[i, 1] = float(frame.iat[i, 1])
    except ValueError:
        frame.iat[i, 0] = None
        frame.iat[i, 1] = None

frame.dropna(axis = 0, thresh = None, subset = None, inplace = True)
newSize = len(frame)

# declare series
salinity_series = frame['Top Salinity  (psu)']
conductivity_series = frame['Top Conductivity (S/m)']

# Scatter plot
plt.scatter(salinity_series, conductivity_series)

# Test results
pearson_test = sci.pearsonr(salinity_series, conductivity_series)
spearman_test = sci.spearmanr(salinity_series, conductivity_series)

# Pearson test result
print('\nCorrelation Value:', pearson_test[0], '\nP-Value:', pearson_test[1])
if pearson_test[0] > 0.3 and pearson_test[0] < 1.0 and pearson_test[1] < ALPHA:
    print("The test supports the possibility that the variable values are colinear.")
    
else:
    print("The test does not support the possibility that the variable values are colinear.")

# Spearman test result
print('\nCorrelation Value:', spearman_test[0], '\nP-Value:', spearman_test[1])
if spearman_test[0] > 0.3 and spearman_test[0] < 1.0 and spearman_test[1] < ALPHA:
    print("The test supports the possibility that the variable values are monotonic, and not linear.")

else:
    print("The test does not support the possibility that the variable values are monotonic.")

### Output Streams
print(f"\nOriginal size: {size}\nNew size: {newSize}")
print("\nThe two levels are monotonically and not linear.")
