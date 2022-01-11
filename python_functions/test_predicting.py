#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import predicting
import numpy


class MyTestCase(unittest.TestCase):
    def test_text_cleaner(self):
        tekst = "W grze Agatha Christie - Hercule Poirot: The First Cases trafiamy do przedwojennej Belgii i wcielamy się w Herkulesa Poirota w przededniu jego detektywistycznej kariery. Pewnego dnia protagonista otrzymuje zaproszenie na przyjęcie zorganizowane przez wpływową rodzinę Van den Bosch z okazji zaręczyn córki. Bal, na który przybywa również nasz podopieczny, przebiega w najlepsze... do momentu, kiedy jeden z gości zostaje zamordowany. Poirotowi nie pozostaje nic innego, jak przeprowadzić śledztwo mające na celu odkrycie tożsamości sprawcy. Niejako przy okazji detektyw trafia na ślad licznych tajemnic rodziny Van den Bosch i jej rywali. W Agatha Christie - Hercule Poirot: The First Cases akcję obserwujemy z lotu ptaka. Motorem gry jest dochodzenie prowadzone przez bohatera. W trakcie zabawy przemierzamy więc lokacje i przesłuchujemy różnorodne postacie. Szybko przekonujemy się, że prowadzenie takich rozmów nie jest łatwe, gdyż wszyscy mają tutaj coś do ukrycia i niemal każdy zachowuje się podejrzanie. Ponadto musimy uważnie rozglądać się po lokacjach, szukając rozmaitych wskazówek, które mogą naprowadzić nas na prawdziwy trop. Jako że z czasem zaczynamy gromadzić coraz więcej cennych informacji, musimy często zaglądać na specjalną mapę myśli, która pozwala porządkować zdobyte wskazówki i łączyć je ze sobą przy użyciu talentu dedukcji Poirota. W ten sposób w miarę postępów nie tylko dojdziemy do tego, kto stał za morderstwem, lecz również odkryjemy inne podejrzane sprawy wymagające rozwiązania."
        result = predicting.text_cleaner(tekst, 1)
        poprawny_tekst = "grze agatha christie hercule poirot the first cases trafiamy do przedwojennej belgii wcielamy się herkulesa poirota przededniu jego detektywistycznej kariery pewnego dnia protagonista otrzymuje zaproszenie na przyjęcie zorganizowane przez wpływową rodzinę van den bosch okazji zaręczyn córki bal na który przybywa również nasz podopieczny przebiega najlepsze do momentu kiedy jeden gości zostaje zamordowany poirotowi nie pozostaje nic innego jak przeprowadzić śledztwo mające na celu odkrycie tożsamości sprawcy niejako przy okazji detektyw trafia na ślad licznych tajemnic rodziny van den bosch jej rywali agatha christie hercule poirot the first cases akcję obserwujemy lotu ptaka motorem gry jest dochodzenie prowadzone przez bohatera trakcie zabawy przemierzamy więc lokacje przesłuchujemy różnorodne postacie szybko przekonujemy się że prowadzenie takich rozmów nie jest łatwe gdyż wszyscy mają tutaj coś do ukrycia niemal każdy zachowuje się podejrzanie ponadto musimy uważnie rozglądać się po lokacjach szukając rozmaitych wskazówek które mogą naprowadzić nas na prawdziwy trop jako że czasem zaczynamy gromadzić coraz więcej cennych informacji musimy często zaglądać na specjalną mapę myśli która pozwala porządkować zdobyte wskazówki łączyć je ze sobą przy użyciu talentu dedukcji poirota ten sposób miarę postępów nie tylko dojdziemy do tego kto stał za morderstwem lecz również odkryjemy inne podejrzane sprawy wymagające rozwiązania"
        self.assertEqual(type(result), str)
        self.assertEqual(result, poprawny_tekst)

    def test_prepare_text(self):
        tekst = "W grze Agatha Christie - Hercule Poirot: The First Cases trafiamy do przedwojennej Belgii i wcielamy się w Herkulesa Poirota w przededniu jego detektywistycznej kariery. Pewnego dnia protagonista otrzymuje zaproszenie na przyjęcie zorganizowane przez wpływową rodzinę Van den Bosch z okazji zaręczyn córki. Bal, na który przybywa również nasz podopieczny, przebiega w najlepsze... do momentu, kiedy jeden z gości zostaje zamordowany. Poirotowi nie pozostaje nic innego, jak przeprowadzić śledztwo mające na celu odkrycie tożsamości sprawcy. Niejako przy okazji detektyw trafia na ślad licznych tajemnic rodziny Van den Bosch i jej rywali. W Agatha Christie - Hercule Poirot: The First Cases akcję obserwujemy z lotu ptaka. Motorem gry jest dochodzenie prowadzone przez bohatera. W trakcie zabawy przemierzamy więc lokacje i przesłuchujemy różnorodne postacie. Szybko przekonujemy się, że prowadzenie takich rozmów nie jest łatwe, gdyż wszyscy mają tutaj coś do ukrycia i niemal każdy zachowuje się podejrzanie. Ponadto musimy uważnie rozglądać się po lokacjach, szukając rozmaitych wskazówek, które mogą naprowadzić nas na prawdziwy trop. Jako że z czasem zaczynamy gromadzić coraz więcej cennych informacji, musimy często zaglądać na specjalną mapę myśli, która pozwala porządkować zdobyte wskazówki i łączyć je ze sobą przy użyciu talentu dedukcji Poirota. W ten sposób w miarę postępów nie tylko dojdziemy do tego, kto stał za morderstwem, lecz również odkryjemy inne podejrzane sprawy wymagające rozwiązania."
        result = predicting.text_cleaner(tekst, 1)
        result = predicting.prepare_text(result)
        self.assertEqual(type(result), numpy.ndarray)



if __name__ == '__main__':
    unittest.main()
