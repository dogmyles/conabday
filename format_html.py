from bs4 import BeautifulSoup
import pathlib
path=pathlib.Path(r"c:\Users\andre\Downloads\conabd\index.html")
text=path.read_text(encoding='utf-8', errors='ignore')
soup=BeautifulSoup(text,'html.parser')
formatted=soup.prettify()
path.write_text(formatted,encoding='utf-8')
print('formatted')
