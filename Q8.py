from collections import defaultdict
import re

def count_word_frequencies(file_path):
    word_count = defaultdict(int)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                words = re.findall(r'\b\w+\b', line)
                for word in words:
                    word_count[word] += 1
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
    final_word_count = {word: count for word, count in word_count.items()}

    return final_word_count

file_path = 'C:\\Users\\acer\\Desktop\\Programs\\Assignment-3PL\\text.txt'
word_frequencies = count_word_frequencies(file_path)

if word_frequencies:
    print(word_frequencies)