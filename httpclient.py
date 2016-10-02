import socket
import webbrowser

def make_http_request(host, port, resource, file_name):
    #setting up some basic variables
    host_name_string = host.decode()
    resource_name_string = resource.decode()
    status_code = 0
    #creating the socket and sending the request header
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_name_string,port))
    send_http_request_header(s, resource_name_string, host_name_string)
    stuffToSave = []
    stuffToSave.append(b'')
    for i in range(0,100000):
       response = s.recv(1)
       stuffToSave[0] += response

    s.close()

    write_message_to_file(stuffToSave, file_name)

    #read in the status line here from the response header. Save info like status code and other tidbits

    #read headers to check for chunk or content-length here. Have it return a tuple of what type of message it is and the length of the message if it is content length or 0 if it is chunk

    #read the chunked or content messaage and save it using write_message_to_file

    return status_code

'''
Author: Eric Nowac`
Purpouse: send bare minimum http request header to server
Arguments: socket connected_socket, string resource_name, string host_name
'''
def send_http_request_header(connected_socket, resource_name, host_name):
    connected_socket.send(('GET ' + '/' + resource_name + ' HTTP/1.1\r\nHost: ' + host_name + '\r\n\r\n').encode())


def read_chunked_message(connected_socket, file_name):
    while(get_size_of_chunk(connected_socket) != 0):
        for i in range(0,get_size_of_chunk(connected_socket)):
            write_byte_to_file(connected_socket.recv(1), file_name)


def get_size_of_chunk(connected_socket):
    current_byte = connected_socket.recv(1)
    amount_of_chunks = 0
    amount_of_chunks_as_ascii_bytes = b''
    while (current_byte != b'\r'):
        amount_of_chunks_as_ascii_bytes += current_byte
        current_byte = connected_socket.recv(1)
    connected_socket.recv(1)
    amount_of_chunks = int(amount_of_chunks_as_ascii_bytes)
    return amount_of_chunks

'''
Author: Eric Nowac
Purpose: print the message to a text file
Arguments: list listOfLines, string file_name
Return: nothing
'''
def write_message_to_file(listOfLines, file_name):
    file = open(file_name + ".txt","wb")
    for bytes in listOfLines:
        file.write(bytes)
    file.close()

'''
Author: Eric Nowac
Purpose: append the byte to a text file
Arguments: byte byte, string file_name
Return: nothing
'''
def write_byte_to_file(byte, file_name):
    file = open(file_name + '.txt', "ab")
    file.write(byte)
    file.close()










#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("seprof.sebern.com",80))
#s.send(('GET / HTTP/1.1\r\nHost: seprof.sebern.com\r\n\r\n').encode())
#stuffToSave = []
#stuffToSave.append(b'')
#for i in range(0,20000):
#    response = s.recv(1)
#    stuffToSave[0] += response


#write_message_to_file(stuffToSave, "finalMessage")

#webbrowser.open_new("http://localhost:63342/NetworkProtocolsLab5/testwebsite.html")

make_http_request(('seprof.sebern.com').encode(), 80, ('sebern1.jpg').encode(),"test")