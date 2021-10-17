from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt
from Hyperlink import add_hyperlink


# word document - open and set normal styles for whole document
def titleGenerator(indexDict, path):
    doc = Document()
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    style.element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')  # Independently change the Chinese font name!!*
    font.size = Pt(12)

    for title, url in indexDict.items():
        para = doc.add_paragraph()
        hyperlink = add_hyperlink(para, url, title)

    doc.save(path)
