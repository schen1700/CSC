import pandas as pd
import math
import matplotlib.pyplot as plt
import csv

# Indicates each csv file names inside a variable
plt.close('all')
file = 'file.csv'               # filename: DataNumbers.csv
path = 'file2.csv'              # filename: DataNum.csv
dframe = pd.read_csv(file)
frame = pd.read_csv(path)

### LOCAL SCALAR VARIABLES
# Finding the mean, square, difference, sum, sd, aand variance of Y values.
yMean = dframe['Y'].mean()
dframe['Diff'] = dframe['Y'] - yMean
dframe['Sqrt'] = dframe['Diff'].pow(2)
sumSqr = dframe['Sqrt'].sum()
var = sumSqr / (dframe['Y'].count() - 1)
std = math.sqrt(var)

# Finding the size, min, max, and median of Y values.
size = dframe['Y'].count()
minVal = dframe['Y'].min()
maxVal = dframe['Y'].max()
midVal = dframe['Y'].max()

### Output Streams
# Displays values for Y
print(f"Size: {size}")
print(f"Max: {round(maxVal, 2)}")
print(f"Min: {round(minVal, 2)}")
print(f"Mean: {round(yMean, 2)}")
print(f"Median: {round(midVal, 2)}")
print(f"Sum: {round(sumSqr, 2)}")
print(f"Variance: {round(var, 2)}")
print(f"Standard Deviation: {round(std, 2)}")

### Plot scatter
# dframe is lesser than the frame.
print("\nLooking at both plots visually, the top scatter plot and the bottom scatter plot are vastly different.")
print("Top plot's data, in reference to the y- axis are closer to the line of best fit and more condensed while the bottom is more spread out.")
print("Looking at the numbers, the variance of the bottom plot is greater by about 4 million.")
                  
dframe.plot.scatter(x = 'X', y = 'Y')
frame.plot.scatter(x = 'X', y = 'Y')
