import subprocess
import sys
import os
from flask import Flask, render_template, request
import joblib
import re

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    # List of required packages
    required_packages = [
        "pandas",
        "numpy",
        "scikit-learn",
        "imbalanced-learn",
        "joblib",
        "flask"
    ]

    # Install required packages
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} not found, installing...")
            install(package)

    # Set up environment variables or other configurations here
    # Example: os.environ['MODEL_PATH'] = '/path/to/your/model'
    print("Setup completed. Environment is ready to use.")

    # Use relative paths for the model and vectorizer
    directory_path = os.path.dirname(__file__)  # Gets the directory where the script runs
    model_path = os.path.join(directory_path, 'model.pkl')
    vectorizer_path = os.path.join(directory_path, 'vectorizer.pkl')

    # Load your trained model
    model = joblib.load(model_path)

    # Load the TfidfVectorizer for text vectorization
    vectorizer = joblib.load(vectorizer_path)

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/analyze', methods=['POST'])
    def analyze():
        text = request.form['userInput']
        cleaned_text = clean_text(text)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]
        result = 'Positive' if prediction == 1 else 'Negative'
        return render_template('home.html', result=result)

    def clean_text(text):
        text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
        text = text.lower().strip()
        return text

    if __name__ == '__main__':
        app.run(debug=True)

if __name__ == "__main__":
    main()
