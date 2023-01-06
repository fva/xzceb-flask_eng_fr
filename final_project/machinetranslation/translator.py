"""

Module to test IBM Translator service

"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

#Setup the Language Translator
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# List the languages that the service can translate
#languages = language_translator.list_identifiable_languages().get_result()
#print(json.dumps(languages, indent=2))

def english_to_french(english_text):

    """
    Convert English text to French text
    """

    model_id = 'en-fr'  # English to French translation

    translation = language_translator.translate(
        text = english_text,
        model_id = model_id
    ).get_result()

    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):

    """
    Convert French text to English text
    """

    model_id = 'fr-en'  # French to English translation

    translation = language_translator.translate(
        text = french_text,
        model_id = model_id
    ).get_result()
    
    english_text = translation['translations'][0]['translation']
    return english_text
