# Copyright (c) 2024 Melodiz
# Licensed under the MIT License

import os
from parse_code import extract_user_text
from translation import translate_russian_to_english
from deBERTa_classification import classify_prompt
from llama_classification import classify_with_llama

# Disable parallelism in tokenizers to avoid warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def process_prompt(prompt, model='deBERTa'):
    """
    Processes the given prompt by extracting text, translating it, and classifying it using the specified model.
    
    Parameters:
    prompt (str): The input text to process.
    model (str): The model to use for classification ('deBERTa' or 'llama').

    Returns:
    tuple: A tuple containing the predicted label and score or classification result.
    """
    # Extract user text from code
    prompt = extract_user_text(prompt)
    # Translate Russian text to English
    prompt = translate_russian_to_english(prompt)
    
    # Classify the prompt using the specified model
    if model == 'deBERTa':
        # Use deBERTa model for classification
        label, score = classify_prompt(prompt)
    elif model == 'llama':
        # Use LLaMA model for classification
        label = classify_with_llama(prompt)
        score = None  # LLaMA model might not provide a score
    else:
        raise ValueError("Invalid model specified. Choose 'deBERTa' or 'llama'.")
    
    return label, score

# Example usage
prompt = "Your prompt text here"
label, score = process_prompt(prompt, model='llama')
print(f"Label: {label}, Score: {score}")