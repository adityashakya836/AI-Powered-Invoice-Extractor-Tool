# 🧾 AI-Powered Invoice Extractor Tool

This AI-powered Invoice Extractor tool leverages generative AI to automatically extract essential information from invoices. Whether it's extracting vendor details, dates, amounts, or line items, this tool simplifies the process of handling and managing invoices.

## 🚀 Features

- **🧠 Generative AI Integration:** Utilizes Google's generative AI for advanced text extraction and processing.
- **💻 Streamlit Interface:** A user-friendly interface built with Streamlit, allowing for easy interaction with the tool.
- **📄 Language and PDF Handling:** Supports language processing using LangChain and PDF manipulation with PyPDF2.
- **📦 Data Storage:** Information is efficiently stored and managed using ChromaDB.
- **🔒 Environment Configuration:** Environment variables are managed securely with Python-dotenv.

## 🛠️ Tech Stack

- **Streamlit:** Frontend interface for seamless user experience.
- **Google Generative AI:** Powering the AI-driven extraction process.
- **Python-dotenv:** Managing environment variables securely.
- **Langchain:** For language processing and chaining AI models.
- **PyPDF2:** For handling and processing PDF files.
- **ChromaDB:** For storing and retrieving extracted information.

## 🏁 Getting Started

### Prerequisites

- 🐍 Python 3.8 or higher
- 🛑 Virtual environment setup (recommended)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/invoice-extractor-tool.git
   cd invoice-extractor-tool

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv

3. **Activate virtual environment:**
   ```bash
   venv\Scripts\activate
4. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
5. **Run the streamlit application**
   ```bash
   streamlit run invoide_extractor.py

## 🔧 How to Use

1. **Upload a PDF invoice** through the Streamlit interface.
2. The tool will automatically **extract and display key information** from the invoice.
3. **Download or store** the extracted data as needed.

![AI-Powered Invoice Extractor](https://github.com/adityashakya836/AI-Powered-Invoice-Extractor-Tool/blob/main/invoice1.png)
![AI-Powered Invoice Extractor](https://github.com/adityashakya836/AI-Powered-Invoice-Extractor-Tool/blob/main/invoice2.png)

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any ideas, improvements, or bug fixes.
