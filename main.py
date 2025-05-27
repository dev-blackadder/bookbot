from stats import word_count, character_frequency, sort_character_frequency
import sys

def get_books_text(filepath):
    with open(filepath) as file:
        text = file.read()
        return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_books_text(book_path)

    print(f"Word count: {word_count(text)}")
    
    freq_dict = character_frequency(text)
    sorted_freq = sort_character_frequency(freq_dict)
    
    print("Character frequency:")
    for item in sorted_freq:
        print(f"{item['char']}: {item['num']}")

main()