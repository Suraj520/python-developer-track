import collections
import os
import requests
import sys
from bs4 import BeautifulSoup
from colorama import init, Fore


def open_page(path, url):
    filename = path + '/' + url + '.txt'
    if not os.path.exists(filename):
        print("Error: Incorrect URL")
    else:
        with open(filename) as f:
            print(f.read())


def save_file(path, url, text):
    index = url.rfind('.')
    filename = path + '/' + url[0:index] + '.txt'
    with open(filename, 'w') as outfile:
        outfile.write(text)
    return url[0:index]


def get_file(url):
    if url.find('https://') < 0:
        url = 'https://' + url
    r = requests.get(url)
    return r.text


def load_page(text):
    text_list = []
    tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    soup = BeautifulSoup(text, 'html.parser')
    for tag in soup.find_all(tags):
        text = tag.get_text()
        if tag.name == 'a':
            text = Fore.BLUE + text
        text_list.append(text)
    return '\n'.join(text_list)


# write your code here
path = '.'
if len(sys.argv) > 1:
    # create directory
    directory = sys.argv[1]
    if not os.path.exists(directory):
        os.mkdir(directory)
    path = directory

browser_history = collections.deque()
prev_tab = ''
current_page = ''

while True:
    if current_page != prev_tab:
        browser_history.append(prev_tab)
        prev_tab = cur_tab
    url = input()
    if url == "exit":
        break
    elif url == "back":
        if browser_history:
            cur_tab = browser_history.pop()
            open_page(path, cur_tab)
    elif url.rfind('.') < 0:
        cur_tab = url
        open_page(path, cur_tab)
    else:
        text = load_page(get_file(url))
        print(text)
        cur_tab = save_file(path, url, text)
