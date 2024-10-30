import socket
import des

def client_program():
    HOST = '127.0.0.1'
    PORT = 5000
    KEY = 'aBhNDJjB'

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    try:
        while True:
            message = input("message to send: ")
            encryptedMessage = des.ecbEncrypt(message, KEY)
            print(f"sending encrypted message: {encryptedMessage}")
            client_socket.send(encryptedMessage.encode('utf-8'))
            
    except KeyboardInterrupt:
        client_socket.close()

if __name__ == '__main__':
    client_program()