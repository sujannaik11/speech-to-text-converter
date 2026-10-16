# 🎙️ Speech-to-Text Converter

A simple multilingual Speech-to-Text application built using Python and Streamlit. It allows users to record their voice and convert speech into text in multiple Indian languages.

## ✨ Features

- 🎤 Record audio directly through the application.
- 🌐 Support for English, Hindi, Malayalam, and Kannada.
- 📝 Convert recorded speech into text.
- 📥 Download the transcription as a `.txt` file.
- ⚠️ Error handling for unclear audio and connection issues.

## 🛠️ Technologies Used

- Python
- Streamlit
- SpeechRecognition
- Google Speech Recognition service

## 📁 Project Structure

```text
speech-to-text-converter/
├── deployspeech.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/speech-to-text-converter.git
cd speech-to-text-converter
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run deployspeech.py
```

The application will open in your web browser.

## 🚀 How to Use

1. Select your preferred language.
2. Click the microphone button and record your speech.
3. Click **Convert to Text**.
4. View the generated transcription.
5. Download the text file if required.

## 🌍 Supported Languages

- English (India)
- Hindi
- Malayalam
- Kannada

## ⚠️ Requirements

- Python installed on your system.
- A working microphone and browser permission to access it.
- An active internet connection for Google's speech recognition service.

## 📌 Future Improvements

- Add more Indian languages.
- Support uploading pre-recorded audio files.
- Improve transcription accuracy and add editing options.
- Add a speech playback feature.

## 👨‍💻 Author

Developed as a Python and Streamlit project.

## 📄 License

This project is available for educational and learning purposes.
