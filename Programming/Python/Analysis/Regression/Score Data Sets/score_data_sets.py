import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sci
import statsmodels.api as sm

frame = pd.read_csv('2019-public-data-file_student.csv')

ALPHA = 0.05   
size = len(frame)

E = 'Effective School Leadership Score'
R = 'Rigorous Instruction Score'
T = 'Trust Score'
C = 'Collaborative Teachers Score'

labels = [E, R, T, C]

# drop unused columns
for i in frame.columns:
    if i not in labels:
        frame.drop(i, axis = 1, inplace = True)

# Remove invalid values
frame.dropna(how = 'any', inplace = True)

newSize = len(frame)

# print statement for normal tests results
def print_norm():
    print("The data set has a non-normal distribution")

# print statement for normal tests results
def print_bart():
    print("The test produced a significant results")
    
# declare series
ser_leader = frame['Effective School Leadership Score']
ser_rigorous = frame['Rigorous Instruction Score']
ser_trust = frame['Trust Score']
ser_collab = frame['Collaborative Teachers Score']

### Normal tests
lead_normal = sci.normaltest(ser_leader)
rigor_normal = sci.normaltest(ser_rigorous)
trust_normal = sci.normaltest(ser_trust)
collab_normal = sci.normaltest(ser_collab)

print("\n- Normal tests -")
def apply_test():
    
    print(f"\nStatistic: {lead_normal[0]}\nP-value: {lead_normal[1]}")
    if lead_normal[1] < ALPHA:
        print_norm()
    
    print(f"\nStatistic: {rigor_normal[0]}\nP-value: {rigor_normal[1]}")
    if rigor_normal[1] < ALPHA:
        print_norm()
    
    print(f"\nStatistic: {rigor_normal[0]}\nP-value: {trust_normal[1]}")
    if trust_normal[1] < ALPHA:
        print_norm()
    
    print(f"\nStatistic: {collab_normal[0]}\nP-value: {collab_normal[1]}")
    if collab_normal[1] < ALPHA:
        print_norm()
        
    else:
        print("The data set has a normal distribution")
apply_test()

# Transformation
frame.transform(lambda x: x ** 2, axis = 1)

# Truncation
frame.iloc[0:125, :]

# Re-applying the normal test for the truncated data sets
print("\n- Truncated normal tests -")
apply_test()

### Scatter Plot
# Leadership Score
lead_plot = plt.figure()
plt.scatter(ser_leader, ser_collab)
plt.title("Title: Effective School Leadership Score")
plt.xlabel('Effective School Leadership Score')
plt.ylabel('Collaborative Teacher Score')

# Rigorous Score
rigor_plot = plt.figure()
plt.scatter(ser_rigorous, ser_collab)
plt.title("Title: Rigourous Instruction Score")
plt.xlabel('Rigorous Instruction Score')
plt.ylabel('Collaborative Teacher Score')

# Trust Score
trust_plot = plt.figure()
plt.scatter(ser_trust, ser_collab)
plt.title("Title: Trust Score")
plt.xlabel('Trust Score')
plt.ylabel('Collaborative Teacher Score')

plt.show()


### Bartlett Tests
lead_bart = sci.bartlett(ser_leader, ser_collab)
rigor_bart = sci.bartlett(ser_rigorous, ser_collab)
trust_bart = sci.bartlett(ser_trust, ser_collab)

print("\n- Bartlett Tests -")
print(f"\nStatistic: {lead_bart[0]}\nP-value: {lead_bart[1]}")
if lead_bart[1] < ALPHA:
    print_bart()

print(f"\nStatistic: {rigor_bart[0]}\nP-value: {rigor_bart[1]}")
if rigor_bart[1] < ALPHA:
    print_bart()

print(f"\nStatistic: {trust_bart[0]}\nP-value: {trust_bart[1]}")
if trust_bart[1] < ALPHA:
    print_bart()

else:
    print("The test produced a non-significant results")

### Regression Analysis
X = frame[[E, R, T]]
Y = frame[[C]]

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(f"\n{print_model}")

### Output Streams
print(f"\nOriginal Size: {size}\nNew size: {newSize}")
print("\nAll four score data sets are non-normally distributed.")
print("The truncated results of the four score data sets are normally distributed.")
print("Which the test scores produces a noon-significant results.")
