# GPT Text Authenticator

A modern, AI-powered tool to detect, analyze, and humanize AI-generated text.

## Core Features

* **AI Detection**: Evaluates text to determine the likelihood of it being AI-generated, providing a confidence score.
* **Explainable Analysis**: Identifies specific characteristics (like perplexity and burstiness) that indicate machine generation.
* **Text Humanization**: Suggests concrete modifications to make text sound more natural and authentic.
* **Style Emulation (Future)**: Will allow fine-tuning the model to a user's unique writing style for personalized suggestions.

## Quick Start

*The package is not pushed to PyPI yet.*

```bash
# Local installation
git clone https://github.com:majedlutfi96/gpt-text-authenticator.git
cd gpt-text-authenticator
python -m pip install .

# Remote installation (not ready yet)
pip install gpt-text-authenticator
```

## Usage

### Command Line Interface

The tool provides a simple command-line interface for easy analysis.

```bash
# Evaluate a text file
gpt-text-authenticator evaluate path/to/your/document.txt

# Launch the interactive web API
gpt-text-authenticator run-server
```

### Python API

You can also use the library directly in your Python code:

```python
from gpt_text_authenticator.authenticator import GPTTextAuthenticator
from dotenv import load_dotenv
import os

# Load environment variables (API keys)
load_dotenv()

# Initialize the authenticator
provider = os.getenv("provider", "google")  # "google" or "ollama"
model = os.getenv("model", "gemini-2.5-pro")  # Model name
api_key = os.getenv("api_key")  # Your API key

authenticator = GPTTextAuthenticator(provider, model, api_key)

# Evaluate text
result = authenticator.evaluate_text("Your text to analyze goes here.")

# Access the analysis results
print(f"AI Score: {result.score}/100")
print(f"Feedback: {result.feedback}")
print("Reasons:")
for reason in result.reasons:
    print(f"- {reason}")
```

See the [examples directory](./examples) for more detailed usage examples.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
