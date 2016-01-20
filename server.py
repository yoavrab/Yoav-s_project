import Queue
import threading
import urllib2
import socket



server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 3000))
server_socket.listen(5)
sockets = []

def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

def connect():
    try:
        (new_socket, address) = server_socket.accept()
        sockets.append(new_socket)
    except:
        pass



def main():
    fi = open("bkg-blu.jpg", "rb")
    data = fi.read()
    print len(data)
    theurls = ["http://google.com", "http://yahoo.com"]
    q = Queue.Queue()
    t1 = threading.Thread(target=connect)
    t1.start()
    while True:
        for socket in sockets:
            if sockets is None:
                break
            '''t = threading.Thread(target=get_url, args = (q,u))
            t.daemon = True
            t.start()'''
            fi = open("bkg-blu.jpg", "rb")
            data = fi.read()
            len(data)
            try:
                socket.send(len(data))
                socket.send(data)
            except:
                print "error"

    #s = q.get()
    #print s





def add(a):
    return a + 1

if __name__ == "__main__":
    main()