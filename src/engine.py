from pathlib import Path
from faster_whisper import WhisperModel


MODEL_SIZE = "large-v3-turbo"
DEVICE = "auto"
COMPUTE_TYPE = "int8"



def run_transcription(audio_path: Path, output_path: Path) -> None:

    if not audio_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print(f"Loading model '{MODEL_SIZE}' (this may take some time)...")

    try:
        model = WhisperModel(
            MODEL_SIZE,
            device=DEVICE,
            compute_type=COMPUTE_TYPE,
        )
    except Exception as e:
        raise RuntimeError(
            f"Unable to load Whisper model '{MODEL_SIZE}': {e}"
        ) from e

    print("Model loaded successfully!")
    print("Starting transcription...")

    try:
        segments, info = model.transcribe(
            str(audio_path),
            multilingual=True,
            beam_size=5,
            condition_on_previous_text=False,
        )
    except Exception as e:
        raise RuntimeError(f"Transcription failed: {e}") from e

    print(
        f"1-st detected language: "
        f"{info.language} "
        f"({info.language_probability:.1%})"
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        for segment in segments:
            line = (
                f"[{segment.start:.2f}s -> "
                f"{segment.end:.2f}s] "
                f"{segment.text}"
            )

            print(line)
            file.write(line + "\n")

    print(f"\nTranscription successfully saved to '{output_path}'.")