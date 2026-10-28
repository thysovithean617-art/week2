import pandas as pd

# --- Task 1: Average of a 'Score' column in a pandas DataFrame ---
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 78]}
df = pd.DataFrame(data)  # pandas DataFrame constructor

average_score = df['Score'].mean()  # pandas .mean() method
print("Average Score:", average_score)

# --- Task 2: Capitalize the first letter of every word in a sentence ---
sentence = "python is a great programming language"

capitalized_sentence = sentence.title()  # built-in str .title() method
print("Capitalized Sentence:", capitalized_sentence)

# --- Task 3: Loop through a 3-item list and print each item with the correct index ---
items = ["apple", "banana", "cherry"]

for index, item in enumerate(items):  # built-in enumerate() function
    print(f"Index {index}: {item}")   # indexes start at 0