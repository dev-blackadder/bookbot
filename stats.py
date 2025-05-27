def word_count(text):
    words = text.split()
    return len(words)

def character_frequency(text):
    freq = {}
    for char in text.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def sort_character_frequency(freq_dict):
    freq_list = [
        {"char": char, "num": count}
        for char, count in freq_dict.items() if char.isalpha()
    ]
    freq_list.sort(key=lambda x: x["num"], reverse=True)
    return freq_list