##################################################################################
# Written/Modified by Karl Tomecek 05/31/2019                                    #
# Program Name: client.py                                                        #
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
    
    #Loop until * is entered
    while True:
        #Get user input
        text = input("Enter text to send (enter '*' to exit): ")
        #If * is entered exit application
        if text =="*":
            print("Program has terminated")
            break
        #Now that there is text open connection to the server
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', 9500))
        #Send that text to the server
        clientsocket.sendall(bytes(text, 'UTF-8'))
        #Now listen for the response
        buf = clientsocket.recv(64).decode("utf-8")
        if len(buf) > 0:
            #Now that there is a response, display to user
            print(buf)
        #Close the connection and wait for more text to send
        clientsocket.close

#Start the client
main()