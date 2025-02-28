from textblob import TextBlob

text = 'I love progamming and Machine Learnnig.'
blob = TextBlob(text)

corrected_text = blob.correct()
print('Orginal Text: ',text)
print('Corrected Text: ',corrected_text)
