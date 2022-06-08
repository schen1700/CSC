import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sci

frame = pd.read_csv('file.csv')          # Filename: DataSet.csv

# Lets quickcheck if the min and max values fall within the internal,
# or outside the interval indicating distribution may be normal.
plot1 = plt.figure(1)
plt.hist(frame, bins = 89)
plot1.show()

# mean
mean = np.mean(frame)
mean_val = mean[0]

# standard deviation
std = np.std(frame)
std_val = std[0]

# minimum
minS = np.std(frame)
min_val = minS[0]

# maximum
maxS = np.max(frame)
max_val = maxS[0]

# lower and higher
low = mean_val - (3 * std_val)
high = mean_val - (3 * std_val)

# Quick Check
nonNorm_quickCheck = True
if min_val <= low or max_val >= high:
    print("\nIndicates a non-normal distribution, the minimum or maximum value falls within the interval.")
    nonNorm_quickCheck = True
else:
    print("\nDistribution may be normal, the minimum and maximum value falls outside the interval.")
    nonNorm_quickCheck = False

# Declare kurtosis variab;e into series
kurt = pd.Series.kurtosis(frame)
kurt_val = kurt[0]
print(f"\nKurtosis: {round(kurt_val, 2)}")

# Declare skew variable into series
skew = pd.Series.kurtosis(frame)
skew_val = skew[0]
print(f"\nSkew: {round(skew_val, 2)}")

# Test kurtosis measurements
kurt_score = sci.kurtosistest(frame)
kurtS = kurt_score[0][0]
print(f"\nKurtosis test score: {kurt_score}")

# Test skew measurements
skew_score = sci.skewtest(frame)
skewS = skew_score[0][0]
print(f"\nSkew test score: {skew_score}")

# Score Test
nonNorm_scoreTest = True
if abs(skew_val) > 2 or abs(kurt_val) > 7:
    print("\nTest scores indicate a non-normal distribution")
    nonNorm_scoreTest = scoreTest = True
else:
    print("\nTest scores do not indicate a non-normal distribution")
    nonNorm_scoreTest = scoreTest = False

if nonNorm_quickCheck and nonNorm_scoreTest:
    print("\nBoth tests conclude that distribution is non-normal")
else:
    print("\nBoth tests conclude that distribution is possibly normal")

### Output Streams
print("\nThe histogram does appear to resemble a normaal distribution.")
print("Its skewness and kurtosis values seem to indicate a normal distribution.")