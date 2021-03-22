from colorama import Fore
import time


class TrafficLight:
    def __init__(self):
        self.__color = 'RED'

    def running(self):
        print(Fore.RED + self.__color)
        time.sleep(7)
        self.__color = 'YELLOW'
        print(Fore.YELLOW + self.__color)
        time.sleep(2)
        self.__color = 'GREEN'
        print(Fore.GREEN + self.__color)
        time.sleep(5)


light = TrafficLight()
light.running()
