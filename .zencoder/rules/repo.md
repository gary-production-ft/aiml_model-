---
description: Repository Information Overview
alwaysApply: true
---

# Cattle vs Buffalo Classifier Information

## Summary
A web application that uses computer vision and machine learning to classify images between cattle and buffalo. The system has both a browser-based frontend using JavaScript and an optional Python Flask backend for enhanced ML capabilities.

## Structure
- **Frontend**: HTML/CSS/JS files for the web interface (`home.html`, `upload.html`, etc.)
- **Backend**: Python Flask API (`app.py`) for ML model serving
- **ML Components**: Training scripts and model files (`train_model.py`, `*.joblib`)
- **Dataset**: TensorFlow dataset (`cow-and-buffalo.v1i.tensorflow`) with training/validation images
- **Utilities**: Demo and test scripts (`demo_system.py`, `test_system.py`)

## Language & Runtime
**Languages**: JavaScript (Frontend), Python 3.x (Backend)
**Runtime**: Web Browser (Frontend), Python 3.x (Backend)
**Build System**: None (Frontend), pip (Backend)
**Package Manager**: npm (Frontend), pip (Backend)

## Dependencies
**Frontend Dependencies**:
- Pure JavaScript (no external libraries required)
- Browser with ES6+ support

**Backend Dependencies**:
- flask==2.3.3
- flask-cors==4.0.0
- opencv-python==4.8.1.78
- numpy==1.24.3
- pandas==2.0.3
- scikit-learn==1.3.0
- joblib==1.3.2
- Pillow==10.0.0

## Build & Installation
```bash
# Install Python dependencies
pip install -r requirements.txt

# Train the ML model (optional)
python train_model.py

# Start the Flask backend server
python app.py
```

## Usage & Operations
**Frontend Only Mode**:
```bash
# Start a simple HTTP server
python -m http.server 8000

# Open in browser
# Navigate to http://localhost:8000/home.html
```

**Full System (with ML backend)**:
```bash
# Start the Flask backend
python app.py

# Open in browser
# Navigate to http://localhost:8000/home.html
```

**Demo Mode**:
```bash
# Run the demo script
python demo_system.py
```

## Main Files & Resources
**Frontend Entry Points**:
- `home.html`: Main landing page
- `upload.html`: Image upload and classification interface
- `script.js`: Main JavaScript logic
- `ml_classifier.js`: ML integration with backend
- `breed-database.js`: Breed information database

**Backend Entry Points**:
- `app.py`: Flask server with ML model serving
- `train_model.py`: Script to train the ML model

**Model Files**:
- `cattle_buffalo_model.joblib`: Trained ML model
- `cattle_buffalo_model_metadata.json`: Model metadata

**Dataset**:
- `cow-and-buffalo.v1i.tensorflow/`: TensorFlow dataset with training/validation images

## Testing & Validation
**Test Files**:
- `test_system.py`: System test script
- `test_web_system.html`: Web interface test page
- `simple_test.py`: Simple model test

**Run Tests**:
```bash
# Run system tests
python test_system.py
```

## Classification Logic
The system uses two classification methods:
1. **Rule-based Classification**: Uses computer vision techniques (color analysis, texture features, edge detection) for browser-only operation.
2. **ML-based Classification**: Uses a trained scikit-learn model served via Flask API for higher accuracy.

The system automatically falls back to rule-based classification if the ML backend is unavailable.

In summary, the classifier is designed to operate in diverse environments, ensuring flexibility and robustness in distinguishing between cattle and buffalo.