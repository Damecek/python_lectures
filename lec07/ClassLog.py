#!/usr/bin/env python3
"""implements log class"""
import sys


class Log:
    printers = [sys.stdout]

    def __init__(self, name):
        self.lName = name
        self.lvl = 0
        self.msg = [(0, 'Init of log\n')]

    def set_level(self, lvl):
        self.lvl = lvl

    def log(self, lvl, msg):
        self.msg.append((lvl, msg + '\n'))

    def add_printer(self, printer):
        self.printers.append(printer)

    def log_print(self):
        for msg in self.msg:
            if msg[0] >= self.lvl:
                for printer in self.printers:
                    printer.write(str(msg[0]) + ' lvl: ' + msg[1])


logger = Log('test')
logger.log_print()
logger.set_level(3)
logger.log_print()
logger.log(1, 'sdfsdfDS')
logger.log(2, 'sdfsdfDS')
logger.log_print()
logger.set_level(2)
logger.log_print()
logger.log(5, 'sdfsd')
logger.set_level(1)
logger.log_print()
logger.add_printer(sys.stderr)
logger.log_print()

