from TTS.api import CS_API

# Init 🐸 Coqui Studio API
# you can either set the API token as an environment variable `COQUI_STUDIO_TOKEN` or pass it as an argument.

# XTTS - Best quality and life-like speech in EN
api = CS_API(api_token='AP4gY6XdhUOztV7o4t82NwQDiwjwrxcd9uG3qyN9wlkkvfvKQlCoqOh1gV1XsXsT', model="XTTS")
api.speakers  # all the speakers are available with all the models.
api.list_speakers()
api.list_voices()
wav, sample_rate = api.tts(text="This is a test.", speaker=api.speakers[0].name, emotion="Happy", speed=1.5)

# XTTS-multilingual - Multilingual XTTS with [en, de, es, fr, it, pt, ...] (more langs coming soon)
#api = CS_API(api_token=<token>, model="XTTS-multilingual")
#api.speakers
#api.list_speakers()
#api.list_voices()
#wav, sample_rate = api.tts(text="This is a test.", speaker=api.speakers[0].name, emotion="Happy", speed=1.5)

# V1 - Fast and lightweight TTS in EN with emotion control.
#api = CS_API(api_token=<token>, model="V1")
#api.speakers
#api.emotions  # emotions are only for the V1 model.
#api.list_speakers()
#api.list_voices()
#wav, sample_rate = api.tts(text="This is a test.", speaker=api.speakers[0].name, emotion="Happy", speed=1.5)
