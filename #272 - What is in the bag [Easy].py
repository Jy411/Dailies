# https://www.reddit.com/r/dailyprogrammer/comments/4oylbo/20160620_challenge_272_easy_whats_in_the_bag/

tileCount = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2,
    'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2
}


def scrabbleTileCounter(tilesInPlay):
    tilesInPlay = list(tilesInPlay)
    print(tilesInPlay)
    for tile in tilesInPlay:
        tileCount[tile] = tileCount[tile] - 1
        if tileCount[tile] < 0:
            print('Invalid Input. More', tile, '\'s has been taken from the bag than possible.')
            exit()
    output = {}
    for tile, count in tileCount.items():
        if count not in output:
            output[count] = []
        output[count].append(tile)
    for key in sorted(output, reverse=True):
        print("%s: %s" % (key, ', '.join(sorted(output[key]))))


scrabbleTileCounter('AXHDRUIOR_XHJZUQEE')