from json2html import json2html 

if __name__ == '__main__':
    filename = './target.json'
    htmlStr = json2html('./target.json')
    print(type(htmlStr))
    print(htmlStr)