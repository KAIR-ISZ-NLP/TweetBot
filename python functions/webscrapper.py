#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import numpy as np


def extract_desc_for_app(address):
    """Changes data type of 'Verdict' column to boolean.
    Args:
        address (str): Text in form of url, can be invalid
    Returns:
        str: Extracted text from provided address
    """
    try:
        x = BeautifulSoup(requests.get(address).text, 'html.parser')
    except:
        return "Invalid url"
    res = x.find_all(id="game-description-cnt")  # [0].find_all('p')
    d = str(res[0]).find('>Dodatkowe')
    kt = str(res[0]).find('>Kwestie')
    inne = str(res[0]).find('>Inne')
    lista = [d, kt, inne]
    if np.min(lista) == -1:
        if np.max(lista) == -1:
            return BeautifulSoup(str(res[0]), 'html.parser').get_text()
        else:
            min_ = min(list(map(lambda x: np.Inf if x == -1 else x, lista)))
            return BeautifulSoup(str(res[0])[0: min_], 'html.parser').get_text()
    else:
        return BeautifulSoup(str(res[0])[0: np.min(lista)], 'html.parser').get_text()


