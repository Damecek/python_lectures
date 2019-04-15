#!/usr/bin/env python3
"""implements log class"""
from datetime import datetime


class Log:
    def __init__(self, name, **kwargs):
        self.lName = name
        self.lvl = 0
        self.msg = [(0, 'Init of log\n', datetime.now()), kwargs]
        self.printers = []

    def set_level(self, lvl):
        self.lvl = lvl

    def log(self, lvl, msg, **kwargs):
        self.msg.append((lvl, msg + '\n', datetime.now(), kwargs))

    def add_printer(self, printer):
        self.printers.append(printer)

    def log_print(self):
        for msg in self.msg:
            if msg[0] >= self.lvl:
                for printer in self.printers:
                    printer.print(msg[1])
                    # printer.write(str(msg[0]) + ' lvl: ' + msg[1])


class Printer:
    def __init__(self):
        self.lvl = False
        self.date = False

    def print(self, log):
        if self.lvl:
            print(log[0] + ": ")
        if self.date:
            print(log[2] + ": ")
        print(log[1])
