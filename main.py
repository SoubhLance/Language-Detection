from langdetect import detect

def detect_language(text):
    return detect(text)


text = "வணக்கம்"

codes = {
 'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Language',
 'sq': 'Albanian', 'bn': 'Bangla', 'bh': 'Bhojpuri',
 'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
 'cze': 'Czech', 'dan': 'Danish', 'ger': 'German', 'eg': 'Egyptian', 'en': 'English',
 'fre': 'French', 'gon': 'Gondi', 'grc': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
 'ind': 'Indonesian', 'ita': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
 'kas': 'Kashmiri', 'geo': 'Georgian', 'kor': 'Korean', 'lat': 'Latin',
}
print("The language of the text is:", codes[detect_language(text)])
