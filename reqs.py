import requests
from bs4 import BeautifulSoup
import re


def name(name):
    clean_name = name.replace("%20", " ")
    print(clean_name)
    return clean_name


def main():
    file_list = []
    url = "http://127.0.0.1:8000/"
    r = requests.get(url, allow_redirects=True)

    soup = BeautifulSoup(r.text)

    for link in soup.find_all('a'):
        file_list.append(link.get('href'))

    for i in range(len(file_list)):
        file_url = url + file_list[i]
        r = requests.get(file_url, allow_redirects=True)
        open(name(file_list[i]), 'wb').write(r.content)


if __name__ == "__main__":
    main()
