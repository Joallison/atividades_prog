import socket

HOST = ""
PORTA = 8051

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORTA))

while True:
    message = input("Sua Mensagem:")
    sock.send(bytes(message, 'UTF-8'))
    if (message == '0'):
        with open('teste1.jpg', 'wb+') as output:
            rec = sock.recv(44032)
            output.write(rec)
    elif (message == 'q'):
        break

sock.close()
