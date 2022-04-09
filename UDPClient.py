rom socket import *
serverName = '192.168.100.8'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
messagetoserver = input('Enter Message for Server: ').encode()
clientSocket.sendto(messagetoserver, (serverName, serverPort))
messagefromserver, serverAddress = clientSocket.recvfrom(2048)
print 'Reply from Server: ', messagefromserver
clientSocket.close()
