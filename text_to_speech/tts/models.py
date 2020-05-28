from django.db import models
import tempfile
from django.core.files import File
from gtts import gTTS

 #Add the audio field to your model
class Tts(models.Model):
    text = models.TextField()
    lang = models.CharField(max_length=5)

    def save(self, *args, **kwargs):
        audio = gTTS(text=self.text, lang=self.lang, slow=False)

        #with tempfile.TemporaryFile(mode='wb') as f:
        #    audio.write_to_fp(f)
        file_name = '{}.mp3'.format(self.lang)
        audio.save("media/audio.mp3")

        super(Tts, self).save(*args, **kwargs)
