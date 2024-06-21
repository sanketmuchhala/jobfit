# Job Description Keyword Extractor

This project is a web application that extracts relevant technical keywords from a job description to help users enhance their resumes. It uses a combination of SpaCy for POS tagging and a pre-trained transformer model for named entity recognition.

## Features

- Extracts technical keywords from job descriptions
- Uses SpaCy for part-of-speech tagging
- Utilizes a pre-trained transformer model for named entity recognition
- Web interface built with Flask

## Technologies Used

- Python
- Flask
- SpaCy
- Transformers (Hugging Face)
- HTML/CSS (for the web interface)

## Prerequisites

- Python 3.9 or higher
- Git
- A Railway account (or another deployment platform if preferred)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/job_description_keyword_extractor.git
   cd job_description_keyword_extractor
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the SpaCy model**:

   ```bash
   python -m spacy download en_core_web_sm
   ```

## Running the Application Locally

1. **Run the Flask application**:

   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://127.0.0.1:5000/`.

## Project Structure

```
job_description_keyword_extractor/
├── app.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── templates/
│   └── index.html
└── static/
    └── style.css
```

- `app.py`: The main Flask application file.
- `requirements.txt`: Python dependencies.
- `runtime.txt`: Specifies the Python version.
- `Procfile`: Specifies the commands to run the application on Railway.
- `templates/index.html`: HTML template for the web interface.
- `static/style.css`: CSS for styling the web interface.
