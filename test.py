import traceback
from faster_whisper import WhisperModel


print("--- Starting Faster-Whisper check ---")

try:
    print("Importing library...")
    print("Import successful.")

    print("Initializing model (large-v3-turbo)...")

    model = WhisperModel(
        "large-v3-turbo",
        device="auto",
        compute_type="int8",
    )

    print("Model loaded successfully!")
    print(f"Device: {model.model.device}")
    print(f"Compute type: {model.model.compute_type}")

except Exception:
    print("\n!!! AN ERROR OCCURRED !!!")
    traceback.print_exc()

finally:
    print("\n--- Check completed ---")