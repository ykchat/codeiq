# coding: UTF-8

import urllib2
import random
import MeCab
from HTMLParser import HTMLParser

class AozoraParser(HTMLParser):

    def __init__(self):

        HTMLParser.__init__(self)

        self.__ndiv = 0
        self.__imain = -1
        self.__smain = u''

    def handle_starttag(self, tag, attrs):

        if tag == 'div':
            self.__ndiv += 1
            for attr in attrs:
                if 'class' == attr[0]:
                    if 'main_text' == attr[1]:
                        self.__imain = self.__ndiv

    def handle_endtag(self, tag):

        if tag == 'div':
            if self.__imain == self.__ndiv:
                self.__imain = -1
            self.__ndiv -= 1

    def handle_data(self, data):

        if self.__imain == self.__ndiv:
            self.__smain += data.strip().decode('shift-jis')

    def getMainText(self):

        return self.__smain

def analysis(url):

    source = urllib2.urlopen(url)

    parser = AozoraParser()
    parser.feed(source.read())
    parser.close()

    main = parser.getMainText()

    tagger = MeCab.Tagger("")

    words = {}

    words['名詞'] = []
    words['動詞'] = []

    node = tagger.parseToNode(main.encode('utf-8'))

    while node:

        feat = node.feature.split(",")
        word = node.surface

        if feat[0] in words:
            if feat[0] == '動詞':
                words[feat[0]].append(feat[6])
            else:
                words[feat[0]].append(word)

        node = node.next

    choices = (random.choice(words['名詞']),)
    choices += (random.choice(words['名詞']),)
    choices += (random.choice(words['動詞']),)

    print "[解答]"
    print "[%s]は最近、[%s]を[%s]している。" % choices

if __name__ == '__main__':

    analysis("http://www.aozora.gr.jp/cards/000035/files/1567_14913.html")
