class Solution:
    c = True
    def canConstruct(selfi, ransomNote, magazine):
        self = selfi
        for i in range(len(ransomNote)):
            if self == True:
                let = ransomNote[i]
                for i in range(len(magazine)):
                    if let == magazine[i]:
                        magazine = magazine[:i] + magazine[i + 1:]
                        self = True
                        break
                    else:
                        self = False
            else:
                break
        return self

    ransomNote = str(input())
    magazine = str(input())

    print(canConstruct(c, ransomNote, magazine))


