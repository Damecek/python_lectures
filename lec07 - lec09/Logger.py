#!/usr/bin/env python3
"""implements log class"""
from datetime import datetime
import abc
from enum import Enum
import time


class Lvl(Enum):
    SEVERE = 1
    WARNING = 2
    INFO = 3
    FINE = 4
    FINER = 5
    FINEST = 6


class Msg:
    def __init__(self, val, lvl):
        self.val = val
        self.lvl = lvl
        self.time = datetime.now()


class Logger:
    def __init__(self, name):
        self.lName = name
        self.lvl = Lvl(1)
        self.msg = []
        self.printers = []
        self.formatter = BasicFormatter()

    def set_level(self, lvl):
        self.lvl = lvl

    def log(self, msg):
        self.msg.append(msg)

    def add_printer(self, printer):
        self.printers.append(printer)

    def set_formatter(self, formatter):
        self.formatter = formatter

    def log_print(self):
        for msg in self.msg:
            if msg.lvl.value >= self.lvl.value:
                for p in self.printers:
                    p.print(p, self.formatter.format(msg))

# --------------enum


class Printer(abc.ABC):
    @abc.abstractmethod
    def print(self, text):
        return


class StdPrinter(Printer):
    def __init__(self):
        pass

    def print(self, text):
        print(text)


class FilePrinter(Printer):
    def __init__(self, file):
        self.file = file

    def print(self, text):
        with open(self.file, "a") as f:
            f.write(text)


# -------------------------


class Formatter(abc.ABC):
    @abc.abstractmethod
    def format(self, msg):
        return


class DateFormatter(Formatter):
    def __init__(self):
        self.startTime = datetime.now()

    def format(self, msg):
        cd_s = str((msg.time - self.startTime).seconds)
        cd_ms = str((msg.time - self.startTime).microseconds // 1000)
        return datetime.strftime(msg.time, '%Y-%m-%d %H:%M') + " <- " + cd_s + "." + cd_ms + " :: " + msg.val


class LvlFormatter(Formatter):
    def format(self, msg):
        return "Priority: " + msg.lvl.name + " | " + msg.val


class BasicFormatter(Formatter):
    def format(self, msg):
        return msg



fLog = Logger.Logger("my loger")
fLog.add_printer(StdPrinter)
fLog.set_formatter(DateFormatter())
fLog.log(Msg("first log", Lvl(2)))
fLog.log(Msg("loff  f", Lvl(4)))

time.sleep(1)

fLog.log(Msg("sdfpsdfpdsf", Lvl(5)))
fLog.log_print()

print("reseting lvl")
fLog.set_level(Lvl(4))
fLog.log(Msg("sdfsdf", Lvl(3)))
fLog.log_print()

print("resetign formater")
fLog.set_formatter(LvlFormatter())
fLog.log_print()
