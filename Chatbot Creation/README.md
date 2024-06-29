# Legal Document NLP Processor

This project implements advanced NLP techniques to process and understand legal language, identify key clauses, and generate concise summaries of legal documents.

## Features

- **Preprocessing**: Tokenization, lemmatization, POS tagging, and named entity recognition.
- **Clause Identification**: Extraction of key clauses such as confidentiality and termination clauses.
- **Summarization**: Generating concise summaries of legal documents using state-of-the-art NLP models.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mhmmeddanish/legal-document-nlp-processor.git
    cd legal-document-nlp-processor
    ```

2. Install the required libraries:

    ```bash
    pip install spacy transformers
    python -m spacy download en_core_web_sm
    ```

## Usage

1. Open the `chatbot.py` file and replace the placeholder text with your legal document text:

    ```python
    # Input your legal document text here
    text = """
    This Agreement is made and entered into as of the Effective Date by and between the parties. 
    1. Confidentiality: The parties agree to maintain in confidence and not to disclose any Confidential Information to any third party.
    2. Termination: This Agreement may be terminated by either party upon thirty (30) days written notice to the other party.
    """
    ```

2. Run the `chatbot.py` script:

    ```bash
    python chatbot.py
    ```

3. The script will output the extracted entities, identified clauses, and the generated summary.

## Example Output

```plaintext
Entities: [('Effective Date', 'DATE')]
Confidentiality Clauses: ['Confidentiality: The parties agree to maintain in confidence and not to disclose any Confidential Information to any third party.']
Termination Clauses: ['Termination: This Agreement may be terminated by either party upon thirty (30) days written notice to the other party.']
Summary: This Agreement is made and entered into as of the Effective Date by and between the parties. The parties agree to maintain in confidence and not to disclose any Confidential Information to any third party. This Agreement may be terminated by either party upon thirty (30) days written notice to the other party.
