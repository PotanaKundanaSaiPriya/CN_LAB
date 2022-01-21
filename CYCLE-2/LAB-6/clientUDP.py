from socket import *
serverName="127.0.0.1"
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
sentence=input("\nenter the file name: ")
clientSocket.sendto(bytes(sentence,"utf-8"),(serverName,serverPort))
filecontents,serverAddress=clientSocket.recvfrom(2048)
print('\nreply from server:\n')
print(filecontents.decode("utf-8"))
#for i in filecontents:
    #print(str(i),end=")
clientSocket.close()    
clientSocket.close()  
