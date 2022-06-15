{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """\
Max Scott\
word to song\
\
"""\
from music import *\
soundscapeScore = Score("Loutraki Soundscape", 60)\
minPitch = 0        # MIDI pitch (0-127)\
maxPitch = 127\
words = "hello world"\
asciiList = []\
notList = []\
phrase = Phrase()  \
for charicter in words:\
      #ord gets the ascii value of a charicter\
   asciiList.append(ord(charicter))\
   note = Note(ord(charicter), HN, 127)\
   phrase.addNote(note)\
   soundscapePart.addPhrase(phrase)\
print(asciiList)\
Play.midi(soundscapeScore)\
}