def count_words(text):
    return len(text.split())

def character_count(text):
    char_object = {}

    for char in text:
        char = char.lower()

        if char not in char_object:
            char_object[char] = 1
        else:
            char_object[char] += 1

    return char_object

def main():
    file_path = 'books/frankenstein.txt'

    with open(file_path, 'r') as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_object = character_count(file_contents)
        print(f'--- Begin report of {file_path} ---')
        print(f'{word_count} words found in the document \n')

        banned_chars = [' ', '.', '#']

        for key in char_object.keys():
            if key in banned_chars:
                continue
            print(f"The '{key}' character was found {char_object[key]} times")

        print('--- End report ---')

main()
