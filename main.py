import PyPDF2
import pyttsx3


pc_path = input("Input your pdf full path:")
path = open(f'{pc_path}.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

from_page = pdfReader.pages[0]

# extracting the text from the PDF
text = from_page.extract_text()

# reading the text
speak = pyttsx3.init()
voices = speak.getProperty("voices")
speak.setProperty("voice", voices[1].id)
speak.setProperty("rate", 110)
speak.say(text)
speak.runAndWait()
