# Copyright (c) 2024 Melodiz
# Licensed under the MIT License

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Initialize classification tokenizer and model
# These are pre-trained models for detecting prompt injections
guard_tokenizer = AutoTokenizer.from_pretrained("ProtectAI/deberta-v3-base-prompt-injection-v2")
guard_model = AutoModelForSequenceClassification.from_pretrained("ProtectAI/deberta-v3-base-prompt-injection-v2")

# Create a text classification pipeline
# This pipeline will handle the tokenization, model inference, and output processing
classifier = pipeline(
    "text-classification",  # Specify the task type
    model=guard_model,      # Use the pre-trained classification model
    tokenizer=guard_tokenizer,  # Use the corresponding tokenizer
    truncation=True,        # Enable truncation to handle long inputs
    max_length=512,         # Set the maximum input length
    device=torch.device("cuda" if torch.cuda.is_available() else "cpu"),  # Use GPU if available
)

def classify_prompt(prompt):
    """
    Classifies the given prompt to detect potential prompt injections.
    
    Parameters:
    prompt (str): The input text to classify.

    Returns:
    tuple: A tuple containing the predicted label and score.
    """
    # Get the prediction from the classifier
    prediction = classifier(prompt)[0]
    # Return the label and score of the prediction
    return prediction['label'], prediction['score']