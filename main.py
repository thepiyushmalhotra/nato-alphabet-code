import pandas as pd

csv_data = pd.read_csv(r'E:\Coding World !!\Angela Yu Python\Python Practice\NATO Alphabet\nato_phonetic_alphabet.csv')
csv_dataframe = pd.DataFrame(csv_data)

csv_dict = {row.letter : row.code for (index, row) in csv_dataframe.iterrows()}

name = input("Please enter a word: ").upper()
phonetic_list = [csv_dict[letter] for letter in name]
print(phonetic_list)
