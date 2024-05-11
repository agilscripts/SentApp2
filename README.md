# Review Sentiment Analysis Tool

This project is a sentiment analysis tool designed to analyze text reviews and determine if they are positive or negative. The application is built using Python and Flask, and it utilizes machine learning models trained with scikit-learn.

## Prerequisites

Before you run this project, you need to have Python installed on your machine. Additionally, you should have the following Python packages installed:
- Flask
- joblib
- pandas
- numpy
- scikit-learn
- imbalanced-learn

You can install all required packages using the following command:

```bash
pip install Flask joblib pandas numpy scikit-learn imbalanced-learn
```

## Project Structure

This project includes the following files and directories:
- `app.py`: The main Python script that runs the Flask application.
- `model.pkl`: The pre-trained sentiment analysis model.
- `vectorizer.pkl`: The TF-IDF vectorizer used to convert text data into a format that can be analyzed by the model.
- `templates/`: Directory containing the HTML templates for the web interface.
- `static/`: Directory for static files such as CSS and JavaScript.

## Setup

1. Clone the repository to your local machine.
2. Navigate to the directory containing the project files.
3. Ensure that all required Python packages are installed.

## Running the Application

To run the application, execute the following command from the root directory of the project:

```bash
python app.py
```

After running the command, the Flask server will start, and the application will be available at `http://127.0.0.1:5000/` in your web browser.

## Using the Application

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. You will see a text box where you can enter a review.
3. Enter a review and click the "Analyze Sentiment" button.
4. The sentiment analysis result will be displayed below the text box.
