from django.db import models

# Create your models here.
class Word(models.Model):

    title = models.CharField(max_length=1000,unique=True)

    word1 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord1 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart1 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd1 = models.CharField(max_length=1000,default=None, blank=True)

    word2 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord2 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart2 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd2 = models.CharField(max_length=1000,default=None, blank=True)

    word3 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord3 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart3 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd3 = models.CharField(max_length=1000,default=None, blank=True)

    word4 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord4 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart4 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd4 = models.CharField(max_length=1000,default=None, blank=True)

    word5 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord5 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart5 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd5 = models.CharField(max_length=1000,default=None, blank=True)

    word6 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord6 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart6 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd6 = models.CharField(max_length=1000,default=None, blank=True)

    word7 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord7 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart7 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd7 = models.CharField(max_length=1000,default=None, blank=True)

    word8 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord8 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart8 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd8 = models.CharField(max_length=1000,default=None, blank=True)

    word9 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord9 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart9 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd9 = models.CharField(max_length=1000,default=None, blank=True)

    word10 = models.CharField(max_length=1000,default=None, blank=True)
    translatedWord10 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceStart10 = models.CharField(max_length=1000,default=None, blank=True)
    sentenceEnd10 = models.CharField(max_length=1000,default=None, blank=True)
    
    def __str__(self):
        return self.title
    