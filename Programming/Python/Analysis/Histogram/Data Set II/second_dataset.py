import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sci

frame = pd.read_csv('DataSet_2.csv')

ALPHA = 0.05
size = len(frame)

### Local Variables
plot = plt.figure()
plt.hist(frame, bins = 89)
plot.show()

# Mean
mean = np.mean(frame)
mean_val = mean[0]

# Standard Deviation
std = np.std(frame)
std_val = std[0]

# Minimum value
minimum = np.min(frame)
min_val = minimum[0]

# Maximum value
maximum = np.max(frame)
max_val = maximum[0]

# Low value
low = mean_val - (3 * std_val)

# High value
high = mean_val - (3 * std_val)

### Quick Check
non_normal_check = True
if min_val <= low or max_val >= high:
    print("\nThe value falls within the interval, including non-normal distribution")
    non_normal_check = True

else:
    print("\nBoth values fall outside the interval, indicating distribution may be normal")
    non_normal_check = False

### Declare variables into series
print("\n- Kurtosis Series -")
kurt_score = pd.Series.kurtosis(frame)
kurt_val = kurt_score[0]
print("Kurtosis value: {kurt_val}")

print("\n- Skew Series -")
skew_score = pd.Series.skew(frame)
skew_val = skew_score[0]
print("Skew value: {skew_val}")

### Test measurements
print("\n- Kurtosis Test Score -")
kurt_test = sci.kurtosistest(frame)
kurt = kurt_test[0][0]
print(f"Kurtosis test score: {kurt}")

print("\n- Skew Test Score -")
skew_test = sci.skewtest(frame)
skew = skew_test[0][0]
print(f"Skew test score: {skew}")

### Tests
non_normal_test = True
if abs(skew_val) > 2 or abs(kurt_val) > 7:
    print("\nTest scores indicate non-normal distribution")
    non_normal_test = True

else:
    print("\nTest scores do not indicate noon-normal distribution")
    non_normal_test = False

if non_normal_check and non_normal_test:
    print("\nBoth tests conclude that distribution is non-normal")

else:
    print("\nBoth tests conclude that distribution is possibly normal")

### Output Streams
print("\nThe histogram does appear to resemble a normal distribution.")
print("Their skewness, kurtosis values and test scores seem to indicate a normal distribution.")
