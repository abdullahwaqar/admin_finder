import requests, sys

def recon(url):
    lives = []
    wordlist = open('wordlist.txt', 'r')
    lines = wordlist.readlines()
    wordlist.close()

    for line in lines:
        line = line.replace('\n', '')
        request = url + '/' + line
        http = requests.get(request)
        code = http.status_code
        if code != 301 and code != 404:
            if not "Page not contentd" in http.content:
                print "Page Found: " + request
                lives.append(request)
            else:
                print "Page Not Found: " + request
        else:
                print "Page N0t Found: " + request
    for live in lives:
        print live
    print 'Finished...'

if __name__ == '__main__':
    recon(sys.argv[1])