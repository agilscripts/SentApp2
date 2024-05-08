import joblib
import os

# Paths to the model and vectorizer
model_path = "/Users/audrey/SentimentAnalysis/model.pkl"
vectorizer_path = "/Users/audrey/Desktop/sentapp/vectorizer.pkl"

# Load the model and vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Print last modified times
print("Model last modified:", os.path.getmtime(model_path))
print("Vectorizer last modified:", os.path.getmtime(vectorizer_path))

# Optionally, perform a test prediction to confirm their functionality
def clean_text(text):
    import re
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = text.lower().strip()
    return text

# Example text
test_texts = ["This is a great product!", "This product is bad"]
test_texts = [clean_text(text) for text in test_texts]
test_vectorized = vectorizer.transform(test_texts)

vectorized_text_script = vectorizer.transform([clean_text("This product is good")]).toarray()
print("Vector from Python script:", vectorized_text_script)


# Make predictions
predictions = model.predict(test_vectorized)
print("Predictions:", predictions)