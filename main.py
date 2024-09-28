def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        #word_count = word_counter(file_contents)
        #print(word_count)
        char_count = char_counter(file_contents)
        print(char_count)

def word_counter(text):
    count = len(text.split())
    return count

def char_counter(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()