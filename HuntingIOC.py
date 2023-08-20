import re
import sys

# COLE OS IOCs NA VARIÁVEL ioc ABAIXO:

ioc = '''

'''

def question():
    siem = input('List format for query in Qradar or Graylog [ Q / G / L ] ')   
    siem = siem.lower() 
    return siem

def help():
    print('=' * 70)
    print('Missing required parameter')
    print('User mode:')
    print('')
    print(f'{sys.argv[0]} [--url, --uri, --ip, --md5, --sha1, --sha256 ]')
    print('=' * 70)
    
def url(ioct):
    ioctout = re.findall(r'\b(?:[a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}\b', ioct)
    liste = []
    resp = question()
    print('')
    if resp == 'q':
        for url in set(ioctout):
            liste.append(url)
        print(liste)
    elif resp == 'g':
        for url in set(ioctout):
            liste.append(url)
        now = str(liste)
        print(now.strip('[]').replace(',',' OR').replace("'",''))
    else:                                           
        for url in set(ioctout):
            print(url)
       
        
def uri(ioct):
    ioctout = re.findall(r'\/[^\s]+', ioct)
    liste = []
    resp = question()
    print('')
    if resp == 'q':
        for uri in set(ioctout):
            liste.append(uri)
        print(liste)
    elif resp == 'g':
        for uri in set(ioctout):
            liste.append(uri)
        now = str(liste)
        print(now.strip('[]').replace(',',' OR').replace("'",''))
    else:
        for uri in set(ioctout):
            print(uri)
        

def ip(ioct):
    ioctout = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ioct)
    liste = []
    resp = question()
    print('')
    if resp == 'q':
        for ip in set(ioctout):
            liste.append(ip)
        print(ioctout)
    elif resp == 'g':
        for ip in set(ioctout):
            liste.append(ip)
        now = str(liste)
        print(now.strip('[]').replace(',',' OR').replace("'",''))
    else:
        for ip in set(ioctout):
            print(ip)


def md5(ioct):
    ioctout = re.findall(r'[0-9a-f]{32}', ioct)
    liste = []
    resp = question()
    print('')
    if resp == 'q':
        for md5 in set(ioctout):
            liste.append(md5)
        print(ioctout)
    elif resp == 'g':
        for md5 in set(ioctout):
            liste.append(md5)
        now = str(liste)
        print(now.strip('[]').replace(',',' OR').replace("'",''))
    else:
        for md5 in set(ioctout):
            print(md5)
    

def sha1(ioct):
    ioctout = re.findall(r'[0-9a-f]{40}', ioct)
    liste = []
    resp = question()
    print('')
    if resp == 'q':
        for sha1 in set(ioctout):
            liste.append(sha1)
        print(ioctout)
    elif resp == 'g':
        for sha1 in set(ioctout):
            liste.append(sha1)
        now = str(liste)
        print(now.strip('[]').replace(',',' OR').replace("'",''))
    else:
        for sha1 in set(ioctout):
            print(sha1)


def sha256(ioct):
    ioctout = re.findall(r'\b[0-9a-fA-F]{64}\b', ioct)
    liste = []
    resp = question()
    print('')
    if resp == 'q':
        for sha256 in set(ioctout):
            liste.append(sha256)
        print(ioctout)
    elif resp == 'g':
        for sha256 in set(ioctout):
            liste.append(sha256)
        now = str(liste)
        print(now.strip('[]').replace(',',' OR').replace("'",''))
    else:
        for sha256 in set(ioctout):
            print(sha256)

    def all():
        pass 

    
def test_option():
    if (len(sys.argv)) == 1:
        return help()
    elif sys.argv[1] == '--ip':
        return ip(ioc)
    elif sys.argv[1] == '--url':
        return url(ioc.replace('[','').replace(']',''))
    elif sys.argv[1] == '--uri':
        return uri(ioc.replace('[','').replace(']',''))
    elif sys.argv[1] == '--md5':
        return md5(ioc)
    elif sys.argv[1] == '--sha1':
        return sha1(ioc)
    elif sys.argv[1] == '--sha256':
        return sha256(ioc)
    elif sys.argv[1] == '--all':
        return all(ioc)
    elif sys.argv[1] == '--help':
        return help()
    else:
        return help()

test_option()