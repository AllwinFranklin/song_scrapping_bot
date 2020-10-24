from datetime import datetime
from datetime import date
import time

def writer(file, str):
    file.write(str.encode('utf-8'))

def x_m (file, head_content, head_content_tamil, web_lyric_content, verse_order):

    verse_order_str = ""
    for i in verse_order:
        verse_order_str += str(" " + i)

    # XML file writer
    writer(file, "<?xml version='1.0' encoding='UTF-8'?>\n")
    writer(file, '<song xmlns="http://openlyrics.info/namespace/2009/song" version="0.8" createdIn="OpenLP 2.4.6" modifiedIn="OpenLP 2.4.6" modifiedDate="')
    writer(file, str(date.today()) + 'T' + str(datetime.now().time().strftime("%H:%M:%S")) + '">\n')
    writer(file, '  <properties>\n')
    writer(file, '    <titles>\n')
    writer(file, '      <title>' + head_content + '</title>\n')
    writer(file, '      <title>')
    file.write(head_content_tamil)
    writer(file, '</title>\n')
    writer(file, '    </titles>\n')
    writer(file, '    <verseOrder>')
    writer(file, verse_order_str.lstrip())
    writer(file, '</verseOrder>\n')
    writer(file, '    <authors>\n')
    writer(file, '      <author>unknown</author>\n')
    writer(file, '    </authors>\n')
    writer(file, '  </properties>\n')

    # lyrics
    writer(file, '  <lyrics>\n')
    for lines, v_o in zip(web_lyric_content.text.split('\n\n'), verse_order):
        writer(file, '    <verse name="')
        writer(file, v_o)
        writer(file, '">\n')
        writer(file, '      <lines>')
        writer(file, lines.replace('\n', "<br/>"))
        writer(file, '</lines>\n')
        writer(file, '    </verse>\n')
    writer(file, '  </lyrics>\n')
    writer(file, '</song>')