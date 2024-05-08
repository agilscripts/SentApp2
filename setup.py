import subprocess
import sys
import os

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

if __name__ == "__main__":
    main()