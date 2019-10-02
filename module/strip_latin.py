import json
def strip_latin(authors):
    c_table = {192:'A',193:'A',194:'A',195:'A',196:'AE',197:'A',
        198:'AE',199:'C',200:'E',201:'E',202:'E',203:'E',
        204:'I',205:'I',205:'I',206:'I',207:'I',
        208:'D',209:'N',210:'O',211:'O',212:'O',213:'O',214:'O',216:'O',
        217:'U',218:'U',219:'U',220:'U',
        221:'Y',223:'ss',
        224:'a',225:'a',226:'a',227:'a',228:'a',229:'a',230:'ae',
        231:'c',232:'e',233:'e',234:'e',235:'e',
        236:'i',237:'i',238:'i',239:'i',
        240:'o',241:'n',242:'o',243:'o',244:'o',245:'o',246:'o',248:'o',
        249:'u',250:'u',251:'u',252:'u',253:'y',255:'y'}

    authors_c = {}

    for k,v in authors.items():
        string = k
        for character in string:
            if ord(character) > 0x007a:
                k = k.replace(character,c_table[ord(character)])
        authors_c[k] = v

    return authors_c