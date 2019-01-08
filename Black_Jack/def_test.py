def ask_to_draw():
    anwser = 0
    while True:
        question = input('Would you like to take another card? Y/N')
        if question in ('y','Y'):
            return anwser
        elif question in ('n','N'):
            anwser =1
            return anwser
        else:
            continue

ask_to_draw()