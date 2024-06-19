# Importing langdetect library
from langdetect import detect

# Function to detect the language of a sentence
def detect_language(text):
    return detect(text)

# The Sentence
text = "வணக்கம்"

# Dictionary of some famous Languages and their respective codes
codes={
 'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Langauge',
 'sq': 'Albanian','bn': 'Bangla', 'bh': 'Bhojpuri',
'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
 'cze': 'Caech', 'dan': 'Danish', 'ger': 'German', 'eg': 'Egyptian', 'en': 'English',
 'fre': 'french', 'gon': 'Gondi', 'grc': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
 'ind': 'Indonesian', 'ita': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
 'kas': 'Kashmiri', 'geo': 'Georgian', 'kor': 'Korean', 'lat': 'Latin',
 'mar': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'dut': 'Dutch',
'te': 'Telugu', 'ta': 'Tamil','cy':'Welsh'}

print("The language of the text is:", codes[detect_language(text)])