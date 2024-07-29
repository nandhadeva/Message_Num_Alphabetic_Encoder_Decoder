alphabetToNum: dict = {
    4: "A",
    3: "E",
    1: "I",
    0: "O",
    5: "S",
    7: "T"
}

NumtoAlphabet: dict = {
    "A": 4,
    "E": 3,
    "I": 1,
    "O": 0,
    "S": 5,
    "T": 7
}


def encoder(get_message: str) -> str:
    message = get_message
    global alphabetToNum, NumtoAlphabet
    result: dict = dict(
        status=False,
        orginal_message=message,
        encoded_message=None
    )

    alphabetToNum_values = list(alphabetToNum.values())
    if not any(message for value in alphabetToNum_values if value in message or value.lower() in message):
        return result

    encode_message_formed = ''
    for char in message:
        if char in NumtoAlphabet or char.upper() in NumtoAlphabet:
            encode_message_formed = encode_message_formed + \
                str(NumtoAlphabet[char.upper()])
            continue
        encode_message_formed = encode_message_formed + char

    result.update({
        'status': True,
        'encoded_message': encode_message_formed
    })
    return result


def decoder(get_message: str) -> str:
    global alphabetToNum, NumtoAlphabet
    message = get_message
    result = dict(
        status=False,
        orginal_message=message,
        decoded_message=None
    )

    NumtoAlphabet_Values = list(NumtoAlphabet.values())
    if not any(message for value in NumtoAlphabet_Values if str(value) in message):
        return result

    decode_message_formed = ''
    for char in message:
        if char >= '0' and char <= '9':
            charToint = int(char)
            if charToint in alphabetToNum:
                decode_message_formed = decode_message_formed + \
                    alphabetToNum[charToint]
                continue
        decode_message_formed = decode_message_formed + char

    result.update({
        'status': True,
        'decoded_message': decode_message_formed
    })
    return result


if __name__ == "__main__":
    message = "Nandha kumar is developer"
    encoded_message = encoder(message)['encoded_message']
    print(decoder(encoded_message))
