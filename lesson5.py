from colorama import *
'''
Fore   = AnsiFore() # Fore, це команда з допомогою якої ми можемо змінювати колір тексту.
Back   = AnsiBack() # Back, це команда з допомогою якої ми можемо змінювати колір фону тексту.
Style  = AnsiStyle() # Style, це команда з допомогою якої ми можемо змінювати стиль тексту.
'''
# Команди
CSI = '\033['
OSC = '\033]'
BEL = '\a'

def code_to_chars(code):
    return CSI + str(code) + 'm'

def clear_screen(mode=2): # ця функція очищує екран
    return CSI + str(mode) + 'J'

def clear_line(mode=2): # ця функція очищує лінію
    return CSI + str(mode) + 'K'

class AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.(підкласи оголошують атрибути класу, які є числами)
        # Upon instantiation we define instance attributes, which are the same(Після створення екземпляра ми визначаємо атрибути екземпляра, які однакові)
        # as the class attributes but wrapped with the ANSI escape sequence(як атрибути класу, але обгорнуті керуючою послідовністю ANSI)
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))

class AnsiFore(AnsiCodes): # Ось всі кольори в числах, для зрозумілості, та зручності
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

class AnsiBack(AnsiCodes): # Ось всі фони в числах, для зрозумілості, та зручності
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    class AnsiStyle(AnsiCodes): # Ось всі стилі в числах, для зрозумілості, та зручності
        BRIGHT = 1
        DIM = 2
        NORMAL = 22
        RESET_ALL = 0
