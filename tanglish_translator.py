unicode_Mapping = { b'\xe0\xae\x85' : 'a',
                        b'\xe0\xae\x86' : 'aa',
                        b'\xe0\xae\x87' : 'i',
                        b'\xe0\xae\x88' : 'ii',
                        b'\xe0\xae\x89' : 'u',
                        b'\xe0\xae\x8a' : 'uu',
                        b'\xe0\xae\x8e' : 'e',
                        b'\xe0\xae\x8f' : 'ae',
                        b'\xe0\xae\x90' : 'ai',
                        b'\xe0\xae\x92' : 'o',
                        b'\xe0\xae\x93' : 'oa',
                        b'\xe0\xae\x94' : 'ow',
                        b'\xe0\xae\x83' : 'q',
                        
                        # 'ஂ' 'ா' 'ி' 'ீ' 'ு' 'ூ' 'ெ' 'ே' 'ை' 'ொ' 'ோ' 'ௌ' '்' 'ௗ'    
                        b'\xe0\xae\x82' : '-',
                        b'\xe0\xae\xbe' : '-aa',
                        b'\xe0\xae\xbf' : '-i',
                        b'\xe0\xaf\x80' : '-ii',
                        b'\xe0\xaf\x81' : '-u',
                        b'\xe0\xaf\x82' : '-uu',
                        b'\xe0\xaf\x86' : '-e',
                        b'\xe0\xaf\x87' : '-ae',
                        b'\xe0\xaf\x88' : '-ai',
                        b'\xe0\xaf\x8a' : '-o',
                        b'\xe0\xaf\x8b' : '-oa',
                        b'\xe0\xaf\x8c' : '-ow',
                        b'\xe0\xaf\x8d' : '-',
                        
                        #'க ங ச ஞ ட ண த ந ப ம ய ர ல வ ள ழ ற ன'
                        b'\xe0\xae\x95' : 'ka',
                        b'\xe0\xae\x99' : 'nGa',
                        b'\xe0\xae\x9a' : 'sa',
                        b'\xe0\xae\x9e' : 'Gna',
                        b'\xe0\xae\x9f' : 'da',
                        b'\xe0\xae\xa3' : 'Na',
                        b'\xe0\xae\xa4' : 'tha',
                        b'\xe0\xae\xa8' : 'na',
                        b'\xe0\xae\xaa' : 'pa',
                        b'\xe0\xae\xae' : 'ma',
                        b'\xe0\xae\xaf' : 'ya',
                        b'\xe0\xae\xb0' : 'ra',
                        b'\xe0\xae\xb2' : 'la',
                        b'\xe0\xae\xb5' : 'va',
                        b'\xe0\xae\xb3' : 'La',
                        b'\xe0\xae\xb4' : 'za',
                        b'\xe0\xae\xb1' : 'Ra',
                        b'\xe0\xae\xa9' : 'na',

                        # sanscript lettters ஷ ஸ ha ja
                        b'\xe0\xae\xb7' : 'sha',
                        b'\xe0\xae\xb8' : 'Sa',
                        b'\xe0\xae\xb9' : 'ha',
                        b'\xe0\xae\x9c' : 'ja',

                        # Symbols
                        b"'" : "'",
                        b'"' : '"',
                        b'.' : '.',
                        b'~' : '~',
                        b'`' : '`',
                        b'!' : '!',
                        b'@' : '@',
                        b'#' : '#',
                        b'$' : '$',
                        b'%' : '%',
                        b'^' : '^',
                        b'&' : '&',
                        b'*' : '*',
                        b'(' : '(',
                        b')' : ')',
                        b'-' : '-',
                        b'_' : '_',
                        b'=' : '=',
                        b'+' : '+',
                        b'[' : '[',
                        b']' : ']',
                        b'{' : '{',
                        b'}' : '}',
                        b':' : ':',
                        b';' : ';',
                        b'<' : '<',
                        b'>' : '>',
                        b'/' : '/',
                        b'|' : '|',
                        b'?' : '?',
                        b' ' : ' ',
                        b',' : ','

                        }

#t_t => tanglish_translator
def t_t(input_txt):
    temp_Mapped_str = ""
    for i in input_txt:
        temp_Mapped_str += unicode_Mapping[i.encode('utf-8')]
    # print (temp_Mapped_str)
    temp_Mapped_str = temp_Mapped_str[::-1]

    # removing - and a
    _removed_str = ""
    skipper = 0
    for i in range(0, len(temp_Mapped_str)):
        if temp_Mapped_str[i] == '-':
            skipper = 1
            continue
        if skipper > 0:
            skipper = 0
            continue
        _removed_str += temp_Mapped_str[i]

    skipper = 0
    crt_str = ""
    for i in range(0, len(_removed_str)):
        if skipper > 0:
            skipper -= 1
            continue
        if _removed_str[i] == 'R' and _removed_str[i+1] == 'R':
            crt_str += "rt"
            skipper = 1
            continue
        if _removed_str[i] == 'd' and _removed_str[i+1] == 'd':
            crt_str += "tt"
            skipper = 1
            continue
        if _removed_str[i] == 'i' and _removed_str[i+1] == 'i' and _removed_str[i+2] == 'n':
            crt_str += "ee"
            skipper = 1
            continue
        crt_str += _removed_str[i]

    crt_str = crt_str[::-1]

    return (crt_str.lower())

# answer = t_t('உகாண்')
# print(answer)
