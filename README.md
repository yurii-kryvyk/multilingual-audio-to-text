# Multilingual Audio Transcription

Python application for offline Multilingual Audio-to-Text Conversion using Faster-Whisper from OpenAI

## Features
- Recognition of multiple languages within a single dialogue
- Offline speech transcription
- Automatic language detection
- Timestamped transcript
- Uses Faster-Whisper from OpenAI
- Automatic CPU/GPU selection (`device="auto"`)

---

## Requirements

- Python 3.11 or newer
- Windows, Linux or macOS

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yurii-kryvyk/multilingual-audio-to-text.git
cd multilingual-audio-to-text
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
project/
│
├── data/
│   └── audio.mp3
│
├── output/
│   └── transcript.txt
│
├── src/
│   └── engine.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Hardware Check

Before running the application, you can verify that Faster-Whisper is installed correctly and that the Whisper model can be loaded.

Run:

```bash
python test.py
```

The test will:

* verify that Faster-Whisper is installed;
* load the Whisper model;
* display the selected device (`cuda` or `cpu`);
* display the selected compute type;
* print the full error message if initialization fails.

If the output shows:

```text
Device: cuda
```

the model has been initialized on the NVIDIA GPU.

If the output shows:

```text
Device: cpu
```

the application is running on the CPU.

## Usage

Place your audio file into the `data` folder.

Rename it to:

```
audio.mp3
```

Run the program:

```bash
python main.py
```

The transcript will be saved to:

```
output/transcript.txt
```

---

## Model

Default model:

```
large-v3-turbo
```

You can change the model in `src/engine.py`:

```python
MODEL_SIZE = "large-v3-turbo"
```

Available models:

- tiny
- base
- small
- medium
- large-v3
- large-v3-turbo

---

## Configuration

Current settings:

```python
DEVICE = "auto"
COMPUTE_TYPE = "int8"
BEAM_SIZE = 5
```

### DEVICE

`auto`

Automatically selects:

- NVIDIA GPU (CUDA) if available
- otherwise CPU

---

### COMPUTE_TYPE

Current value:

```
int8
```

Provides a good balance between speed and memory usage.

---

### BEAM_SIZE

Current value:

```
5
```

Higher values generally improve transcription quality but increase processing time.

---

## GPU Support

The application automatically uses an NVIDIA GPU if available.

To enable GPU acceleration you need:

- NVIDIA GPU
- Latest NVIDIA driver
- CUDA Toolkit
- cuDNN

If CUDA is not available, Faster-Whisper automatically falls back to CPU.

---

## Tested Environment

Python 3.11

Faster-Whisper 1.2.0

CTranslate2 4.8.1

ONNX Runtime 1.27.0

---

## Notes

The first launch may take several minutes because the Whisper model is downloaded from Hugging Face.

After downloading, the model is cached locally and future launches are much faster.

---

## License

MIT License