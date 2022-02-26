def DecimalToBinary(DecimalNumber):  # d2k
    kvalue = ""
    mapping = "01"
    while DecimalNumber > 0:
        kvalue = mapping[DecimalNumber % 2] + kvalue
        DecimalNumber //= 2

    return "{:0>8}".format(kvalue)


test = [18, 0, 255, 128, 64]

for i in test:
    print(DecimalToBinary(i))
print("")


def BitShift(binaryString):
    try:
        if len(binaryString) != 8:
            raise ValueError
        for i in binaryString:
            if i not in ["1", "0"]:
                raise ValueError
    except:
        print("Error occured, invalid 8-bit binary string.")

    # shift one place to left

    newstring = binaryString[1:] + binaryString[0]
    print(newstring)
    return newstring


# 1.3 suitable tests

# 1.4 encryption

def encrypt(word):
    final = []
    for char in word:
        converted = BitShift(DecimalToBinary(ord(char) + 1))
        final.append(converted)

    for char in final:
        print(char, end=" ")


encrypt("AM")
