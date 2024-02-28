import easyocr
import re

reader = easyocr.Reader(['en', 'hi'])
def recognize_text(image):
    result = reader.readtext(image,paragraph=True)
    for i in result:
        for j in i:
            if 'र' in j:
                print("got it")
                amount = j
    def extract_numbers(text):
        """Extract numbers from a string"""
        numbers = re.findall(r'\d+', text)
        return (''.join(numbers))

    amt = extract_numbers(amount)

    hindi_to_english = {
        '०': '0', '१': '1', '२': '2', '३': '3', '४': '4', '५': '5', '६': '6', '७': '7', '८': '8', '९': '9'
    }

    def hindi_num_to_english(hindi_num):
        """Convert Hindi numbers to English"""
        return ''.join(hindi_to_english.get(char, char) for char in hindi_num)
    print(hindi_num_to_english(amt))
    return hindi_num_to_english(amt)
