PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        print(new_letter)
        with open(f"./output/readytosend/letter_for_{stripped_name}.txt", "w") as finished_letter:
            finished_letter.write(new_letter)
