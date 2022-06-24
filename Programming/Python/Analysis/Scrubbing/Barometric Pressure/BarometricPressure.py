import pandas as pd
import numpy as np
import scipy.stats as sci

frame = pd.read_csv('AutomatedSensors.csv')

ALPHA = 0.05
size = len(frame)

# Dropping unused columns
A = 'Station Name'
B = 'Measurement Timestamp'
C = 'Barometric Pressure'

labels = [A, B, C]
for i in frame.columns:
    if i not in labels:
        frame.drop(i, axis = 1, inplace = True)

# drop invalid values
frame.dropna(subset = ['Barometric Pressure'], inplace = True)

# split timestamp values into different columns
frame['Date'] = frame['Measurement Timestamp'].str.split(' ').str[-2]
frame[['Month', 'Day', 'Year']] = frame['Date'].str.split('/', expand = True)

# Filter two groups
frame = frame[(frame['Station Name'] == '63rd Street Weather Station') |
              (frame['Station Name'] == 'Oak Street Weather Station')]

# Filter assigned values
frame = frame[(frame['Month'] == '5') &
              (frame['Year'] == '2020')]

# update frame and size
newSize = len(frame)

### Test techniques
stationName = frame['Station Name']
baroPress = frame['Barometric Pressure']

kurtScore = sci.kurtosistest(baroPress)
skewScore = sci.skewtest(baroPress)
    
# Kurtosis Score Test
print(f"\nKurtosis Score: {kurtScore[0]}\nPvalue: {kurtScore[1]}")   
if kurtScore[1] < ALPHA:
    print("The test produced a significant outcome")

# Skew Score Test
print(f"\nSkew Score: {skewScore[0]}\nPvalue: {skewScore[1]}")
if skewScore[1] < ALPHA:
    print("The test produced a significant outcome")

else:
    print("The tests produced a non-significant outcome")

# Score tests are greater than ALPHA
if kurtScore[1] > ALPHA and skewScore[1] > ALPHA:
    print("\nBoth test produced non-significant results and the parametrics are indicated.")

else:
    print("\nAt least one test produced a significant results and parametrics are not indicated.")

### Barometric Pressure tests
# arrays between two groups
srdPress = []
oakPress = []

for i in range(newSize):
    if stationName.iloc[i] == '63rd Street Weather Station':
        srdPress.append(baroPress.iloc[i])
    if stationName.iloc[i] == 'Oak Street Weather Station':
        oakPress.append(baroPress.iloc[i])

tScore = sci.ttest_ind(srdPress, oakPress)
print(f"\nTest statistic: {tScore[0]}\nPvalue: {tScore[1]}")

if tScore[1] < ALPHA:
    print("The test produced a significant outcome")
else:
    print("The test produced a non-significant outcome")

# get the mean between two groups
srdMean = np.mean(srdPress)
oakMean = np.mean(oakPress)
print(f"\n63rd Street Weather Station: {srdMean}\nOak Street Weather Station: {oakMean}")

### Output Streams
print(f"\nOriginal Size: {size}\nNew Size: {newSize}")
print("\nThe barometric pressure test bewteen the two groups produced a non-significant outcome for May 2020.")