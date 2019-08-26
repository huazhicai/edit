# coding:utf-8
import json
import os
from mutil import loadJsonData, dumpJsonData

currnt_dir = os.path.dirname(os.path.abspath(__file__))


def load_nodes_meta_information():
    return loadJsonData(os.path.join(currnt_dir, 'meta', 'nodes.json'))


def load_graph_information(filename):
    return loadJsonData(filename)


def load_color_config():
    return loadJsonData(os.path.join('meta', 'colors.json'))


def load_prefs():
    return loadJsonData(os.path.join('meta', 'prefs.json'))


def save_prefs(prefs):
    dumpJsonData(os.path.join('meta', 'prefs.json'), prefs)
