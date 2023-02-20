from html.parser import HTMLParser

N = int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print(tag)
        for attribute in attributes:
            print(f"-> {attribute[0]} > {attribute[1]}")
    
html = '\n'.join([input() for x in range(0, N)])  
parser = MyHTMLParser()
parser.feed(html)
parser.close()