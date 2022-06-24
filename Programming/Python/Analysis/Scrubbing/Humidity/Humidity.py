import pandas as pd
import numpy as np
import scipy.stats as sci

frame = pd.read_csv('AutomatedSensors.csv')

ALPHA = 0.05
size = len(frame)

# Drop unused columns
A = 'Station Name'
B = 'Humidity'

labels = [A, B]
for i in frame.columns:
    if i not in labels:
        frame.drop(i, axis = 1, inplace = True)

# drop invalid values
frame.dropna(axis = 0, how = 'any', thresh = None, subset = ['Humidity'], inplace = True)

newSize = len(frame)

### Variable Declarations
stationName = frame['Station Name']
humidVal = frame['Humidity']
humidMean = np.mean(humidVal)
humidStd = np.std(humidVal)

highVal = humidMean + (3 * humidStd)
lowVal = humidMean + (3 * humidStd)

highGap = np.abs(highVal - humidMean)
lowGap = np.abs(lowVal - humidMean)

checkVal = 2 * humidStd

# Quick Check
if (highGap <= checkVal and lowGap > checkVal) or (highGap > checkVal and lowGap <= checkVal):
    print("\nThe quick check has failed")
    print("The data set is notably skewed, and is therefore non-normally distributed")

else:
    print("\nThe quick check is successful")

### Test Analysis
# Score Tests
kurtScore = sci.kurtosistest(humidVal)
print(f"\nKurtosis Score: {kurtScore[0]}\nPvalue: {kurtScore[1]}")

skewScore = sci.skewtest(humidVal)
print(f"\nSkew Score: {skewScore[0]}\nPvalue: {skewScore[1]}")

if skewScore[1] < ALPHA or kurtScore[1] < ALPHA:
    print("\nEither test produced a significant outcome")
    print("The test indicates a non-parametric technique")

else:
    print("\nThe test produced a non-significant outcome")
    print("The test indicate a parametric technique")

streetVal = []
fosterVal = []
oakVal = []

for i in range(len(frame)):
    if stationName.iloc[i] == '63rd Street Weather Station':
        streetVal.append(humidVal.iloc[i])
    
    if stationName.iloc[i] == 'Foster Weather Station':
        fosterVal.append(humidVal.iloc[i])
    
    if stationName.iloc[i] == 'Oak Street Weather Station':
        oakVal.append(humidVal.iloc[i])

# Levene Test
levTest = sci.levene(streetVal, fosterVal, oakVal)
print(f"\nStatistics: {levTest[0]}\nPvalue: {levTest[1]}")

if levTest[1] < ALPHA:
    print("\nThe test produces a significant outcome")
    print("WARNING! The analysis results may not be reliable due to heterogenic variances between test groups")

else:
    print("\nThe test produces a non-siginificant outcome")
    print("The variance is homogenic")

# Kruskal Test
krusTest = sci.kruskal(streetVal, fosterVal, oakVal)
print(f"\nStatistics: {krusTest[0]}\nPvalue: {krusTest[1]}")

if krusTest[1] < ALPHA:
    print("The test produces a sginificant outcome")

else:
    print("The test produces a non-significant outcome")

Hmean = frame[['Station Name', 'Humidity']].groupby('Station Name').mean()
Hmid = frame[['Station Name', 'Humidity']].groupby('Station Name').median()

# Box plot
frame.boxplot(by = 'Station Name', column = ['Humidity'], grid = False)

### Output Streams
print(f"\nOriginal Size: {size}\nNew Size: {newSize}")
print("\nThe tests produced a significant outcome across the entire data collection period.")
