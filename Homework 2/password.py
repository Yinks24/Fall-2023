password_text = input()
#replace fuction updates the character
password_text = password_text.replace('i','!')
password_text = password_text.replace('a','@')
password_text = password_text.replace('m','M')
password_text = password_text.replace('B','8')
password_text = password_text.replace('o','.')

password_text = password_text + 'q*s'

print(password_text)
