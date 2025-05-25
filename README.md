# 🤖 Jarvis - AI Voice Assistant

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
</div>

## 📋 Overview

Jarvis is an intelligent voice assistant built with Python that combines speech recognition, face authentication, and web interface capabilities. It can perform various tasks like opening applications, sending messages, making calls, checking internet speed, and much more through voice commands.

## ✨ Features

- 🎤 **Voice Recognition**: Advanced speech-to-text using Google Speech Recognition
- 👤 **Face Authentication**: Secure login using OpenCV face recognition
- 🌐 **Web Interface**: Beautiful web-based UI with animations
- 📱 **WhatsApp Integration**: Send messages and make calls
- 🔍 **Smart Commands**: Open applications, search web, control system
- 🎵 **Media Control**: Play YouTube videos, take screenshots
- 📊 **System Monitoring**: Check battery, internet speed, location
- 🗑️ **System Management**: Empty recycle bin, shutdown/restart
- 💬 **AI Chatbot**: Intelligent conversation capabilities

## 🏗️ Core Components

### 1. **Engine Module** (`/engine/`)

- **`command.py`**: Main command processing and speech recognition
- **`features.py`**: Core functionality implementations (WhatsApp, YouTube, etc.)
- **`helper.py`**: Utility functions for system operations
- **`db.py`**: Database operations for contacts and commands
- **`config.py`**: Configuration settings

### 2. **Authentication System** (`/engine/auth/`)

- **`sample.py`**: Capture face samples for training
- **`trainer.py`**: Train the face recognition model
- **`recognize.py`**: Face authentication during login

### 3. **Web Interface** (`/www/`)

- **`index.html`**: Main web interface
- **`controller.js`**: Frontend-backend communication
- **`main.js`**: UI interactions and animations
- **`style.css`**: Styling and animations

### 4. **Main Files**

- **`run.py`**: Main entry point with multiprocessing
- **`main.py`**: Web server and initialization
- **`device.bat`**: ADB device connection script

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Webcam for face authentication
- Microphone for voice commands
- ADB (Android Debug Bridge) for mobile features

### Step 1: Clone the Repository

```bash
git clone https://github.com/Hamza-Meer007/Jarvis-Python.git
cd Jarvis-Python
```

### Step 2: Create Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate  # On Windows
# source myenv/bin/activate  # On macOS/Linux
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create Required Directories

Create these empty folders in the project directory:

```bash
mkdir engine\auth\sample
mkdir engine\auth\trainer
```

### Step 5: Face Authentication Setup

**Important**: You must complete face authentication setup before running the main application.

#### 5.1 Capture Face Samples

```bash
python engine/auth/sample.py
```

- Enter a numeric user ID when prompted
- Look at the camera and let it capture 100 face samples
- Press 'ESC' to stop early if needed

#### 5.2 Train the Model

```bash
python engine/auth/trainer.py
```

- This will process your face samples and create a trained model
- Wait for "Model trained" message

#### 5.3 Test Recognition (Optional)

```bash
python engine/auth/recognize.py
```

- Test if face recognition is working properly
- Press 'ESC' to exit

## 🎯 Running the Application

### Method : Using run.py

```bash
python run.py
```

## 🎮 Usage

1. **Launch**: Run `python run.py`
2. **Face Authentication**: Look at the camera for face recognition
3. **Voice Commands**: Click the microphone button or use hotword "Jarvis"
4. **Keyboard Shortcut**: Press `Win + J` to activate voice command

### Sample Voice Commands

- "Open Google"
- "Play [song name] on YouTube"
- "Send message to [contact name]"
- "What's my IP address?"
- "Check internet speed"
- "Take a screenshot"
- "What's the weather?"
- "Tell me a joke"
- "Shutdown the computer"

## 📱 Mobile Integration

For WhatsApp and SMS features:

1. Connect your Android device via USB
2. Enable USB Debugging
3. Run `device.bat` to setup ADB connection
4. Authorize the connection on your device

## 🔧 Configuration

### Database Setup

The application automatically creates `jarvis.db` with tables for:

- System commands
- Web commands
- Contacts

### Voice Settings

Modify voice properties in:

- Voice type
- Speech rate
- Volume

## 🛠️ Troubleshooting

### Common Issues

1. **Face Recognition Not Working**

   - Ensure you've run `sample.py` and `trainer.py`
   - Check if webcam is properly connected
   - Verify the `trainer.yml` file exists
2. **Voice Recognition Issues**

   - Check microphone permissions
   - Ensure stable internet connection
   - Adjust microphone sensitivity
3. **WhatsApp Features Not Working**

   - Verify ADB is installed and device is connected
   - Check USB debugging is enabled
   - Run `device.bat` to setup connection
4. **Web Interface Not Loading**

   - Check if port 8000 is available
   - Ensure Microsoft Edge is installed
   - Try running as administrator

## 📦 Dependencies

Key packages used:

- `eel` - Web interface
- `speech_recognition` - Voice recognition
- `opencv-python` - Face recognition
- `pyttsx3` - Text-to-speech
- `pyautogui` - GUI automation
- `speedtest-cli` - Internet speed testing
- `pywhatkit` - WhatsApp automation
- `hugchat` - AI chatbot

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenCV community for face recognition capabilities
- Google Speech Recognition API
- All open-source contributors

---

<div align="center">
  <p>Made with ❤️ by Hamza Meer</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>
