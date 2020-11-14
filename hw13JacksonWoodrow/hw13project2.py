#
#
# File Name:     hw13Project2 (client side)
# Programmer:    Woodrow Jackson
#
#
# Description: echo server the client side of it
#
# Overall Plan:
# 1. Create the connection to the server
# 2. Sends Message to the server
# 3. Recieves the message reversed
#

import socket

def main():

    # create a socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 3743
    #connecting to host name on the port

    serverSocket.connect((host, port))

    #Will get the input message from user
    messageInput = input("Enter a message or 'e' to Exit ")

    while messageInput[0].lower() != 'e':

        serverSocket.send(messageInput.encode('ascii'))

        data = serverSocket.recv(1024).decode('ascii')
        print("Message recevied:".format(data))

        messageInput= input("Enter a message or 'e' to exit")

    # close socket
    serverSocket.close()




main()