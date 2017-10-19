import re
import collections
import argparse


def create_args_parser():
    parser = argparse.ArgumentParser(
        description='Get top 10 of most frequent using word of text')
    parser.add_argument("path",
                        help="Plese input your path to analyze text file")
    return parser


def load_text_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file_with_text:
        text = file_with_text.read()
        return text


def get_most_frequent_words(text):
    all_words_list = re.split('\W+', text)
    counter_all_words = collections.Counter()
    for word in all_words_list:
        if re.search('\d+', word) or word == '':
            continue
        counter_all_words[word] += 1
    top_of_most_frequent_words = counter_all_words.most_common(NUBER_OF_TOP)
    total_number_of_words = len(counter_all_words)
    return top_of_most_frequent_words, total_number_of_words


if __name__ == '__main__':
    # количество слов в топе
    NUBER_OF_TOP = 10
    # создаем парсер и получаем аргумент path
    args_parser = create_args_parser()
    args = args_parser.parse_args()
    # получаем топ 10 самых часто употребляемых слов в тексте
    top_words_in_text, total_number_of_words = get_most_frequent_words(
        load_text_from_file(args.path))
    if len(top_words_in_text) != 0:
        print("В тексте {} слов, вот самые часто встречающиеся из них:".format(
            total_number_of_words))
        for key in top_words_in_text:
            print('Слово :"{}" употребляеться: {} раз(а)'.format(key[0],
                                                                 key[1]))
    else:
        print("Файл {} пуст".format(args.path))
