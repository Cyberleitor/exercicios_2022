normal_word = input().lower()

normal_word_list = [indice.strip() for indice in normal_word if indice.strip() != '']
odd_word_list = [indice.strip() for indice in normal_word if indice.strip() != '']

odd_word_list.reverse()

if normal_word_list == odd_word_list:
    print(f'The word – {normal_word} – is a palindrome.')
else:
    print(f'The word – {normal_word} – is not a palindrome.')
