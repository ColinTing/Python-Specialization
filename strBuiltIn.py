str = 'ABC'
print(str.capitalize())

text = "X-DSPAM-Confidence:    0.8475"

pos = text.find('0.8475')
print(float(text[pos:]))
