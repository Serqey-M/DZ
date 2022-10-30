# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
file = open('1.txt', 'r')
text = file.read()
file.close()
print(len(text))
text1=''
i=1
while i<len(text)-1:
    if text[i]==text[i-1]:
        j=1
        while text[i]==text[i-1] and i<len(text)-1:
            j+=1
            i+=1
            print(f'i={i} j={j}')
            temp=text1+str(j)+text[i-1]
            print(temp)
    else:
        temp=text1+'1'+text[i]
        i+=1
    text1+=temp
    print(text1)



    # print(f'i={i}')
    # j=1
    # while text[i]==text[i+1]:
    #     print(f'j={j}')
    #     j+=1
    #     i+=1
    #     print(f'{j} {text[i]}')
    # i+=1
# print(text1)