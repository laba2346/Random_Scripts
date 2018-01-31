from collections import Counter
import re


def main():
    alphabetVals = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11,
        'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23,
        'y':24, 'z':25}
    p = [0.080, 0.015, 0.030, 0.040, 0.130, .020, 0.015, 0.060, 0.065, 0.005, 0.005,
            0.035, 0.030, 0.070, 0.080, 0.020, 0.002, 0.065, 0.060, 0.090, 0.030,
            0.010, 0.015, 0.005, 0.020, 0.002]
    ciphertext = input('Enter ciphertext: ').lower()
    ciphertext = re.sub(' ', '', ciphertext)
    totalChars = len(ciphertext)
    freq = Counter(ciphertext)
    for key,value in freq.items():
        freq[key] = value/totalChars
    print(ciphertext)
    print(freq)
    results = []
    for i in range(0,26):
        print("i = {}".format(i))
        result = 0
        for letter,fc in freq.items():
            c = alphabetVals[letter]
            cMinusI = 0
            if(c-i < 0):
                cMinusI = 26+(c-i)
            else:
                cMinusI = c-i
            result += fc*p[cMinusI]
            #print("{}*p({}-{}) + ".format(fc, c, i), end="")
        results.append(result)

        #print("\n\n\n\n")
    results = [round(i, 5) for i in results]
    print(results)
    print(sorted(results))




if(__name__ == "__main__"):
    main()
