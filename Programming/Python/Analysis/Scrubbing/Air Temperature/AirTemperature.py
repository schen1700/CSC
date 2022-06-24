import pandas as pd
import numpy as np
import scipy.stats as sci

frame = pd.read_csv('AutomatedSensors.csv')

ALPHA = 0.05
size = len(frame)

# Drop unused columns
A = 'Air Temperature'
B = 'Measurement Timestamp'
C = 'Station Name'

labels = [A, B, C]
for i in frame.columns:
    if i not in labels:
        frame.drop(i, axis = 1, inplace = True)

# Drop invalid valid
frame.dropna(axis = 0, how = 'any', thresh = None, subset = None, inplace = True)

# Set a column to NaN
frame.replace(['Air Temperature', np.nan])

# Split Timestamp into different columns
frame['Date'] = frame['Measurement Timestamp'].str.split(' ').str[-2]
frame[['Month', 'Day', 'Year']] = frame['Date'].str.split('/', expand = True)

# Filter assigned values
frame = frame[(frame['Month'] == '8') &
              (frame['Year'] == '2017')]

newSize = len(frame)

### Variable Declarations
stationName = frame['Station Name']
airTemps = frame['Air Temperature']
tempMean = np.mean(airTemps)

kurtScore = sci.kurtosistest(airTemps)
skewScore = sci.skewtest(airTemps)

streetTemps = []
fosterTemps = []
oakTemps = []

for i in range(len(frame)):
    if stationName.iloc[i] == '63rd Street Weather Station':
        streetTemps.append(airTemps.iloc[i])
    
    if stationName.iloc[i] == 'Foster Weather Station':
        fosterTemps.append(airTemps.iloc[i])
        
    if stationName.iloc[i] == 'Oak Street Weather Station':
        oakTemps.append(airTemps.iloc[i])

# ANOVA Test results
fTest = sci.f_oneway(streetTemps, fosterTemps, oakTemps)
print(f"\nStatistics: {fTest[0]}\nPvalue: {fTest[1]}")

barTest = sci.bartlett(streetTemps, fosterTemps, oakTemps)
print(f"\nStatistics: {barTest[0]}\nPvalue: {barTest[1]}")

if barTest[0] < ALPHA:
    print("\nThe test produces a significant outcome")
    print("WARNING! The analysis results may not be reliable due to heterogeneity between the test groups.")

else:
    print("\nThe test produces a non-significant outcome.")
    print("The variance is homogenic.")

groupMean = frame[['Station Name', 'Air Temperature']].groupby('Station Name').mean()
groupSize = frame[['Station Name', 'Air Temperature']].groupby('Station Name').size()

# Box plot for frame
frame.boxplot(by = 'Station Name', column = ['Air Temperature'], grid = False)

### Output Streams
print(f"\nOriginal number of data set tuples: {size}")
print(f"Final number of data set (n): {newSize}")

print(f"\nKurtosis Score: {kurtScore[0]}\nPvalue: {kurtScore[1]}")
print(f"\nSkew Score: {skewScore[0]}\nPvalue: {skewScore[1]}")

print("The test produces a non-significant outcome and the variance is homogenic.")
