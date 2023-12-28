def main():
    path = "books/frankenstein.txt"
    print_report(path)


def get_file_contents(path):
    with open(path) as f:
        return(f.read())

def get_number_of_words(string):
    word_array = string.split()
    return( len(word_array) )

def get_number_of_characters(string):
    lower_case_string = string.lower()
    characters = {}
    for char in lower_case_string:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def print_report(path): 
    file_contents = get_file_contents(path)
    number_of_words = get_number_of_words(file_contents)
    number_of_characters = get_number_of_characters(file_contents)
    print(f"--- Begin report of {path} ---")
    print(f"{number_of_words} words found in the document")
    print("")
    characters = []
    for character_count in number_of_characters:
        character = character_count[0]
        if character.isalpha():
            characters.append(character)
    characters.sort()
    for character in characters:
        count = number_of_characters[character]
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")

main()
