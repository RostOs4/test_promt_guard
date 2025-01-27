# Copyright (c) 2024 Melodiz
# Licensed under the MIT License

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_ollama import OllamaLLM
import re

# Initialize the LLaMA model for classification
guard_model = OllamaLLM(model="xe/llamaguard3:latest")

# Regular expression to detect Russian characters

def classify_with_llama(prompt):
    """
    Classifies the given prompt using the LLaMA model.
    
    Parameters:
    prompt (str): The input text to classify.

    Returns:
    str: The classification result from the LLaMA model.
    """
    # Translate Russian text to English if necessary
    # Use the LLaMA model to classify the prompt
    classification_result = guard_model.invoke(prompt)
    return classification_result