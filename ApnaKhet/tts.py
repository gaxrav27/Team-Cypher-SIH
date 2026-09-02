import os
import base64
from sarvamai import SarvamAI

SARVAM_LANGUAGE_CODES = {
    "en": "en-IN",
    "hi": "hi-IN",
    "mr": "mr-IN",
}

DEFAULT_SPEAKER = "shubh"


def _get_client():
    api_key = os.environ.get("SARVAM_API_KEY")
    if not api_key:
        raise RuntimeError(
            "SARVAM_API_KEY is not set. Create a .env file in this folder "
            "(see .env.example) with SARVAM_API_KEY=your_key_here."
        )
    return SarvamAI(api_subscription_key=api_key)


def synthesize_speech(text, lang):
    if lang not in SARVAM_LANGUAGE_CODES:
        raise ValueError(f"Unsupported language for TTS: {lang}")

    if len(text) > 2500:
        text = text[:2500]

    client = _get_client()
    audio = client.text_to_speech.convert(
        text=text,
        model="bulbul:v3",
        language_code=SARVAM_LANGUAGE_CODES[lang],
        speaker=DEFAULT_SPEAKER,
    )

    audio_base64 = "".join(audio.audios)
    return base64.b64decode(audio_base64)
