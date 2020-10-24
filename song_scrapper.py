from selenium import webdriver
import tanglish_translator
import verse_order_finder
import xml_maker
import os

#bot = firefox webdriver object to open and control the browser
options = webdriver.ChromeOptions()
bot = webdriver.Chrome('chromedriver.exe', options=options)
folder_name = 'scrapped_song'
os.makedirs('./'+ folder_name, exist_ok=True)

with open("song_link_main.txt", 'r') as link_file:
    os.chdir('./scrapped_song/')
    os.makedirs('./Raw text/', exist_ok=True)
    os.makedirs('./OpenLP/', exist_ok=True)
    os.makedirs('./MediaShout/', exist_ok=True)
    # looping through links from the song_link_main text file
    for i in link_file:
        try:
            bot.get(i)
        except:
            print("No Internet Connection detected.\nBot couldn't function - Stopping")
            exit(0)

        '''
        encoding tamil text to binary encoded values
        Only can be written inside a file which is opened in a binary format
        '''
        web_lyric_heading = bot.find_element_by_id("ctl00_MainContent_lblHeading")
        web_lyric_content = bot.find_element_by_id("ctl00_MainContent_lblPost")

        head_content = tanglish_translator.t_t(web_lyric_heading.text)
        head_content_tamil = web_lyric_heading.text.encode('utf-8')
        song_content = web_lyric_content.text.encode('utf-8')
        verse_order = []
        file_name_xml = (head_content + '.xml')
        file_name_txt = (head_content + '.txt')
        os.chdir('./Raw text/')
        with open(file_name_txt, 'wb') as file_txt:
            file_txt.write(song_content)
            file_txt.close()

        verse_order = verse_order_finder.v_o_f(file_name_txt)
        os.chdir('..')

        os.chdir('./OpenLP')
        with open(file_name_xml, 'wb') as file:
            xml_maker.x_m(file, head_content, head_content_tamil, web_lyric_content, verse_order)
            file.close()
        os.chdir('..')
        
        print(head_content)
