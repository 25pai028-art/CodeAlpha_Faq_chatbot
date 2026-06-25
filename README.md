# FAQ Chatbot

A smart FAQ chatbot built with Python that helps answer frequently asked questions efficiently.

## Features

- 🤖 Intelligent question-answer matching
- ⚡ Fast response times
- 📚 Easy FAQ database management
- 💬 Natural language processing
- 🔍 Semantic search capabilities

## Installation

1. Clone the repository:
```bash
git clone https://github.com/25pai028-art/CodeAlpha_Faq_chatbot.git
cd CodeAlpha_Faq_chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
# Basic usage example
from chatbot import FAQChatbot

chatbot = FAQChatbot()
response = chatbot.get_answer("Your question here")
print(response)
```

## Project Structure

```
CodeAlpha_Faq_chatbot/
├── README.md
├── requirements.txt
├── chatbot.py
├── faqs/
│   └── faq_data.py
└── tests/
    └── test_chatbot.py
```

## Requirements

- Python 3.7+
- See `requirements.txt` for dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, please open an issue on GitHub.
