import itertools

def bruteForce(pattern, maxLen):
    for length in range(1, maxLen + 1):
        for guess_tuple in itertools.product(pattern, repeat=length):
            guess = list(guess_tuple)
            if comperator(guess):
                return ''.join(guess)  

def comperator(guess, answer="pass"):
    if len(guess) != len(answer):
        return False
    for i in range(len(guess)):
        if guess[i] != answer[i]:
            return False
    return True

myPattern = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print(bruteForce(myPattern, 8))
