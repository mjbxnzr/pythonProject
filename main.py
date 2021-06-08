import re

def encode(list_of_string):
    list_of_string = [ eachString.capitalize()  for eachString in list_of_string]
    encoded_txt = ''.join(list_of_string)
    print(encoded_txt)

def decode(encoded_string):
    list_of_string = re.findall('([A-Z][a-z]+|[A-Z])', encoded_string[0])
    print(list_of_string)
    dencoded_txt = ' '.join(list_of_string).capitalize()
    print(dencoded_txt)


import sys

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2:])



