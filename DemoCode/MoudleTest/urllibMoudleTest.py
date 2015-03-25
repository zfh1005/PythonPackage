import urllib.request
import html.parser

fh = urllib.request.urlopen("http://10.64.32.73/mydasnew/")
htmlPage = fh.read().decode("utf8")
#print (htmlPage)

