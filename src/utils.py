import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

def initialize_firebase_object():
    cred = credentials.Certificate("PATH_TO_FIREBASE_AUTH")

    try:
        firebase_admin.get_app()
    except ValueError as e:
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

def get_word_info(word_data_list):
    hints ={}
    
    for word_data in word_data_list:
        # Check if the word data is available
        if isinstance(word_data, dict):
            # Extract the word and its meanings
            word = word_data.get("word", "")
            
            meanings = []
            if "meanings" in word_data:
                for meaning in word_data["meanings"]:
                    part_of_speech = meaning.get("partOfSpeech", "")
                    definitions = meaning.get("definitions", [])
                    meanings.append({
                        "Part of Speech": part_of_speech,
                        "Definitions": [definition.get("definition", "") for definition in definitions]
                    })
            
            # Create a dictionary with hints
            hints["Word"] = word
            for i, meaning in enumerate(meanings):
                hints[f"Part of Speech {i + 1}"] = meaning["Part of Speech"]
                hints[f"Definitions {i + 1}"] = meaning["Definitions"]
    print(hints)
    return hints