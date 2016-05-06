# -*- coding: utf-8 -*-
import word2vec

if __name__ == '__main__':
    word2vec.word2vec("raw_text","text8.bin",size=100,verbose=True)