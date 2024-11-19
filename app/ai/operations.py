from openai import OpenAI
import json
import os

client = OpenAI()

def check_factuality(input_string):
    """
    Queries the OpenAI API to check if a statement is factually correct.

    Parameters:
        input_string (str): The input statement to check.

    Returns:
        dict: JSON response indicating factuality.
    """
    # Define the system message for the chat completion
    # Define the function schema
    functions = [
        {
            "name": "check_factuality",
            "description": "Determine whether a given statement is factually correct.",
            "parameters": {
                "type": "object",
                "properties": {
                    "is_factual": {"type": "string", "enum": ["true", "false"]},
                    "reason": {"type": "string", "description": "Reason if the statement is false."}
                },
                "required": ["is_factual"]
            }
        }
    ]

    try:
        # Query the OpenAI API using ChatCompletion
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a fact-checking assistant. Check number and date related facts are accurate as well"},
                {"role": "user", "content": input_string}
            ],
            functions=functions,
            function_call={"name": "check_factuality"}
        )

        # Parse and return the JSON response
        return json.loads(completion.choices[0].message.function_call.arguments)

    except Exception as e:
        return {"error": str(e)}


def check_tone(input_string):
    """
    Analyzes the tone and style of the input string to ensure it remains conversational.

    Parameters:
        input_string (str): The input string to check for tone and style.

    Returns:
        dict: JSON response indicating whether the tone is conversational and any suggestions for improvement.
    """
    # Define the function schema for tone analysis
    functions = [
        {
            "name": "check_tone",
            "description": "Evaluate the tone of the provided text and suggest improvements to match Paul Graham's writing style, which combines a Direct & Conversational tone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "is_conversational": {
                        "type": "string",
                        "enum": ["true", "false"]
                    },
                    "suggestions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "previous_sentence": {
                                    "type": "string",
                                    "description": "The original sentence before rephrasing."
                                },
                                "new_suggested_sentence": {
                                    "type": "string",
                                    "description": "The rephrased sentence to align with the desired tone."
                                }
                            },
                            "required": ["previous_sentence", "new_suggested_sentence"]
                        },
                        "description": "Rephrases, sentence by sentence if any are required."
                    }
                },
                "required": ["is_conversational"]
            }
        }
    ]

    try:
        # Query the OpenAI API using ChatCompletion
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a tone analysis assistant trained to evaluate text based on Paul Graham's writing style"
                },
                {"role": "user", "content": input_string},
            ],
            functions=functions,
            function_call={"name": "check_tone"}
        )

        # Parse and return the JSON response
        return json.loads(completion.choices[0].message.function_call.arguments)

    except Exception as e:
        return {"error": str(e)}


def generate_upsc_tags(input_string):
    """
    Generates tags or taxonomy suggestions for UPSC-related content.

    Parameters:
        input_string (str): The text content to analyze.

    Returns:
        dict: JSON response containing suggested tags for the content.
    """
    # Define the function schema
    functions = [
        {
            "name": "generate_upsc_tags",
            "description": "Generate up to 5 UPSC subject tags based on the provided content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "Art and Culture",
                                "Geography",
                                "Environment & Ecology",
                                "Polity",
                                "Economy",
                                "History",
                                "Science and Technology",
                                "Ethics",
                                "Sociology",
                                "Anthropology",
                                "Public Administration",
                                "Current Affairs"
                            ]
                        },
                        "description": "List of suggested tags, up to 5."
                    }
                },
                "required": ["tags"]
            }
        }
    ]

    try:
       # Query the OpenAI API using ChatCompletion
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a UPSC subject tagging assistant."},
                {"role": "user", "content": input_string}
            ],
            functions=functions,
            function_call={"name": "generate_upsc_tags"}
        )

        # Parse and return the JSON response
        return json.loads(completion.choices[0].message.function_call.arguments)

    except Exception as e:
        return {"error": str(e)}
