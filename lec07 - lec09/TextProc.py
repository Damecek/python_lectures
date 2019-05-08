#!/usr/bin/env python3
"""text processing"""

import abc


class Processor:
    def __init__(self):
        self.text = ""
        self.plugs = []
        self.methods = [ToUpper(), ToLower(), Capitalize()]

    def read(self, arg):
        self.text = arg[0]
        self.plugs = arg[1:]

    def apply_plugs(self):
        for m in self.methods:
            if m.iden in self.plugs:
                self.text = m.process(self.text)

    def write(self):
        print(self.text)


class Plug(abc.ABC):
    def __init__(self, iden):
        self.iden = iden

    @abc.abstractmethod
    def process(self, text):
        return

    @abc.abstractmethod
    def iden(self):
        return


class ToUpper(Plug):
    def __init__(self):
        super().__init__("TU")

    def process(self, text):
        return text.upper()

    def iden(self):
        return self.iden


class ToLower(Plug):
    def __init__(self):
        super().__init__("TL")

    def process(self, text):
        return text.lower()

    def iden(self):
        return self.iden


class Capitalize(Plug):
    def __init__(self):
        super().__init__("Ca")

    def process(self, text):
        return text.capitalize()

    def iden(self):
        return self.iden


p = Processor()
p.read('sfsfasfsJHASD TL'. split())
p.apply_plugs()
p.write()
