# Install spaCy library if not already installed
# !pip install spacy
# python -m spacy download en_core_web_sm

import spacy
import pandas as pd

# Load spaCy's pre-trained model
nlp = spacy.load("en_core_web_sm")

# Sample text data
text = """Apple is looking at buying U.K. startup for $1 billion. 
        San Francisco considers banning sidewalk delivery robots. 
        London is a big city in the United Kingdom."""

# Process the data with spaCy
doc = nlp(text)

# Function to extract named entities
def extract_named_entities(doc):
    entities = []
    for ent in doc.ents:
        entities.append({
            'Entity': ent.text,
            'Label': ent.label_,
            'Description': spacy.explain(ent.label_),
            'Start': ent.start_char,
            'End': ent.end_char
        })
    return entities

# Extract named entities from the document
named_entities = extract_named_entities(doc)
print("Named Entities:")
for ent in named_entities:
    print(f"  {ent['Entity']} ({ent['Label']}): {ent['Description']}")

# Convert to DataFrame
df_entities = pd.DataFrame(named_entities)

# Save named entities to a CSV file
df_entities.to_csv('named_entities.csv', index=False)
print("\nNamed entities saved to 'named_entities.csv'")
print("\nDataFrame preview:")
print(df_entities)