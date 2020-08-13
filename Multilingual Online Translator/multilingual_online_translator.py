import requests
import sys
from bs4 import BeautifulSoup


VARIABLES = {1: 'arabic', 2: 'german', 3: 'english', 4: 'spanish', 5: 'french', 6: 'hebrew', 7: 'japanese', 8: 'dutch',
             9: 'polish', 10: 'portuguese', 11: 'romanian', 12: 'russian', 13: 'turkish', 0: 'all'}
VARIABLES1 = {'arabic': '1', 'german': '2', 'english': '3','spanish': '4','french': '5','hebrew': '6', 'japanese': '7',
              'dutch': '8','polish': '9','portuguese': '10','romanian': '11','russian': '12','turkish': '13', 'all': '0'}
# class Error404(Exception):
#     def __init__(self, text):
#         self.txt = text

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='translation')
    translate_word = []
    for item in items:
        translate_word.append(item.get_text(strip=True))
    return translate_word


def get_long_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='example')
    translate_long_word = []
    for item in items:
        translate_long_word.append(item.find('span', class_='text').get_text().replace('\n', '').strip())
    return translate_long_word


def get_long_content1(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='trg')
    translate_long_word = []
    for item in items:
        a = item.find('span', class_='text')
        if a:
            translate_long_word.append(item.find('span', class_='text').get_text().replace('\n', '').strip())
    return translate_long_word

def erros(html):
    if html.status_code == 404:
        print(f'Sorry, unable to find {us_word}')
        exit()
    if html.status_code != 200:
        print(f'Something wrong with your internet connection')
        exit()

def translater(us_languag,us_languag1,us_word):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    if us_languag1 != 'all':
        url = f"https://context.reverso.net/translation/{us_languag}-{us_languag1}/{us_word}"
        html = requests.get(url, headers=headers)
        erros(html)
        word = get_content(html.text)
        sentence = get_long_content(html.text)
        sentence1 = get_long_content1(html.text)
        print(f'{us_languag1.capitalize()} Translations:')
        for i in range(5):
            print(word[i])
        print(f'\n{us_languag1.capitalize()} Examples:')
        for i in range(5):
            print(sentence[i])
            print(sentence1[i])
            print()
    else:
        for i in VARIABLES.values():
            if i == us_languag or i == 'all':
                continue
            url = f"https://context.reverso.net/translation/{us_languag}-{i}/{us_word}"
            html = requests.get(url, headers=headers)
            erros(html)
            if html:
                word = get_content(html.text)
                sentence = get_long_content(html.text)
                sentence1 = get_long_content1(html.text)
                with open(f'{us_word}.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{i.capitalize()} Translations:\n')
                    f.write(f'{word[1]}\n')
                    f.write(f'\n{i.capitalize()} Examples:\n')
                    f.write(f'{sentence[0]}\n')
                    f.write(f'{sentence1[0]}\n')
                    f.write('\n')
                print(f'{i.capitalize()} Translations:')
                print(word[1])
                print(f'\n{i.capitalize()} Examples:')
                print(sentence[0])
                print(sentence1[0])
                print()

us_languag = sys.argv[1]
us_languag1 = sys.argv[2]
us_word = sys.argv[3]
try:
    try:
        VARIABLES1[us_languag]
    except:
        raise KeyError(f"Sorry, the program doesn't support {us_languag}")
    try:
        VARIABLES1[us_languag1]
    except:
        raise KeyError(f"Sorry, the program doesn't support {us_languag1}")
except KeyError as er:
    print(er)
    exit()
else:
    translater(us_languag, us_languag1, us_word)
