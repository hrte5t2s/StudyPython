import docx
from docx import Document
path = "I:\\test.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)