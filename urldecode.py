import HTMLParser

parser = HTMLParser.HTMLParser()
s = """
&#75;&#69;&#89;
"""
print parser.unescape(s)