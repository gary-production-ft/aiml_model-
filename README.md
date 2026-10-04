# Cattle and Buffalo Classifier

A browser-based cattle-versus-buffalo image classifier with an optional Python Flask backend. The frontend can run by itself with browser-side computer-vision rules. When the backend is available, uploaded images are sent to a trained scikit-learn model and the response also includes breed information from the project database.

## Features

- Drag-and-drop image upload with preview
- Cattle versus buffalo classification
- Confidence scores and probability breakdown
- Breed matching using color-profile analysis
- Browser-only fallback when the Flask API is unavailable
- Responsive pages for home, upload, breed information, and project information
- REST endpoints for health checks, model metadata, breeds, and classification

## Project Structure

```text
.
|-- app.py                              # Flask API and model inference
|-- breed_database.py                   # Python breed data and matching logic
|-- train_model.py                      # Feature extraction and model training
|-- setup.py                             # Optional dependency and training setup helper
|-- demo_system.py                      # Command-line demonstration
|-- test_system.py                      # Backend/system tests
|-- simple_test.py                      # Small model smoke test
|-- requirements.txt                    # Python dependencies
|-- run_system.bat                      # Windows backend launcher
|-- run_system.sh                       # Linux/macOS backend launcher
|-- home.html                           # Main frontend page
|-- index.html                          # Minimal frontend entry page
|-- upload.html                         # Image upload and results page
|-- breeds.html                         # Breed browser
|-- info.html                            # System information page
|-- contact.html                        # Contact page
|-- test_web_system.html                # Browser-side test page
|-- script.js                           # Frontend upload and classification logic
|-- ml_classifier.js                    # Backend integration and browser fallback
|-- breed-database.js                   # Frontend breed data
|-- style.css                           # Shared frontend styles
|-- cattle_buffalo_model.joblib         # Trained classifier
|-- cattle_buffalo_model_metadata.json  # Class and feature metadata
|-- simple_model.joblib                 # Small test model
|-- cow-and-buffalo.v1i.tensorflow/     # Training, validation, and test data
|-- processed_buffalo_dataset/          # Additional breed image data
|-- models/                             # Model workspace directory
|-- static/                             # Flask/static asset directory
`-- templates/                          # Flask template directory
```

## Requirements

- Python 3.9 or newer recommended
- A modern browser with JavaScript enabled
- Windows, Linux, or macOS

The backend dependencies are listed in `requirements.txt`: Flask, Flask-CORS, OpenCV, NumPy, pandas, scikit-learn, joblib, and Pillow.

## Installation

From the project root:

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

The repository already contains a trained model. Retraining is optional and can take several minutes:

```bash
python train_model.py
```

## Run the Project

The full application uses two local servers. Start the Flask API in one terminal:

```bash
python app.py
```

The API listens on `http://localhost:5000`.

Start the static frontend in a second terminal:

```bash
python -m http.server 8000
```

Open the application at:

```text
http://localhost:8000/home.html
```

The direct upload page is available at `http://localhost:8000/upload.html`.

On Windows, `run_system.bat` starts the Flask backend. The frontend still needs to be served separately with `python -m http.server 8000`. On Linux or macOS, `run_system.sh` starts the backend.

## Browser-Only Mode

The frontend can be used without the Flask server by serving the project directory and opening `home.html`. In this mode, `ml_classifier.js` uses the browser-side rule-based classifier. Running the Flask API enables the trained model and richer API responses.

## API Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/api/health` | Check server and model status |
| `GET` | `/api/model_info` | Return model metadata |
| `POST` | `/api/classify` | Classify a base64-encoded image |
| `GET` | `/api/breeds/<animal_type>` | List breeds for cattle or buffalo |
| `GET` | `/api/breed/<animal_type>/<breed_name>` | Return breed details |
| `GET` | `/api/breed_stats` | Return breed database statistics |

Example health check:

```bash
curl http://localhost:5000/api/health
```

Example classification request body:

```json
{
  "image": "data:image/jpeg;base64,<base64-image-data>",
  "bbox": [0, 0, 640, 480]
}
```

The `bbox` field is optional. The classification response includes the predicted animal type, confidence, class probabilities, breed match, breed confidence, color profile, and model metadata.

## Testing

Run the Python system tests from the project root:

```bash
python test_system.py
```

Run the small model smoke test:

```bash
python simple_test.py
```

With the frontend server running, open `http://localhost:8000/test_web_system.html` for browser-side checks.

## Troubleshooting

- If `/api/health` reports that the model is not loaded, confirm that `cattle_buffalo_model.joblib` and `cattle_buffalo_model_metadata.json` are in the project root.
- If the page cannot reach the API, confirm that `python app.py` is running on port `5000`.
- If the HTML page does not load correctly from a file path, serve the project with `python -m http.server 8000` instead.
- Use clear, well-lit images where the animal is visible and occupies a substantial part of the frame.

## Notes

The model uses handcrafted image features including RGB and HSV histograms, texture, edges, shape, brightness, contrast, and color moments. Predictions are intended as a prototype and should not be treated as veterinary or production-grade identification without further validation.
