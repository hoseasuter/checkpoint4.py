import numpy as np
import pandas as pd

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print("1. Original DataFrame:")
print(df)
print()

print("2. First three rows using head():")
print(df.head(3))
print()

df = df.dropna()
print("3. DataFrame after deleting rows with NaN values:")
print(df)
print()

print("4. Extract 'name' and 'score' columns:")
print(df[['name', 'score']])
print()

new_row = pd.DataFrame({
    'name': ['Suresh'],
    'score': [15.5],
    'attempts': [1],
    'qualify': ['yes']
}, index=['k'])

df = pd.concat([df, new_row])
print("5. DataFrame after appending new row 'k':")
print(df)
print()

df = df.drop(columns=['attempts'])
print("6. DataFrame after deleting the 'attempts' column:")
print(df)
print()

df['Success'] = df['score'].apply(lambda x: 1 if x > 10 else 0)
print("7. DataFrame after adding the 'Success' column:")
print(df)
