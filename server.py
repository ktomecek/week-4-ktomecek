##################################################################################
# Written/Modified by Karl Tomecek 05/31/2019                                    #
# Program Name: server.py                                                        #
# Week 4 Assignment                                                              #
# Comments: Modeled from code retrieved from                                     #
# https://stackoverflow.com/questions/7749341/basic-python-client-socket-example #
#                                                                                #
##################################################################################

#Import Socket library
import socket


def clearScreen():
    for i in range(15): #clear the screen
        print('\n')

def main():
    #'Clear' the screen
    clearScreen()

    # Start listening for an input stream
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 9500))
    serversocket.listen(5) # become a server socket, maximum 5 connections

    #Main processing loop
    print("SERVER STARTED...LISTENING ON PORT 9500")
    while True:
        #Open a connection on port 9500
        connection, address = serversocket.accept()
        #Wait for inbound data
        buf = connection.recv(64).decode("utf-8")
        #If data is received, process it as per the assignment
        if len(buf) > 0:
            #If Hello is received, answer with Hi
            if (buf == "Hello"):
                #Show action on console
                print ("Hi sent to client")
                connection.send(bytes('Hi','UTF-8'))
            else:
                #Show action on console.  Is anything else other than Hello is received, answer with Goodbye
                print ("Goodbye sent to client")
                connection.send(bytes('Goodbye','UTF-8'))

#Start the server
main()