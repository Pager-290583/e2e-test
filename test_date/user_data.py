import time
import random


class UserData:
    def __init__(self):

        self.email = f'oleg_kozlov_QA_Python+4_{random.randint(100, 999)}@yandex.ru'
        self.pas = f'123{random.randint(100, 999)}'
        self.pas_fail = f'1{random.randint(100, 999)}'
        self.name = f'Oleg_{time.time()}'
