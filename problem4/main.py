def ubah_huruf(sentence):
    pattern = ""
    huruf1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    huruf2 ="KLMNOPQRSTUVWXYZABCDEFGHIJ"
    for i in range(len(sentence)):
        if sentence[i] in huruf1:
            convert = huruf2[huruf1.index(sentence[i])]
        else:
            convert = sentence[i]
        pattern += convert
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB