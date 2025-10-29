import spacy


nlp = spacy.load("en_core_web_sm")


text = input("Enter your requirement description: ")


doc = nlp(text)

entities = {}

for sent in doc.sents:
    words = [token.text for token in sent]

    
    if "has" in words:
        has_index = words.index("has")

        if has_index > 0:
            entity = words[has_index - 1].capitalize()
        else:
            entity = words[0].capitalize()

        attributes_text = " ".join(words[has_index + 1:]).replace(".", "")
        attributes_text = attributes_text.replace("and", ",")  
        attributes = [attr.strip() for attr in attributes_text.split(",") if attr.strip()]

        clean_attrs = []
        for attr in attributes:
            attr = attr.replace("a ", "").replace("an ", "").replace("list of ", "").strip()
            clean_attrs.append(attr)

        entities[entity] = clean_attrs

print("Extracted entities and attributes:", entities)

