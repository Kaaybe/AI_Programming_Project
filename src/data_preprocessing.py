"""
Sentiment Analysis Application
==============================

Main application file integrating all modules.

Author: Gloria Kihuria
Date: 13th/Nov/2025
Version: 2.0
"""

import sys
from config import get_project_info, get_paths
from utils import print_header, print_separator, create_directories, get_timestamp

def display_welcome():
    """Display welcome message"""
    info = get_project_info()
    print_header(info['name'])
    print(f"\nVersion: {info['version']}")
    print(f"Author: {info['author']}")
    print(f"Registration: {info['registration']}")
    print(f"Date: {get_timestamp()}")
    print_separator()

def display_system_info():
    """Display system information"""
    print("\n📋 System Overview:")
    print_separator('-', 60)
    
    print("\n1. Data Processing Pipeline")
    print("   → Load CSV data")
    print("   → Clean and preprocess")
    print("   → Handle missing values")
    print("   → Remove duplicates")
    
    print("\n2. Machine Learning Pipeline")
    print("   → Split train/test data")
    print("   → Train logistic regression model")
    print("   → Evaluate performance")
    print("   → Save trained model")
    
    print("\n3. Evaluation Metrics")
    print("   → Accuracy")
    print("   → Precision")
    print("   → Recall")
    print("   → F1-Score")
    
    print_separator('-', 60)

def display_usage():
    """Display usage instructions"""
    print("\n💡 How to Use:")
    print_separator('-', 60)
    
    print("\nStep 1: Prepare Your Data")
    print("  • Place CSV file in 'data/' folder")
    print("  • Ensure proper column headers")
    
    print("\nStep 2: Run the Application")
    print("  • python src/sentiment_analysis.py")
    
    print("\nStep 3: Check Results")
    print("  • Model: models/model.pkl")
    print("  • Metrics: results/metrics.json")
    
    print_separator('-', 60)

def display_requirements():
    """Display requirements"""
    print("\n📦 Requirements:")
    print_separator('-', 60)
    print("  • Python >= 3.8")
    print("  • pandas >= 2.0.0")
    print("  • numpy >= 1.24.0")
    print("  • scikit-learn >= 1.3.0")
    print("  • nltk >= 3.8")
    print("  • matplotlib >= 3.7.0")
    print("  • seaborn >= 0.12.0")
    print("\n  Install: pip install -r requirements.txt")
    print_separator('-', 60)

def main():
    """Main execution function"""
    # Welcome
    display_welcome()
    
    # Setup
    print("\n🔧 Setting up environment...")
    create_directories()
    print("✓ Environment ready!")
    
    # Display info
    display_system_info()
    display_usage()
    display_requirements()
    
    # Final message
    print("\n" + "="*60)
    print("✓ System initialized successfully!")
    print("✓ Ready for sentiment analysis!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()