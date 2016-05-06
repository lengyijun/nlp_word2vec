# -*- coding: utf-8 -*-
import json
import codecs

if __name__ == '__main__':
    data=[]
    with codecs.open("train_pdtb.json","rU","utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    with open("raw_text","w") as f:
        for json_unit in data:
            f.write(json_unit['Arg1']['RawText'])
            f.write("\n")
            f.write(json_unit['Arg2']['RawText'])
            f.write("\n")
