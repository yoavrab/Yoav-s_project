import Queue
import threading
import urllib2

# called by each thread
def get_url(q, url):
    q.put(urllib2.urlopen(url).read())





def main():
    theurls = ["http://google.com", "http://yahoo.com"]
    q = Queue.Queue()
    for u in theurls:
        t = threading.Thread(target=get_url, args = (q,u))
        t.daemon = True
        t.start()

    s = q.get()
    print s





def add(a):
    return a + 1

if __name__ == "__main__":
    main()