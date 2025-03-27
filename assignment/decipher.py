import json
import pickle


def decipher_phrase(phrase, lexicon_filename, abc_filename):
    # todo: implement this function
    print(f'starting deciphering using {lexicon_filename} and {abc_filename}')

    # todo: due to possible difference in file encodings between operating systems, make sure to add
    #  utf8 encoding type when opening a file, as an example: with open(<file name>, 'r', encoding='utf8') as fin
    #  python developers plan to make utf8 a default at 3.15 - https://peps.python.org/pep-0686/

    result = {"status": 0, "orig_phrase": '', "K": -1}
    return result


# todo: fill in your student ids
students = {'id1': '000000000', 'id2': '000000000'}

if __name__ == '__main__':
    with open('config-decipher.json', 'r') as json_file:
        config = json.load(json_file)

    # note that lexicon.pkl is a serialized list of 10,000 most common English words
    result = decipher_phrase(config['secret_phrase'],
                             config['lexicon_filename'],
                             config['abc_filename'])

    assert result["status"] in {1, -1, 0}

    if result["status"] == 1:
        print(f'deciphered phrase: {result["orig_phrase"]}, K: {result["K"]}')
    elif result["status"] == -1:
        print("cannot decipher the phrase!")
    else:  # result["status"] == 0:
        print("empty phrase")
