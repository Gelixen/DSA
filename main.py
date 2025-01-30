import json
from collections import Counter

SETTINGS_FILE_PATH = 'settings.json'

INPUT_PATH_KEY = 'inputPath'
OUTPUT_PATH_KEY = 'outputPath'
LENGTH_ORDER_KEY = 'lengthOrder'
COUNT_ORDER_KEY = 'countOrder'


def read_json_file(file_path: str):
    try:
        with open(file_path) as file:
            return json.load(file)
    except FileNotFoundError:
        print('Error: File not found.')
    except json.JSONDecodeError:
        print('Error: Invalid JSON format.')


def read_text_file(file_path: str):
    try:
        with open(file_path) as file:
            return file.read()
    except FileNotFoundError:
        print('Error: File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')


def write_to_file(file_path: str, sorted_words_with_count: list[tuple[str, int]]):
    try:
        with open(file_path, 'w') as file:
            for word, count in sorted_words_with_count:
                file.write(f'Word: {word} Length: {len(word)} Count: {count}\n')
    except FileNotFoundError:
        print('Error: File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    settings_json = read_json_file(SETTINGS_FILE_PATH)

    if settings_json:
        input_path = settings_json.get(INPUT_PATH_KEY)
        input_data = read_text_file(input_path)
        words = input_data.lower().split()
        words_with_count = Counter(words)

        count_sort_order = settings_json.get(COUNT_ORDER_KEY)
        words_with_count_sorted_by_count = sorted(words_with_count.items(),
                                                  key=lambda item: item[1],
                                                  reverse=count_sort_order == 'descending')

        length_sort_order = settings_json.get(LENGTH_ORDER_KEY)
        words_with_count_sorted_by_count_and_length = sorted(words_with_count_sorted_by_count,
                                                             key=lambda item: len(item[0]),
                                                             reverse=length_sort_order == 'descending')

        output_path = settings_json.get(OUTPUT_PATH_KEY)
        write_to_file(output_path, words_with_count_sorted_by_count_and_length)
