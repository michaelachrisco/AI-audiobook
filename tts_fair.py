from TTS.api import TTS
import os
api = TTS(model_name="tts_models/eng/fairseq/vits").to("cuda")
api.tts_to_file("This is a test.", file_path=os.getcwd() + "/output.wav")

# TTS with on the fly voice conversion
api = TTS("tts_models/deu/fairseq/vits")
api.tts_with_vc_to_file(
    "Wie sage ich auf Italienisch, dass ich dich liebe?",
    speaker_wav=os.getcwd() + "/speaker.wav",
    file_path=os.getcwd() + "/ouptut.wav"
)
