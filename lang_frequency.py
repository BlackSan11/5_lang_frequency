

def load_data_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file_with_json:
        json_from_file = json.load(file_with_json)
        return json_from_file['features']


def get_most_frequent_words(text):
    pass


if __name__ == '__main__':
    pass
