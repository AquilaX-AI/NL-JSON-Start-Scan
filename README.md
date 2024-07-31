# AquilaX-NL-JSON-Start-Scan

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

AquilaX-NL-JSON-Start-Scan is a model built using Hugging Face's T5-small to convert natural language queries about vulnerabilities into JSON queries for MongoDB.

## Features
- Convert natural language queries to JSON queries.
- Easily integrate with MongoDB for scanning repositories.
- Built using Hugging Face T5-small model.

## Model Information

### Model
- **Name**: AquilaX-NL-JSON-Start-Scan
- **Architecture**: T5-small
- **Framework**: Hugging Face Transformers

### Description
The AquilaX-NL-JSON-Start-Scan model is designed to interpret natural language queries related to vulnerabilities in code and convert them into JSON queries that can be executed on a MongoDB database. This facilitates automated scanning and analysis of code repositories for security issues. The model leverages the capabilities of the T5-small architecture, which is well-suited for natural language understanding and generation tasks.

## Getting Started

### Prerequisites
- Hugging Face Transformers
- torch

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AquilaX-AI/NL-JSON-Start-Scan.git
   cd NL-JSON-Start-Scan

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Using Colab Notebook
You can run the model directly in a Colab notebook. Open the provided notebook in Google Colab:

### Using Python Script
Alternatively, you can run the model using the provided Python script in app.py
```bash
python app.py
```
## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.


## Authors
- [Aquilax-Ai](https://huggingface.co/AquilaX-AI)

## Acknowledgments
- Hugging Face for the Transformers library.
