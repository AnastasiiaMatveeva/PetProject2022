import re
import io
from collections import defaultdict
from models.node import Node

if __name__ == "__main__":
    input_file = "../input data/input_file.cdb"
    keywords = ('ET','NBLOCK','EBLOCK','MPDATA','SECOFFSET','SECBLOCK')

def read_file(input_file, mode, enc):
    with io.open(input_file, mode, encoding = enc) as text_file:
        f = text_file.readlines()

    return f

def import_cdb(input_file, keywords):
    dictionary = transform(input_file, keywords)
    dict_key_int, dict_key_node = import_nodes(dictionary)

    return dictionary, dict_key_int, dict_key_node

def import_nodes(dictionary):
    key = 'NBLOCK'
    f = lambda x, y, z, t: Node(x, y, z, t)
    res = map(f, dictionary[key]['loc_num'],
              dictionary[key]['x_coord'],
              dictionary[key]['y_coord'],
              dictionary[key]['z_coord']
              )
    list_nodes = list(res)
    dict_key_int = dict(zip(dictionary[key]['loc_num'], list_nodes))
    dict_key_node = {n: i for i, n in enumerate(list_nodes, 1)}

    return dict_key_int, dict_key_node

def transform(input_file, keywords):
    text = read_file(input_file, "r", enc="utf-8")
    dict = defaultdict(lambda: (defaultdict(list)))

    for line in text:
        try:
            key_find, object = parse_line(line, keywords)
            dict = parse_block(object, dict, key_find)
        except Exception:
            pass # убрать
            #print('нет совпадений')

    return dict

def parse_block(object, dict, key):
    dict_key = object.groupdict()
    for k, v in dict_key.items():
        dict[key][k].append(change_type(v))

    return dict

def change_type(value):
    try:
        k = float(value)
        if k % 1 == 0:
            return int(k)

        return k

    except ValueError:

        return value

def parse_line(line, keywords):
    for key in keywords:
        name_fun = eval('extract_{}'.format(key))
        object = name_fun(line)
        if object:

            return key, object
        else:
            pass


def extract_ET(line):
    # pattern = (r'^{},\s+\d+,\d+$').format(key)
    pattern = (r'^ET,\s+(?P<loc_num>\d+),(?P<type_elem>\d+)$')
    ET = re.match(pattern, line)
    if ET:

        return ET

def extract_NBLOCK(line):
    # pattern = r'^(\s+\d+){3}(\s\d+.\d+E(-|\+)\d+)*$'
    pattern = r'^(\s+(?P<loc_num>\d+))(\s+\d+){2}' \
              r'(?P<x_coord>(\s\d+.\d+E(-|\+)\d+)?)' \
              r'(?P<y_coord>(\s\d+.\d+E(-|\+)\d+)?)' \
              r'(?P<z_coord>(\s\d+.\d+E(-|\+)\d+)?)$'
    NBLOCK = re.match(pattern, line)
    if NBLOCK:

        return NBLOCK

def extract_EBLOCK(line):
    # pattern = r'^(\s+\d+){14,}'
    pattern = r'^\s+\d+\s+(?P<id_elem_type>\d+)(\s+\d+){2}\s+' \
              r'(?P<esys>\d+)(\s+\d+){5}\s+' \
              r'(?P<elem_num>\d+)\s+' \
              r'(?P<node_s>(\s+\d+){4}$)'
    EBLOCK = re.match(pattern, line)
    if EBLOCK:

        return EBLOCK


def extract_MPDATA(line):
    # pattern = r'^MPDATA,\w\d.\d,\s\d+,[A-Z]+\s*,(\s+\d+(.\d+)*,*){3,}'
    pattern = r'^MPDATA,\w\d.\d,\s\d+,' \
              r'(?P<props>[A-Z]+)\s*,\s+' \
              r'(?P<id_mat>\d+),\s+\d+,\s+' \
              r'(?P<value>\d+.\d+)\s+,(\d+.\d+\s+,?)*$'
    MPDATA = re.match(pattern, line)
    if MPDATA:

        return MPDATA

def extract_SECOFFSET(line):
    # pattern = r'^SECOFFSET,\w+$'
    pattern = r'^SECOFFSET,(?P<plane>\w+)$'
    SECOFFSET = re.match(pattern, line)
    if SECOFFSET:

        return SECOFFSET

def extract_SECBLOCK(line):
    # pattern = r'^(\s+-*\d+(.\d+)*,*){4}$'
    pattern = r'^\s+(?P<thikness>\d+.\d+),' \
              r'\s+(?P<id_sec>\d+),' \
              r'\s+(?P<angle>-*\d+.\d+),' \
              r'\s+\d+$'
    SECBLOCK = re.match(pattern, line)
    if SECBLOCK:

        return SECBLOCK

dict = import_cdb(input_file, keywords)
print(dict)