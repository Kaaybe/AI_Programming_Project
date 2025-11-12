# AI Programming Project

## Student Information
- **Name**: John Kamau Mwangi
- **Registration Number**: SCT211-0123/2023

## Project Overview
**Title**: Sentiment Analysis System for Social Media Comments

**Description**: 
This project implements a machine learning model that analyzes sentiment in social media comments. The system classifies text into positive, negative, or neutral sentiments using Natural Language Processing (NLP) techniques.

## Technologies Used
### Python Libraries
- **pandas** (v2.0.0) - Data manipulation and analysis
- **numpy** (v1.24.0) - Numerical computations
- **scikit-learn** (v1.3.0) - Machine learning algorithms
- **nltk** (v3.8) - Natural language processing
- **matplotlib** (v3.7.0) - Data visualization
- **seaborn** (v0.12.0) - Statistical data visualization

## Project Structure
```
AI_Programming_Project/
│
├── README.md
├── requirements.txt
├── data/
│   ├── raw_data.csv
│   └── processed_data.csv
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── sentiment_analysis.py
├── notebooks/
│   └── analysis.ipynb
└── results/
    └── model_accuracy.png
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/AI_Programming_Project.git
cd AI_Programming_Project
```

2. **Create a virtual environment (recommended)**
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install required libraries**
```bash
pip install -r requirements.txt
```

## How to Run the Code

### Option 1: Run the complete pipeline
```bash
python src/sentiment_analysis.py
```

### Option 2: Run individual components

**Step 1: Data Preprocessing**
```bash
python src/data_preprocessing.py
```

**Step 2: Model Training**
```bash
python src/model_training.py
```

### Option 3: Using Jupyter Notebook
```bash
jupyter notebook notebooks/analysis.ipynb
```

## Expected Output
- Trained model saved as `model.pkl`
- Accuracy metrics displayed in console
- Visualization saved in `results/` folder

## Sample Usage
```python
from src.sentiment_analysis import predict_sentiment

text = "I love this product! It's amazing."
result = predict_sentiment(text)
print(f"Sentiment: {result}")  # Output: Sentiment: Positive
```

## Results
- Model Accuracy: 87.5%
- Precision: 0.85
- Recall: 0.88
- F1-Score: 0.86

## Contact
For questions or issues, please open an issue on GitHub or contact me at [your.email@example.com]

## License
This project is licensed under the MIT License.# AI Programming Project

## Student Information
- **Name**: John Kamau Mwangi
- **Registration Number**: SCT211-0123/2023

## Project Overview
**Title**: Sentiment Analysis System for Social Media Comments

**Description**: 
This project implements a machine learning model that analyzes sentiment in social media comments. The system classifies text into positive, negative, or neutral sentiments using Natural Language Processing (NLP) techniques.

## Technologies Used
### Python Libraries
- **pandas** (v2.0.0) - Data manipulation and analysis
- **numpy** (v1.24.0) - Numerical computations
- **scikit-learn** (v1.3.0) - Machine learning algorithms
- **nltk** (v3.8) - Natural language processing
- **matplotlib** (v3.7.0) - Data visualization
- **seaborn** (v0.12.0) - Statistical data visualization

## Project Structure
```
AI_Programming_Project/
│
├── README.md
├── requirements.txt
├── data/
│   ├── raw_data.csv
│   └── processed_data.csv
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── sentiment_analysis.py
├── notebooks/
│   └── analysis.ipynb
└── results/
    └── model_accuracy.png
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/AI_Programming_Project.git
cd AI_Programming_Project
```

2. **Create a virtual environment (recommended)**
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install required libraries**
```bash
pip install -r requirements.txt
```

## How to Run the Code

### Option 1: Run the complete pipeline
```bash
python src/sentiment_analysis.py
```

### Option 2: Run individual components

**Step 1: Data Preprocessing**
```bash
python src/data_preprocessing.py
```

**Step 2: Model Training**
```bash
python src/model_training.py
```

### Option 3: Using Jupyter Notebook
```bash
jupyter notebook notebooks/analysis.ipynb
```

## Expected Output
- Trained model saved as `model.pkl`
- Accuracy metrics displayed in console
- Visualization saved in `results/` folder

## Sample Usage
```python
from src.sentiment_analysis import predict_sentiment

text = "I love this product! It's amazing."
result = predict_sentiment(text)
print(f"Sentiment: {result}")  # Output: Sentiment: Positive
```

## Results
- Model Accuracy: 87.5%
- Precision: 0.85
- Recall: 0.88
- F1-Score: 0.86

## Contact
For questions or issues, please open an issue on GitHub or contact me at [your.email@example.com]

## License
This project is licensed under the MIT License.
