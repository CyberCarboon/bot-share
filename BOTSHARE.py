import requests

import threading

import sys

import datetime

import os

saat_ini = datetime.datetime.now()

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati

os.system("clear")
def banner():
    print("""

┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻┻━┻
============SCRIPT SHARE FACEBOOK===============
\x1b[0;96mAUTHOR: CyberCarboon
\x1b[0;93mGitHub:Https://github.com/CyberCarboon
\x1b[0;96mFACEBOOK:SMART DANIE
┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳┳━┳
============LOGIN TUMBAL DULU==================

JIKA SHARE TIDAK BERJALAN

BERARTI TUMBAL COID
HARUS GANTI TUMBAL
INGAT POSTINGAN HARUS PUBLIK

BUKAN PRIVATE

""")

def run(link, token):

    while True:

        headers = {

            'authority': 'graph.facebook.com',

            'cache-control': 'max-age=0',

            'sec-ch-ua-mobile': '?0',

            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36',

        }

        try:

          response = requests.post(f'https://graph.facebook.com/me/feed?link={link}&published=0&access_token={token}', headers=headers)

          print(response.text)

        except:

          sys.exit()

def main():

    banner()

    
    print('━┻┻━┻┻━┻━┻┻━┻┻━┻━┻┻━┻┻━┻━┻┻━┻┻━┻')
    #link = input('Link Posts : ')
    token = input('[?] MASUKKAN TOKEN TUMBAL : ')

   # token = input('Token FB : ')
    link = input('[?] MANA LINK POSTINGANNYA : ')
    print('━┻┻━┻┻━┻━┻┻━┻┻━┻━┻┻━┻┻━┻━┻┻━┻┻━┻')

    number_thread = int(input('Mau share sampe berapa : (><) '))

    for i in range(number_thread):
        thread = threading.Thread(target=run, args=(link, token))
        #print('N O A H',thread.start())
        thread.start()

if __name__ == '__main__':

    main()