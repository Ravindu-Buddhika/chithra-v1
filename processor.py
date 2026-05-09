import spacy

nlp = spacy.load("en_core_web_sm")

def check_local_intent(text):
    doc = nlp(text.lower())
    
    common_apps = ["whatsapp", "chrome", "notepad", "calculator", "vlc", "Brave", "browser", "Steam","VS Code"]
    
    for token in doc:
        if token.lemma_ == "open" and token.pos_ == "VERB":
            for child in token.children:
                if child.dep_ == "dobj" and child.text in common_apps:
                    return "OS_OPEN_APP", child.text
                    
    return "GEMINI_QUERY", None