import traceback
from pathlib import Path
from src.engine import run_transcription


def main() -> None:

    input_file = Path("data/audio.mp3")
    output_file = Path("output/transcript.txt")

    if not input_file.is_file():
        print(
            f"Error: File '{input_file}' not found.\n"
            "Please place the audio file into the 'data' folder."
        )
        return

    try:
        print(f"Starting transcription for: {input_file.name}")

        run_transcription(input_file, output_file)

        print(f"\nSuccess! Transcript saved to '{output_file}'.")

    except Exception:

        print("\n--- AN ERROR OCCURRED ---")
        traceback.print_exc()
        input("\nPress Enter to close...")


if __name__ == "__main__":
    main()