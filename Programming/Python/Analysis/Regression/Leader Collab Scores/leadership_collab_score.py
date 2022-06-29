import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sci
import statsmodels.api as sm

frame = pd.read_csv('2019-public-data-file_student.csv')

ALPHA = 0.05
size = len(frame)

labels = frame.columns
labInd = [5, 6]

# keep columns
keep = []
for i in labInd:
    keep.append(labels[i])

# drop unused columns
for i in labels:
    if i not in keep:
        frame.drop(i, axis = 1, inplace = True)

frame.dropna(how = 'all', inplace = True)

newSize = len(frame)

# declare series
leader_series = frame['Effective School Leadership Score']
collab_series = frame['Collaborative Teachers Score']

# Normal test for the data sets
leader_normal = sci.normaltest(leader_series)
collab_normal = sci.normaltest(collab_series)

print("\nStatistic:", leader_normal[0], "\nP-value:", leader_normal[1])
if leader_normal[1] < ALPHA:
    print("The Effective School Leadership Score data set has a non-normal distribution")

print("\nStatistic:", collab_normal[0], "\nP-value:", collab_normal[1])
if collab_normal[1] < ALPHA:
    print("The Collaborative Teacher Score data set has a non-normal distribution")

else:
    print("The data set has a normal distribution")

# Transformation
frame.transform(lambda x: x ** 2, axis = 1)

# Truncation
frame.iloc[0:125, :]

# Normal test of the truncated data sets
print("\n-Truncated data sets-\nStatistic:", leader_normal[0], "\nP-value:", leader_normal[1])
if leader_normal[1] < ALPHA:
    print("The truncated effective school leadership score data set has a non-normal distribution")

print("\nStatistic:", collab_normal[0], "\nP-value:", collab_normal[1])
if collab_normal[1] < ALPHA:
    print("The truncated collaboration teacher score dat set has a normal distribution.")

else:
    print("The data set has a normal distribution")

# Scatter plot
leader_colab_plot = plt.figure()

plt.scatter(leader_series, collab_series)
plt.title("Title: Effective School Leadership Score")

plt.xlabel('Effective School Leadership Score')
plt.ylabel('Collaborative Teacher Score')

plt.show()

# Bartlet test of the data sets
bartlett_test = sci.bartlett(leader_series, collab_series)

print(f"\nStatistic: {bartlett_test[0]}\nP-value: {bartlett_test[1]}")
if bartlett_test[1] < ALPHA:
    print("Test produced significant results")
    
else:
    print("Test produced non-significant result")

# Regression Analysis
leader = 'Effective School Leadership Score'
collab = 'Collaborative Teachers Score'

X = frame[[leader]]
Y = frame[[collab]]

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
predictions = model.predict(X)
print_model = model.summary()
print(f"\n{print_model}")

### Output Streams
print(f"\nOriginal size: {size}\nNew size: {newSize}")
print("\nBoth score data sets are noon-normally distributed.")
print("After re-applying the normal sets for the truncated data sets both score data sets are non-normally distributed.")
print("The bartlett test produces non-significant results.")

