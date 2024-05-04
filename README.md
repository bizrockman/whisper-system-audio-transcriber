
# PC Audio Transcription Tool

This repository contains a Python script designed to record audio directly from your computer's system output and transcribe it into text. The script is particularly useful for transcribing audio from various sources such as movies, YouTube shorts, voice messages from platforms like Telegram or WhatsApp, and even game sounds. It simplifies the process of capturing and converting system audio output to text using a spacebar-controlled recording mechanism.

## Features

- **Simple Control**: Start and stop recording with the spacebar.
- **Audio Transcription**: Transcribes the audio using OpenAI's Whisper model.
- **Flexible Source Input**: Compatible with various audio sources that can be routed through the PC's output.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bizrockman/whisper-system-audio-transcriber.git
   ```
2. Navigate to the project directory:
   ```bash
   cd whisper-system-audio-transcriber
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

To capture audio from your PC's output, ensure that you have configured "Stereo Mix" as the recording device on Windows or are using a Virtual Audio Cable setup. This will allow the system's audio output to be used as an input for recording.

## Usage

Run the script from the command line:

```bash
python app.py
```

Press and hold the spacebar to start recording and release it to stop. The recording will be saved, and its transcription will be displayed in the console.

## Configuration

Store your OpenAI API key in a `.env.local` file in the project root with the following content:

```
OPENAI_API_KEY='your_openai_api_key_here'
```

## License

This project is open-sourced under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or encounter problems.
