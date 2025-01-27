# Copyright (c) 2024 Melodiz
# Licensed under the MIT License

import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Initialize translation tokenizer and model
# These are pre-trained models from the Helsinki-NLP group for translating Russian to English
translate_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
translate_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

# Regular expression to detect Russian characters
russian_regex = re.compile(r'[а-яА-ЯёЁ]')

def translate_russian_to_english(text_to_translate):
    """
    Translates Russian text within the input string to English using a pre-trained model.
    
    Parameters:
    text_to_translate (str): The text that may contain Russian words to be translated.

    Returns:
    str: The input text with Russian words translated to English.
    """
    # Ensure the input is a string
    if type(text_to_translate) != str:
        try:
            # Attempt to convert non-string input to a string
            text_to_translate = ''.join(text_to_translate.split())
        except Exception as e:
            # Log and return the original input if conversion fails
            print(f"Error while translating Russian to English: {e}")
            return text_to_translate

    # Split the text into words for individual translation
    words = text_to_translate.split()
    translated_words = []

    # Iterate over each word in the text
    for word in words:
        # Check if the word contains Russian characters
        if russian_regex.search(word):
            # Encode the word into tokens and generate the translation
            input_tokens = translate_tokenizer.encode(word, return_tensors="pt")
            output_tokens = translate_model.generate(input_tokens)
            # Decode the translated tokens back into a string
            translated_word = translate_tokenizer.decode(output_tokens[0], skip_special_tokens=True)
            translated_words.append(translated_word)
        else:
            # If the word is not Russian, keep it as is
            translated_words.append(word)

    # Join the translated words back into a single string
    return ' '.join(translated_words)