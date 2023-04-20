from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.handle_attrs(attrs)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.handle_attrs(attrs)
    
    def handle_attrs(self, attrs):
        if attrs:
            print('\n'.join(f"-> {item[0]} > {item[1]}" for item in attrs))

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
