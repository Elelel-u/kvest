import random
import time
from random import randint as rn
import duck
import winsound
import threading


def play_music():
    winsound.PlaySound("utka.wav", winsound.SND_FILENAME)
music_thread = threading.Thread(target=play_music)


def kulonchek():
    winsound.PlaySound("kulon.wav", winsound.SND_FILENAME)
music = threading.Thread(target=kulonchek)


def _print(text=''):
    print(text)
    i=(input())
    if i=='вещи':
        inv_Nemo()


def inv_Nemo():
    if kulon==1:
        print('[кулон]\n')
        input()
    if shram==1:
        print('[стрёмненький шрам.\n   стрёмненький в меру возможностей моего зрения]')
        input()
    if golod==1:
        print('*негодующее урчание живота*')
        input()
    elif golod==0:
        print('[хм, мне тепло и сонливо.]')
        input()
    else:
        print('[у Вас пока ничего нет]')
        input()

    
def kvest_kulon():
    _print('С проволкой в руках решительно выхожу из-за стола.')
    _print('Подхожу к шкафу, опускаюсь на колени и лезу рукой в пыль и грязь.')
    _print('Через полминуты наконец нащупываю стеклянный шарик и аккуратно его выуживаю.')
    _print('Беру в руки плоскогубцы и...')
    music.start()
    time.sleep(1)
    input()
    input()
    input()
    _print('Немного времени, начинающих болеть пальцев и пара ошмётков некрасиво согнутой проволоки, красующихся на *кхм* полу и...')
    _print('|что-то подсказывает Вам проверить вещи|')
    global kulon
    kulon=1
    nach_Nemo()


def stol_Nemo():
    global stol
    if stol==0:
        print('На столе открытая пустая тетрадь, ручка и стеклянный кувшин с ромашками, принесёнными Мамой.')
        stol=stol+1
    elif stol<4:
        print('Всё те же стол, ручка и Мамины ромашки.')
    elif stol>=4:
        print('... ты фанат ромашек?')        
    b=input('1.Порыскать в ящиках стола\n2.Вернуться\n3.  вещи\n')
    if b=='1':
        if kulon==0:
            _print('В выдвижном ящике натыкаюсь на проволку и плоскогубцы.')
            _print('Вспоминаю чёрные кудри соседской дочери и появляется идея.')
            c=input('1.Соорудить подарок\n2.Вернуться\n')
            if c=='1':
                kvest_kulon()
            elif c=='2':
                nach_Nemo()
            else:
                print('Не понимаю тебя. Можешь повторить?')
                stol_Nemo()
        elif kulon==1:
            print('Тут нечего делать.')
            nach_Nemo()
    elif b=='2':
        nach_Nemo()
    elif b=='3':
        inv_Nemo()
        stol_Nemo()
    else:
        _print('Не понимаю тебя. Можешь повторить?')
        stol_Nemo()


def nach_Nemo():
    a=input('1. Рассмотреть комнату\n2. Рассмотреть содержимое стола\n3.  вещи\n')
    if a=='1':
        detskaya()
    elif a=='2':
        stol_Nemo()
    elif a=='3':
        inv_Nemo()
        nach_Nemo()
    else:
        _print('Не понимаю тебя. Можешь повторить?')
        nach_Nemo()


def detskaya():
    global detsk
    if detsk==0:
        print('Небольшая детская комната, из мебели кровать, стол, стул да шкаф.\nНебольшое окошко, которое я бы задвинул шторой целиком, да не умею писать вслепую.')
        detsk=1
    elif detsk==1:
        print('Мои спальня, рабочее место и столовая в одном флаконе.')
    e=input('1. Вернуться к столу\n2. Рассмотреть кровать\n3. Рассмотреть зашторенное окно\n4. Рассмотреть дверь\n5.  вещи\n')
    if e=='1':
        stol_Nemo()
    if e=='2':
        sleep_Nemo()
    if e=='3':
        _print('Хотите открыть окно?')
        _print('н')
        _print('е')
        _print('т')
        detskaya()
    if e=='4':
        kushat()
    if e=='5':
        inv_Nemo()
        detskaya()
    else:
        _print('Не понимаю тебя. Можешь повторить?')
        detskaya()


def kushat():
        global golod
        global shram
        print('В животе неприятно урчит.')
        j=input('За дверью не слышно ни Папы, ни Мамы.\n1. Остаться в детской\n2. Пойти приготовить поесть с шансом быть обнаруженным и наказанным\n3.  вещи\n')
        if j=='1':
            detskaya()
        if j=='2':
            _print('С опаской выхожу из комнаты.')
            _print('Мама оставила еду в сковородке.')
            _print('.')
            _print('.')
            _print('.')
            kitch=rn(1,40)
            if kitch<23:
                print('Греть еду в сковородке, не будучи способным различить цифры на электроплите, было глупо.\n')
                shram=1
                golod=0
                print('|Вы получили шрам.|')
                _print('|И ощущение сытости!|')
                detskaya()
            else:
                print('Уф, даже без боевых ранений!\n')
                shram=0
                golod=0
                detskaya()
        if j=='3':
            inv_Nemo()
            kushat()
        else:
            _print('Не понимаю тебя. Можешь повторить?')
            kushat()


def sleep_Nemo():
        global kryaaak
        if kryaaak==0:
            _print('Обыкновенная кровать. Мягкая и с милой "желтой" уточкой в изголовье.')
            _print('Помню, как сдавленно улыбнулся, когда мама ненароком проболталась о цвете подарка.')
            _print('Прищуриваюсь, смотря уточке в нарисованные глаза.')
            _print(duck.krya)
            music_thread.start()
            _print('Нервно сглатываю.')
            _print('Будем считать, что это случилось из-за моей сонливости.')
            kryaaak=1
        elif kryaaak==1:
            _print('Намеренно не смотрю на утку.')
            _print(' Как же клонит в сон...')
        h=input('|Завершить квест?|\n1. Завершить\n2. Вернуться\n3.  вещи\n')
        if h=='1':
            if kulon==1:
                _print('Сжимаю в руке подарок, заранее набираясь смелости подойти к Ней на перемене после второго урока.')
            if golod==1:
                print('Пусть и на голодный желудок,')
            elif golod==0:
                print('Сытый, пусть и прошедший через настоящее Кухонное Побоище,')
            _print('укладываюсь в кровать.')
            exit()
        elif h=='2':
            detskaya()
        elif h=='3':
            inv_Nemo()
            detskaya()
        else:
            _print('Не понимаю тебя. Можешь повторить?')
            sleep_Nemo()

            
kryaaak=0
golod=1
shram=0
kulon=0
stol=0
detsk=0
_print('__________\nВы можете открыть инвентарь, набрав "вещи" в любой момент игры,\nкроме выбора действий, где инвентарь можно открыть посредством выбора варианта "вещи"\n      Хорошей игры!\n__________')
_print('  Я - мальчик, заплакавший на первой странице "Книжного вора" Маркуса Зусака.')
_print(' Таких, как я, примерно ноль целых три стотысячных процента на Земле.')
_print('Мне 6 и у меня полная цветовая слепота.')
_print('И сочинения по литературе частенько заставляют меня вспомнить о своём недуге.')
_print('*стук ручки о дерево, скрип отодвинутого от стола стула*\n*зевок*')
nach_Nemo()
