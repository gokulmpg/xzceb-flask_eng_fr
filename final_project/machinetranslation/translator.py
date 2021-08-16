""" Program that translates texts"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

""" create an instance of the IBM Watson Language translator """

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ funtion that translates English to French """
    fren_text= language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text= fren_text ['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ funtion that translates French to English """
    eng_text= language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text= eng_text ['translations'][0]['translation']
    return english_text
