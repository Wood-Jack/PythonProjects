#
# File Name:     hw13Project2_server (Holds the sever of the project)
# Programmer:    Woodrow Jackson
#
#
# Description: Compare the search times of linear search and binary search for the list sizes of 5000, 50000, and 500000
# For binary search to work the list must be sorted. Use the built-in python method to sort the list.
#
# Overall Plan:
#1. Forms the connnection
#2. Recives the message
#3. Reverses the message
#4. Close connections
#
#


import socket

#reverseing string
def stringReversal(input):

    reverseString = ''.join(reversed(input))
    return reverseString


def main():

    #create a socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()

    port = 3743


    #bind to port
    serverSocket.bind((host,port))

    # queue up to5 requests

    serverSocket.listen(5)


    #establish a connection
    address = serverSocket.accept()
    clientsocket = serverSocket.accept()

    #displaying the connenction

    print("Connection from:" .format(str(address)))


    while True:

        data = clientsocket.recv(1024).decode('ascii')

        if not data:
            break
        data = stringReversal(data)
        clientsocket.send(data.encode('ascii'))

    clientsocket.close()




main()


