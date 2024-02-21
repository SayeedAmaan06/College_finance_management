import pytesseract
import re

word_pattern = r"\b\w+\b"

def pytest(img):
    def textdetection():
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        text = pytesseract.image_to_string(img)
        return text
    words = re.findall(word_pattern, textdetection())
    for i in range(len(words)):
        if 'ID' in words[i] and 'ransaction' in words[i-1]:
            t = words[i+1]
        elif 'No' in words[i] and 'Ref' in words[i-1]:
            t = words[i+1]
    for i in range(len(words)):
        if '2024' in words[i]:
            dd = words[i-1],words[i-2],'2024'
            d = ' '.join(dd)
    return t,d