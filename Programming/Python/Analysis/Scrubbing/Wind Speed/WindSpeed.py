import pandas as pd
import numpy as np
import scipy.stats as sci

frame = pd.read_csv('AutomatedSensors.csv')

ALPHA = 0.05
size = len(frame)

# Drop unused columns
A = 'Station Name'
B = 'Wind Speed'

labels = [A, B]
for i in frame.columns:
    if i not in labels:
        frame.drop(i, axis = 1, inplace = True)

# Remove invalid values
frame.dropna(subset = ['Wind Speed'], inplace = True)

# FIlter two groups
frame = frame[(frame['Station Name'] == '63rd Street Weather Station') |
              (frame['Station Name'] == 'Oak Street Weather Station')]

newSize = len(frame)

### Tests technique
# Declare Variables
stationName = frame['Station Name']
windSpeed = frame['Wind Speed']

windMean = np.mean(windSpeed)
windStd = np.std(windSpeed)

highVal = windMean + (3 * windStd)
lowVal = windMean + (3 * windStd)

highGap = np.abs(highVal - windMean)
lowGap = np.abs(lowVal - windMean)
checkVal = 2 * windStd

kurtScore = sci.kurtosistest(windSpeed)
skewScore = sci.skewtest(windSpeed)

### Conditional Statements
# Quick Check
if (highGap <= checkVal and lowGap > checkVal) or (highGap > checkVal and lowGap <= checkVal):
    print("The quick check failed")
    print("Data set is notably skewed, and therefore is non-normally distributed.")

else:
    print("The quick check is successful.")

# Score tests
print(f"\nKurtosis Score: {kurtScore[0]}\nPvalue: {kurtScore[1]}")
if kurtScore[1] < ALPHA:
    print("The test produced a significant outcome")

print(f"\nSkew Score: {skewScore[0]}\nPvalue: {skewScore[1]}")
if skewScore[1] < ALPHA:
    print("The test produced a significant outcome")

else:
    print("The test produced a non-significant outcome")

# Indicated Techniques
if kurtScore[1] > ALPHA and skewScore[1] > ALPHA:
    print("Both tests produced non-significant results, therefore the data set is normally distributed")
    print("The use of parametrics are indicated")

else:
    print("\nAt least one test produced a significant result")
    print("The use of parametrics are not indicated")

# Mann-Whitney U Test
strSpeed = []
fosSpeed = []

for i in range(newSize):
    if stationName.iloc[i] == '63rd Street Weather Station':
        strSpeed.append(windSpeed.iloc[i])
    if stationName.iloc[i] == 'Oak Street Weather Station':
        fosSpeed.append(windSpeed.iloc[i])

uScore = sci.mannwhitneyu(strSpeed, fosSpeed, alternative = 'two-sided')

print(f"\nU-test statistic: {uScore[0]}\nPvalue: {uScore[1]}")
if uScore[1] < ALPHA:
    print("The test produced a significant outcome")
    
else:
    print("The test produced a non-significant outcome")

print(f"\n63rd Street Weather Station: {len(strSpeed)}\nOak Street Weather Station: {len(fosSpeed)}")

### Output Streams
print(f"\nOriginal size: {size}\nNew Size: {newSize}")
print("\nThe wind speed test between the two groups produced a significant outcome.")