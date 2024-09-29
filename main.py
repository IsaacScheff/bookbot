def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        print_report(file_contents, file_path)

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

def print_report(text, file_name):
    print(f"Begin report for {file_name}")
    word_count = word_counter(text)
    print(f"{word_count} words in document\n")
    char_count = char_counter(text)

    #sort char_count by value https://docs.python.org/3/howto/sorting.html
    sorted_chars = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    for char in sorted_chars:
        if char.isalpha():
            print(f"The letter '{char}' is found {char_count[char]} times")
    print("\nEnd of report")

main()