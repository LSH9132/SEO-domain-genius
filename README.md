# SEO Domain Genius 🔍

![GitHub](https://img.shields.io/github/license/LSH9132/seo-domain-genius)
![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-latest-green)
![OpenAI](https://img.shields.io/badge/OpenAI-API-orange)

AI-powered domain name generator that creates SEO-friendly domain suggestions using LangChain and OpenAI/Llama models. 🚀

## ✨ Features

- 🎯 **SEO-Optimized Suggestions**: Generate domain names optimized for search engines
- 🤖 **AI-Powered Analysis**: Utilizes GPT/Llama models for intelligent suggestions
- ✨ **Brand Analysis**: Provides detailed brand meaning and potential analysis
- 🔄 **Real-time Availability**: Checks domain availability instantly
- 🌐 **Multiple Models**: Supports both OpenAI GPT and Llama models
- 🛡️ **Validation**: Ensures generated domains follow naming conventions and best practices

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker (optional)
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/LSH9132/seo-domain-genius.git
cd seo-domain-genius
```
2. Set up the environment:
```bash
./scripts/setup.sh
```
3. Configure your environment variables:
```bash
cp .env.example .env
```
### Edit .env with your API keys and preferences


### Usage

#### Using Docker (Recommended)

```bash
./scripts/run.sh "your platform name"
```

#### Using Python directly
```bash
python main.py "your platform name"
```
## 🏗️ Project Structure
```domain_generator/
├── config/ # Configuration files
├── models/ # AI model files
├── src/ # Source code
│ ├── llm/ # LLM implementations
│ ├── domain/ # Domain generation logic
│ └── utils/ # Utility functions
├── tests/ # Test files
└── scripts/ # Utility scripts
```


## 🔧 Configuration

The application can be configured using environment variables in the `.env` file:

```env
OPENAI_API_KEY=your-api-key
DEFAULT_MODEL_TYPE=openai
GPT_MODEL_NAME=gpt-3.5-turbo
```


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for their GPT models
- LangChain for the amazing framework
- Python community for various packages used in this project

## 📞 Support

If you have any questions or need help, please:
1. Check the [Issues](https://github.com/LSH9132/seo-domain-genius/issues) page
2. Create a new issue if your problem isn't already listed

## 🔮 Roadmap

- [ ] Add support for more TLD options
- [ ] Implement advanced SEO scoring
- [ ] Add bulk domain generation
- [ ] Create web interface
- [ ] Add more language models support

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/LSH9132/seo-domain-genius?style=social)
![GitHub forks](https://img.shields.io/github/forks/LSH9132/seo-domain-genius?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/LSH9132/seo-domain-genius?style=social)

---

<p align="center">Made with ❤️ by Your Name</p>
