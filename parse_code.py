# Copyright (c) 2024 Melodiz
# Licensed under the MIT License

import ast
import re

def extract_user_text(code):
    """
    Extracts meaningful text from the given code by parsing it and collecting
    identifiers, class names, function names, constant values, and comments.

    Parameters:
    code (str): The source code to extract text from.

    Returns:
    str: A string containing extracted text elements concatenated together.
    """
    try:
        # Parse the code into an abstract syntax tree (AST)
        tree = ast.parse(code)
        names = set()

        # Walk through the AST nodes
        for node in ast.walk(tree):
            # Collect variable and identifier names
            if isinstance(node, ast.Name):
                names.add(node.id)
            # Collect class names
            elif isinstance(node, ast.ClassDef):
                names.add(node.name)
            # Collect function names
            elif isinstance(node, ast.FunctionDef):
                names.add(node.name)
            # Collect constant values
            elif isinstance(node, ast.Constant):
                names.add(node.value)

        # Find all comments in the code
        comments = re.findall(r'#.*', code)

        # Combine names and comments into a single set
        user_text = names.union(comments)

        # Return concatenated text elements with length greater than 4
        return ''.join([x for x in user_text if len(x) > 4])
    except Exception:
        # Fallback: replace newlines and indentation with spaces
        return code.replace('\n', '. ').replace('    ', ' ')