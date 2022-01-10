import pandas as pd

# {new_key:new_value for (index, row) in df.iterrows()}
csv_data = pd.read_csv(r'E:\Coding World !!\Angela Yu Python\Python Practice\NATO Alphabet\nato_phonetic_alphabet.csv')
csv_dataframe = pd.DataFrame(csv_data)

#TODO 1. Create a dictionary in this format:
csv_dict = {row.letter : row.code for (index, row) in csv_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Please enter a word: ").upper()
phonetic_list = [csv_dict[letter] for letter in name]
print(phonetic_list)