# emoticon_gen.py
import random
eyes_list = [':', ';', '>:', '<:']
nose_list = ['o', '-', '^']
mouth_list = [')', '(', 's', 'P', 'O']
emoticon_out = ''

for num in range(0, 5):
    emoticon_out = emoticon_out + random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list)
    emoticon_out = emoticon_out + '\n'
print(emoticon_out)
