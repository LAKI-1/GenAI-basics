from translate import Translator

translator = Translator(to_lang='it')

#Text to be translated
text = 'Hello, how are you?'

# Perform the translation
translated = translator.translate(text)

# Perform the translation
print('Translated Text:', translated)