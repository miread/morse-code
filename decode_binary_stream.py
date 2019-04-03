from basic_decode import decodeMorse

def testBits(bits):
    time_test = []
    count = 0
    for bit in bits:
        if bit == "1":
            count += 1
        else:
            if count != 0:
                if count not in time_test:
                    time_test.append(count)
                count = 0
        if len(time_test) == 2:
            return sorted(time_test)[0]

    if count != 0:
                if count not in time_test:
                    time_test.append(count)
                count = 0
    for bit in bits:
        if bit == "0":
            count += 1
        else:
            if count != 0:
                if count not in time_test:
                    time_test.append(count)
                count = 0
    if len(time_test) == 1:
        return time_test[0]
    if len(time_test) == 2:
        if sorted(time_test)[0] * 2 == sorted(time_test)[1] or sorted(time_test)[0] * 3 == sorted(time_test)[1]:
            return sorted(time_test)[0]
    if len(time_test) == 3:
        return sorted(time_test)[0]

def decodeBits(content):
    bits = content
    while bits[0] == "0":
        bits = bits[1:]
    while bits[-1] == "0":
        bits = bits[:-1]
    time_unit = testBits(bits)
    output, storage = "", ""
    dict = {}
    dict["1" * time_unit] = "."
    dict["1" * time_unit * 3] = "-"
    dict["0" * time_unit] = ""
    dict["0" * time_unit * 3] = " "
    dict["0" * time_unit * 7] = "   "

    for bit in bits:
        if bit in storage or storage == "":
            storage += bit
        else:
            output += dict[storage]
            storage = bit
    output += dict[storage]
    return output


print(decodeMorse(decodeBits("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")))
