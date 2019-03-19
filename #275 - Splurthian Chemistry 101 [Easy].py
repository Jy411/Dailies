# https://www.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/


def verifySymbol(chemical, symbol):
    chemical = list(chemical)
    chemical = [x.lower() for x in chemical]
    symbol = list(symbol)
    if chemical.index(symbol[0].lower()) >= 0:
        if chemical.index(symbol[1].lower(), chemical.index(symbol[0].lower())) >= 0:
            print(''.join(chemical), ",", ''.join(symbol), "-> true")
        else:
            print(''.join(chemical), ",", ''.join(symbol), "-> false")


verifySymbol("Venkmine", "Kn")