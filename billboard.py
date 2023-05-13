import requests
from bs4 import BeautifulSoup
s = """Anri
Haruomi Hosono
Toshiki Kadomatsu
Miki Matsubara
Yumi Matsutoya
Meiko Nakahara
Eiichi Ohtaki
Taeko Ohnuki
Hiroshi Sato
Omega Tribe
Masayoshi Takanaka
Mariya Takeuchi
Akira Terao
Junko Yagami
Mai Yamane
Tatsuro Yamashita
Yasuha
Yoshida Minako
Toshiki Kadomatsu
Lamp
Taeko Onuki
Eiichi Ohtaki
Ohashi Junko
MAMALAID RAG
Seishiro Kusunose
Hitomitoi
Akira Terao
Uma no Hone
Yumi Matsutoya
orginal love
sugar babe
Anzen Chitai
Akina Nakamori
Yoriko Ichinomiya
ipo
Masamichi Sugi
Rajie 
Miharu Koshi
Daija
Yukie Yamamura
Cocunut boys
Tomita Keiichi
Nona Reeves
jack or jive
sing like talking
Yuki Saito
Masatoshi Nakamura
the checkers
Saki Kubota
Sayuri Kume
Kyoko Koizumi
Mari Iijima
Junichi Inagaki
garo
sadistics
Kazuhito Murata
Kaoru Sudo
Amii Ozaki
Misuzu Ohara
Tomoko Soryo
Kimiko Kasai
Yuki Okazaki
Kokubu Yurie
Tomomi Sano
Masayuki Suzuki
BAKUFU-SLUMP
Hiroshi Sato
Miki Nakatani
Kaoru Akimoto
Tomoko Aran
Hiromi Iwasaki
Yo Hitoto
Fabienne
Okuda Miwako
Yuiko Tsubokura
Toki Asako
Kukikodan
Toki Asako
paris match
Orange Pekoe
Seiko Matsuda
BREAD & BUTTER
Seri Ishikawa
Hiroko Yakushimaru
char
Hanae
Yukiko Iiri
Yoshiko Sai
Nav Katze
Toko Furuuchi
Benzo
Stardust Revue
The Shamrock
secret cruise
Sentimental City Romance
Kiyonori Matsuo
Tin Pan Alley
Jadoes
Noriko Miyamoto
Hiroyuki Namba
Osaka-fu
Hitomi Tohyama
Kengo Kurozumi
Noda Mikiko
Sayaka Kushibiki
Piccadilly Circus
Stardust Revue
Orangenoise Shortcut
The Mattson 2
Moonriders
Minako
Cindy
Hako Yamasaki
Yasuda Hatsuko
Kimiko Kasai
Crayon-Sha
Kureyon-sha
Masanori Ikeda
Momoko Kikuchi
Yusuke Nakamura
Ichiro Araki
Heartphones
Yoshida Minako
kiyoshi hasegawa
Chocolat & Akito
Namiko
Mari Mizuno
Minuano
Takero Ogata
Pinacoteca
Lazy Sunday
Namy
Greeen Linez
Miyako Yoneyama
Wakui Emi
Omega Tribe
Lea Herman
Ryusenkei
Mari Kaneko
Laula
Makoto Matsushita
Akai Kutsu
Takako Mamiya
Yasuha
Android Apartment
Takeuchi Mariya
Ohashi Junko
Happy End
Kadomatsu Toshiki
Casiopea
Ohnuki Taeko
Matsushita Makoto
Bread & Butter
Yamane Mai
Junko Ohashi
Toshiki Kadomatsu
Tomoko Aran
Junko Ohashi
Minako Yoshida
Suchmos
Every Little Thing
Tina Tamashiro
Minako Honda
t-square
pink martini
saori yuki
beckett
wink
off course
omoinotake
haruomi hosono
friday night plans
nona reeves
kiyotaka sugiyama
kingo hamada
onyako club
naoko gushima
taeko onuki
makoto matsushita
yurie kokubu
kirinji

"""

def web(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup

def getDiv(ID, soup):
    ids = soup.find_all(id=ID)
    return ids

# def getTable(soup):
#     names = []
#     ids = soup.find('table').tbody.findAll("td")
#     for i in ids:
#         c = i.find_all("a")
#         # c = i.finalAll("a")
#         if len(c) != 0:
#             t = c[0].get_text()
#         else:
#             t = i.get_text()
#         t = t.replace("\n", "")
#         t = t.replace("\xa0[ja]", "")
#         escapes = ''.join([chr(char) for char in range(1, 32)])
#         translator = str.maketrans('', '', escapes)
#         t = t.translate(translator)
#         names.append(t.lower())
#     return names

def getTable(soup):
    names = []
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        # print(row.findAll("td"))
        col = row.findAll("td")
        
        if len(col) > 1:
            c = col[1].find_all("a")
            # c = i.finalAll("a")
            if len(c) != 0:
                t = c[0].get_text()
            else:
                t = col[1].get_text()
            names.append(t)

    return names

def getUniformTable(soup, num):
    names = []
    for row in soup.findAll('table')[num].tbody.findAll('tr'):
        col = row.findAll("td")
        if len(col) == 3:
            names.append(col[2].get_text())
    return names

artists = s.split("\n")
artists = [x.lower() for x in artists]
print(artists)

u = "https://en.wikipedia.org/wiki/List_of_Oricon_number-one_singles_of_{}"
counter = 0
for i in range(1972, 1993):
    getU = u.format(i)
    soup = web(getU)
    if (i < 1990):
        names = getTable(soup)
    else:
        if i == 1992:
            names = getUniformTable(soup,1)
        else:
            names = getUniformTable(soup, 0)

    names = [x.lower() for x in names]
    names = [x.replace("\n", "") for x in names]
    # print(names)
    for j in names:
        if j in artists:
            counter+=1
    if (int(counter/10) == 0):
        print("Year: {} City Pop: {}  Total: {}".format(i, counter, len(names)))
    else:
        print("Year: {} City Pop: {} Total: {}".format(i, counter, len(names)))
    counter = 0

