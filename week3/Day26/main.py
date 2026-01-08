import pandas

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index, row) in nato_alphabet_data.iterrows()}

def convert_to_nato():
    user_word = input("Enter a word: ").upper()
    try:
        if user_word == "":
            print("Sorry, you must enter a word")
            convert_to_nato()
        nato_list = [nato_alphabet[letter] for letter in user_word]
    except KeyError:
        print(f"sorry, {user_word} is not a valid word")
        convert_to_nato()
    else:
        print(nato_list)

convert_to_nato()