import json
import pickle
import os

ABLE_TO_DECIPHER = 1
NOT_ABLE_TO_DECIPHER = -1
EMPTY_PHRASE = 0


def decode_char(current_char: chr, k: int, letters: list[chr]):
    """
    Decodes a single character using a decipher_phrase shift.
    Input:
       current_char (str): A single character to decode.
       k (int): The cipher shift value.
       letters (list): A list of all possible letters.
    Output:
       str: The decoded character (or the same character if it's not in the alphabet).
    """
    if current_char not in letters:
        return current_char  # leave space and other non-alphabet characters unchanged
    index = (letters.index(current_char) + k) % len(letters)  # circular shift in the alphabet
    return letters[index]


def try_all_possible_shifts(letters: list[chr], phrase: str, lexicon: set[str]) -> dict | None:
    """
        Attempts to decode a phrase by trying all shifts and checking for valid words.
        Input:
            letters (list[chr]): List of valid characters used for encoding.
            phrase (str): Encoded phrase to decode.
            lexicon (set[str]): Set of valid words to verify decoding.
        Output:
            dict | None: Returns a dict with 'status', 'orig_phrase', and 'K' if decoding is successful, else None.
        """
    for k in range(len(letters)):
        decoded = ''.join(decode_char(current_char, k, letters) for current_char in phrase)
        words = decoded.split()

        # Check if all decoded words exist in the lexicon
        if all(word in lexicon for word in words):
            return {
                'status': ABLE_TO_DECIPHER,
                'orig_phrase': decoded,
                'K': k
            }


def decipher_phrase(phrase: str, lexicon_filename: str, abc_filename: str):
    """
     Deciphers a phrase by trying all possible shifts.
     Input:
         phrase (str): The encoded phrase to be deciphered.
         lexicon_filename (str): The path to a pickle file containing a list of valid English words.
         abc_filename (str): The path to a text file containing the alphabet characters (one per line).
     Output:
         dict: A dictionary with the keys:
             - 'status': int (1 if deciphered successfully, -1 if failed, 0 if phrase is empty)
             - 'orig_phrase': str (the deciphered phrase, if successful)
             - 'K': int (the shift value used, if successful; otherwise -1)
     """
    # If the phrase is empty or just spaces, return status 0
    result = {"status": EMPTY_PHRASE, "orig_phrase": phrase, "K": -1}
    if not phrase.strip():
        return result

    # Check that input files exist
    if not os.path.exists(lexicon_filename):
        print(f'Error: file {lexicon_filename} not found.')
        exit(1)
    if not os.path.exists(abc_filename):
        print(f'Error: file {abc_filename} not found.')
        exit(1)

    # Load alphabet from file (one character per line)
    with open(abc_filename, 'r', encoding='utf8') as abc_file:
        letters = [line.strip() for line in abc_file if line.strip()]

    # Load the English lexicon (a set of valid words)
    with open(lexicon_filename, 'rb') as lexicon_file:
        lexicon = set(pickle.load(lexicon_file))

    result = try_all_possible_shifts(letters, phrase, lexicon)
    # If no valid decoding found, return status -1
    if result['K'] == -1:
        result['status'] = NOT_ABLE_TO_DECIPHER
    return result


students = {'id1': '208077214', 'id2': '207080185'}

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
