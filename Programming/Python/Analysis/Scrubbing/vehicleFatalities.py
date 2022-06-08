import pandas as pd
import scipy.stats as sci

frame = pd.read_csv('file.csv')         # Filename: MotorVehicleCrashes.csv

ALPHA = 0.05
size = len(frame)

# Dropping unused columns
A = 'Seating Position'
B = 'Sex'
C = 'Injury Severity'
D = 'Age'

labels = [A, B, C, D]
for i in frame.columns:
    if i not in labels:
        frame.drop(i, axis = 1, inplace = True)

# Removing entries related to non-drivers
frame = frame[frame['Seating Position'] == 'Driver']

# Removing entries with invalid gender values
frame.rename(columns = {'Sex': 'Gender'}, inplace = True)
frame = frame[(frame['Gender'] == 'F') |
              (frame['Gender'] == 'M')]

# Removing entries with unknown injury severity values
frame = frame[(frame['Injury Severity'] == 'Uninjured') |
                    (frame['Injury Severity'] == 'Minor') |
                    (frame['Injury Severity'] == 'Moderate') |
                    (frame['Injury Severity'] == 'Severe')]

new_size = len(frame)

# Analysis Approach
# All analysis will use categorical or ordinal values
# Nonparametric analysis techniques will be used
seatPos = frame['Seating Position']
caseGen = frame['Gender']
caseSev = frame['Injury Severity']
caseAge = frame['Age']

num_female = 0
num_male = 0

for i in range(new_size):
    if caseGen.iloc[i] == "M":
        num_male += 1
    elif caseGen.iloc[i] == "F":
        num_female += 1

fem_cal = int((num_female / new_size * 100))
male_cal = int((num_male / new_size * 100))

print("\nCases:")
print("Males", num_male, ', %.2f' % male_cal, '%')
print("Females", num_female, ', %.2f' % fem_cal, '%')

### Binomial Test
# Invoke binomial test
binomTest = sci.binom_test(num_male, new_size, 0.05)

# Comparing binomial against ALPHA
if binomTest < ALPHA:
    print("Not fair")
else:
    print("Equal change")

### Chi-squared Test
# Array of the integer values
male_arr = [0, 0, 0, 0]
fem_arr = [0, 0, 0, 0]

# First and Second Sub-array in the table for both genders
for i in range(new_size):
    if caseGen.iloc[i] == "M":
        if caseSev.iloc[i] == "Uninjured":
            male_arr[0] += 1
        elif caseSev.iloc[i] == "Minor":
            male_arr[1] += 1
        elif caseSev.iloc[i] == "Moderate":
            male_arr[2] += 1
        elif caseSev.iloc[i] == "Severe":
            male_arr[3] += 1
    
    elif caseGen.iloc[i] == "F":
        if caseSev.iloc[i] == "Uninjured":
            fem_arr[0] += 1
        elif caseSev.iloc[i] == "Minor":
            fem_arr[1] += 1
        elif caseSev.iloc[i] == "Moderate":
            fem_arr[2] += 1
        elif caseSev.iloc[i] == "Severe":
            fem_arr[3] += 1

# Builds the 2D array and examines the results            
sev_arr = [male_arr, fem_arr]
sev_test = sci.chi2_contingency(sev_arr)

print(f"Chi-squared: {sev_test}")       
            
### Output Streams
print(f"\nOriginal data set tuples: {size}\nFinal data after scrubbing: {new_size}")

print("\nThe original size of the data contains about a million than the new size.")
print("Which concludes the data scrubbing is complete.")
print("After performing an analysis approach, all analysis use categorical or ordinal values.")
print("The non-parametric techniques will be used.")
print("The statistical analysis base on both gender results, males have higher percentage than females in vehicle crashes")
print("62% for males, whereas 37% for females.")
print("The ratio for the binomial test of observed frequencies of male versus female drivers in accidents are 1.65 M : 1 F")
print("The comparison of the results between binomial test and ALPHA is not fair.")            
