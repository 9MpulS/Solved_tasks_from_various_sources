class Solution:
    c = True    # не нужная переменная

    def canConstruct(selfi, ransomNote, magazine):  # selfi требует литкод(функция должна принимать 3 переменных)
        self = selfi
        for i in range(len(ransomNote)):  # Перебераем буквы в записке
            if self == True:
                let = ransomNote[i]
                for i in range(len(magazine)):   # перебираем буквы в журнале
                    if let == magazine[i]:   # если находим то удаляем ее и заканчиваем поиск в журнале
                        magazine = magazine[:i] + magazine[i + 1:]
                        self = True
                        break
                    else:
                        self = False
            else:
                break
        return self

    ransomNote, magazine = str(input()), str(input())

    print(canConstruct(c, ransomNote, magazine))


