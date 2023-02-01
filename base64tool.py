def removespace(input):

    nospace = input.replace(" ", "")

    return nospace
    
def texttobin(input):
    listedinput = []
    listedascii = []
    listedbin = []

    for i in range(len(input)):
        listedascii.append(ord(input[i]))
        listedbin.append(bin(listedascii[i]))
        listedbin = [y.replace('b', '') for y in listedbin]

        if len(listedbin) == len(input):
            return listedbin

def binblock(listedbin):
    strbin = ""
    block = []
    firstsix = 0
    secondsix = 6
    counter = 0

    for i in range(len(listedbin)):
        strbin += listedbin[i]
        
    for i in range(len(strbin)):
        firstbyte = strbin [firstsix:secondsix]

        if firstbyte == "":
            continue
        else:

            if (len(firstbyte)) != 6:
                firstbyte = firstbyte.ljust(6, '0')
        
            block.append(firstbyte)

        firstsix += 6
        secondsix += 6

    return block

def base64encodenum(listedblock):
    countlist = []
    totalcount = 0
    for i in range(len(listedblock)):
        
        blockseq = listedblock[i]

        if blockseq[0] == "1":
            totalcount += 32

        if blockseq[1] == "1":
            totalcount += 16

        if blockseq[2] == "1":
            totalcount += 8

        if blockseq[3] == "1":
            totalcount += 4

        if blockseq[4] == "1":
            totalcount += 2

        if blockseq[5] == "1":
            totalcount += 1

        countlist.append(totalcount)
        totalcount = 0

    return countlist

def base64encodealp(basenum):
    char1_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encode = []
    encodestr = ""

    for i in range(len(basenum)):
        numalp = char1_set[basenum[i]]
        encode.append(numalp)
        
    for i in range(len(encode)):
        encodestr += encode[i]
    
    calc = (len(encodestr)) % 4

    if calc != 0:
        for i in range(calc):
            encodestr += "="
            if (len(encodestr)) % 4 == 0:
                break

    return encodestr

def decrypt(encoded):

    char2_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encodedstrred = ""
    encode8bitlist = []
    cleaned = ""
    firsteight = 0
    secondeight = 8

    for i in range(len(encoded)):
        encdec = encoded[i]
        if encdec == "=":
            continue
        else:
            pos = char2_set.find(encdec)

            edit = bin(pos)[2:].zfill(6)

            encodedstrred += edit

    for i in range(len(encodedstrred)):
        temp = encodedstrred [firsteight:secondeight]

        if temp == "":
            continue
        else:
            encode8bitlist.append(temp)
            firsteight += 8
            secondeight += 8

    for i in range(len(encode8bitlist)):
        decodedascii = int(encode8bitlist[i], 2)
        asciireturn = chr(decodedascii)

        cleaned += asciireturn
    
    return cleaned

def main():
    while True:
        print("Base64 Encrytion + Decryption tool. ")
        print("Whitespaces are removed from the text before encryption. ")
        choice = input("(E)ncrypt or (D)ecrypt: ")

        if choice == "E":

            start = input("String: ")

            spacelessstr = removespace(start)
            listedbin = texttobin(spacelessstr)
            listedblock = binblock(listedbin)
            basenum = base64encodenum(listedblock)
            base64 = base64encodealp(basenum)

            print(f"Encrypted string: {base64}\n")
    
        if choice == "D":

            encoded = input("String: ")

            cleaned = decrypt(encoded)

            print(f"Decrypted string: {cleaned}\n")

#RUNIT
main()