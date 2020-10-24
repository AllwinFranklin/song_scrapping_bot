def v_o_f(file_name_txt):

    verse_order = []
    space = 1
    with open(file_name_txt, 'rb') as txt_file:
        for line in txt_file:
            txt = line.split(b'. ')
            if line == b'\n':
                space += 1
            if txt[0].isdigit():
                if txt[1].isdigit():
                    verse_order.append('v' + str(txt[0:1].decode("utf-8", "ignore")))
                else:
                    verse_order.append('v' + str(txt[0].decode("utf-8", "ignore")))
        txt_file.close()

    intro = space - len(verse_order)

    # if len(verse_order) == 0
    
    for i in reversed(range(1, intro+1)):
        verse_order.insert(0, 'i' + str(i))

    return verse_order