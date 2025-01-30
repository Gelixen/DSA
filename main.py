# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import json
from collections import Counter

def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # Reads the whole file as a single string
            print(content)  # Print the entire content
            return content
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def sort_word_counts(word_counts, sort_by="count", descending=True):
    if sort_by == "count":
        # Sort by count
        sorted_items = sorted(word_counts.items(), key=lambda item: item[1], reverse=descending)
    elif sort_by == "word":
        # Sort by word (alphabetically, case-insensitive)
        sorted_items = sorted(word_counts.items(), key=lambda item: item[0].lower(), reverse=descending)


if __name__ == "__main__":
    settings_file_path = "settings.json"
    settings_json = read_json_file(settings_file_path)

    if settings_json:
        print("Settings:")
        print(json.dumps(settings_json, indent=4))

        input_path = settings_json.get('inputPath')
        input_data = read_file(input_path)
        words = input_data.lower().split()
        word_counts = Counter(words)

        count_sort_order = settings_json.get('countOrder')
        sorted_words_count = sorted(word_counts.items(), key=lambda item: item[1], reverse=count_sort_order == "descending")
        length_sort_order = settings_json.get('lengthOrder')
        sorted_words_count_and_length = sorted(sorted_words_count, key=lambda item: len(item[0]), reverse=length_sort_order == "descending")

        for word, count in sorted_words_count_and_length:
            print(f"Word: {word} Length: {len(word)} Count: {count}")

        output_path = settings_json.get('outputPath')
        with open(output_path, 'w') as file:
            for word, count in sorted_words_count_and_length:
                file.write(f"Word: {word} Length: {len(word)} Count: {count}\n")