def count_word_frequency(text):
    text = text.lower()
    punctuation_chars = ".,?!;:'\"()[]{}"
    for char in punctuation_chars:
        text = text.replace(char, "")
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency
if __name__ == "__main__":
    user_input = input("Enter a text: ")
    frequencies = count_word_frequency(user_input)
    print("\nWord Frequency:")
    for word, count in frequencies.items():
        print(f"{word}: {count}")
