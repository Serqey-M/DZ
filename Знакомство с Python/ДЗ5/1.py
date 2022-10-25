# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'саббуфер сабвуфер абвиатура аббревиатура абведенный обведенный рабвладелец рабовладелец '
print(text)
text = text.split()
i = 0
while i < len(text):
    if 'абв' in text[i]:
        text.pop(i)
        i -= 1
    i += 1
text = ' '.join(text)
print(text)
