import re
import requests
import arguments
import sys

args = arguments.arguments_user()


def mainargs():
    if args.target:
        if args.vt or args.tm or args.li:
            print("Error: When passing argument '--target' don't use argument --vt, --tm, ou --li")
            sys.exit(1)


mainargs()


req = requests.get(args.target)
out = req.content
end = str(out)


def question():
    siem = input('List format for query in Qradar or Graylog [ Q / G / L ] ')   
    siem = siem.lower() 
    return siem

      
def ip(out):
    ioctout = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', out)
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

def domain(domain):
    ioctout = re.findall(r'\b(?:[a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}\b', out)
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

def uri(out):
    ioctout = re.findall(r'\/[^\s]+', out)
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


def md5(out):
    ioctout = re.findall(r'[0-9a-f]{32}', out)
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
    

def sha1(out):
    ioctout = re.findall(r'[0-9a-f]{40}', out)
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


def sha256(out):
    ioctout = re.findall(r'\b[0-9a-fA-F]{64}\b', out)
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

    def li():
        pass
    
    def vt():
        pass

    def tm():
        pass

     
def test_option():
    if args.ip:
        return ip(end)
        
    elif args.domain:
        return domain(end)
    
    elif args.uri:
        return uri(end)

    elif args.md5:
        return md5(end)
    
    elif args.sha1:
        return sha1(end)
    
    elif args.sha256:
        return sha256(end)

    else:
        return args.help()

test_option()