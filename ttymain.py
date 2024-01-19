import os
os.environ["SUNO_USE_SMALL_MODELS"] = "True"
os.environ["SUNO_OFFLOAD_CPU"] = "True"

import bark

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
The Fae are always enthralled by something new and watched the negotiations with interest, wagering, and the hope of some entertainment. That had changed when the forbidden metal had been dumped from a magical bag into the Duchess's lands. The lesser fae were in pain, but the greater Fae Lords and Ladies might not survive. Only the barrier between the realms saved them. Even dying, they watched with interest and delight as the Duchess was humbled and the iron was put away.

The screams of pain subsided as the cold iron disappeared, replaced by the roar of battle and the spectacle of holy fire roaring from the skies. Finally, there was a moment of silence, where anyone with a bit of drama to their soul knew fateful words were being spoken before someone met their end. The crowd at the gate was enthralled and knew what was coming: the mortals would die, some souls would go to Hades, and some would not. Duchess Midnight would walk to her gates as if nothing had happened, maybe one hair out of place and the flush of exertion on her pale cheeks. She would look many of the Lords and Ladies in the eye, seeking any sort of rebellion, and then a feast would be held for no reason at all with her taking the seat of honor.

The scream as she died shocked nearly everyone. Normally, it would have been all anyone talked about in court for the next dozen seasons. But the Lords and Ladies would soon have other topics of interest to discuss as five mortals walked to the gates, weary and bloodied, the effects of thorn and poison showing on most of them. The lands of the Fae had not been kind to them, as it rarely is to mortals.

But their heads were held high, and Midnight was dead. Today, it was more a case of the mortals not treating the Fae lands kindly. Oberon didn't blame them. Their trusting nature had been taken advantage of; guest rights had been abused, and a hound attacked. Promises and business dealings had been cast aside in the anger of battle. They had tried to do a good deed, rescuing a fallen knight and bringing him home. Their kindness had been returned with malice.

Oberon had warned every fae, of high station or low, that travel in the mortal lands could be fraught with danger. Poisoning by iron, falling in love with a short-lived mortal, or siring children who would appear in the most inopportune times. It was a dangerous place. The fate of Prince Leporidon was a warning for even the mightiest of warriors. The death of Duchess Midnight was a lesson that no matter how dangerous and powerful you thought yourself, the mortal world still held brave heroes who could pull miracles out of their magic bags. Or, in this case, iron from the dawn of time.

The damnable iron was high on Oberon's mind now as the heroes walked to the gates of the lands formerly belonging to the Duchess. Beyond those were the common lands that formed thin buffers between neighboring realms. The common lands would melt quickly to the poison of that iron, and Oberon would be forced to expend far too much power to deal with it before all around him died and his own realm was damaged. He turned to the Sphynx standing nearby. "Princess Sahkmet, is the Butcher a reasonable man?"

She turned to him and smiled. "Who is asking?"

Oberon sighed, but the information had value, and so a price must be paid. Dealing with a creature older than himself was a rare experience for Oberon, and he was cautious around her. "The High King of the Fae who has far too many enchanted trinkets in his castle and would ask that you take a necklace of fire opals from him as a gift to ease his mind."

The Sphynx inclined her head. "The Butcher is a riddle that takes time to unravel. He was an inept and shy boy who only knew how to chop meat and grew up loving a little barmaid. In time, he journeyed far and learned from gods and titans. He gives council to Barons and Emperors. He gives warnings to those who cross him and is slow to anger unless his friends are threatened. But the warnings are backed up by a growing power. He is reasonable until he is pushed to be unreasonable." She paused for a moment, "And I advise you to treat the little barmaid well. He is at his most ferocious in her defense, as you just saw."

Oberon inclined his head, and a messenger from his court came running, quite out of breath, bearing a beautiful necklace the Sphynx allowed to be placed upon her. She purred as she looked at the necklace made of gold and hundreds of gems. "Your gift pleases me, King of the Fae. I will tell you more."

"These four mortals have traveled through other worlds before being reborn here. The Engine has taken notice of them and uses them to further its stories. This makes them interesting allies and crafty foes. The system rewards them when they overcome a dangerous challenge. I prefer them as allies, but then, I am only a silly kitten who likes her ribbons and baubles."

The King of the Fae was thankful he had offered one of the most expensive treasures in his vault. The Sphynx's words spurred him to caution where he might have relied on pride, and her declaration of an alliance was both clear and as pointed as her claws.

She continued. "And the gnome that walks with them is of Royal lineage, his style of clothing is at least seven centuries out of fashion, and his body language shows that he owes the barmaid a substantial debt."

The King had noticed the small figure but, preoccupied with the problem of dealing with the Butcher, had given him little thought. Now he did, and the conclusion chilled him. That could only be one person.
"""
audio_array = generate_audio(text_prompt, history_prompt="v2/en_speaker_1")

# save audio to disk
write_wav("butcher.wav", SAMPLE_RATE, audio_array)
  
# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)
