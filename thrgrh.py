

from xml.dom.expatbuilder import FilterVisibilityController


def game():
    progrees = True
    word = 'апельсин'
    lifes = 3
    template = start_template(word)
    welcome_speech (template)
    
    while progrees:
        user_guess = input ('введите букву ')
        template = build_template (template, word, user_guess)
        print (template)
#         guessed = list_to_string_convert (template)
#         print_result (guessed)
        progrees = check_win (template)
        
        if not check_mistake(word,user_guess):
            lifes-=1
            print (lifes)
        
        if lifes==0:
            break
            
def check_mistake (w,g):
    flag = False
    if g in w:
        flag= True
    return flag
def check_win (t):
    if "#" in t:
        return True
    else:
         return False


def welcome_speech(t):
    print(f'''
    Добро пожаловать в игру - hangman 2000
    Ваша задача угадать загаданное слово за несколько попыток,
    иначе вас ждет расплата! Загаданное солво состоит из {len (t)} букв {t}''')

def start_template(w):
    return '#' * len(w)

def build_template (t,w, g=''):
    t=list (t)
    for i in range (len(w)):
        if t [i] =='#':
            if w [i]== g:
                t [i]= w [i]
            # else:
            #     t [i] = '#'
    return t

game()
