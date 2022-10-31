# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
def compression(text):
    text1 = ''
    i = 1
    while i < len(text):
        if text[i] == text[i-1]:
            j = 2
            while i < len(text) and text[i] == text[i-1]:
                temp = str(j)+text[i]
                i += 1
                j += 1
        elif (i == len(text)-1):
            temp = '1'+text[i]
            i += 1
        elif text[i] == text[i+1]:
            i += 1
            temp = ''
        else:
            temp = '1'+text[i]
            i += 1
        text1 += temp
    return text1


def recovery(text):
    i = 0
    text2 = ''
    while i < len(text)-1:
        temp = ''
        while (text[i].isdigit() == True):
            temp += text[i]
            i += 1
        else:
            temp = int(temp)
        text2 += text[i]*temp
        i += 1
    return text2


# file = open('1.txt', 'r')
file = open('2.txt', 'r')
text = file.read()
file.close()
print(text)

# print(compression(text))
print(recovery(text))

# file2 = open('2.txt', 'w')
file2 = open('1.txt', 'w')
# file2.writelines(compression(text))
file2.writelines(recovery(text))
file.close()