# Log Anomaly Detection System

## Description
This project implements a basic anomaly detection system using machine learning to identify unusual patterns in log data. It uses an unsupervised learning approach to classify log entries as Normal or Anomaly.

## Tech Stack
- Python
- Pandas
- Scikit-learn

## Features
- Detects anomalous or suspicious log entries
- Uses Isolation Forest for anomaly detection
- Converts text logs into numerical features using CountVectorizer
- Simple and easy-to-run implementation

## How It Works
1. Log data is loaded from a CSV file
2. Text logs are converted into numerical features using vectorization
3. An Isolation Forest model is trained on the data
4. The model predicts whether each log entry is normal or anomalous

## How to Run

1. Install dependencies:
pip install pandas scikit-learn

2. Run the program:
python anomaly_detection.py

## Example Output
The system classifies logs as:
- Normal
- Anomaly

## Learning Outcomes
- Understood how anomaly detection works using machine learning
- Learned to preprocess text data for ML models
- Gained experience applying AI techniques to cybersecurity-related problems

## Future Improvements
- Use larger and real-world log datasets
- Improve feature extraction techniques
- Add visualization for anomaly detection results
- Build a real time monitoring system
