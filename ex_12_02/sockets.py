import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
#在命令行最后只需输入\n\n,而在这里需要\r\n\r\n
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode()) #end=''避免了recv一次后换行
mysock.close()                         

