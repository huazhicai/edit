#coding:utf-8
from distutils.core import setup
import glob
import py2exe
import numpy
import sys

sys.argv.append('py2exe')

options = {
	'py2exe': {
		'includes': ['sip'],
		"dll_excludes": ["MSVCP90.dll",],
		'packages': ['numpy']
	}
}

setup(windows=['main.py',], options=options,
	data_files=[('images',glob.glob('images\\*.png')),
		 ('graph',glob.glob('graph\\*.json')),
		 ('meta',glob.glob('meta\\*.json'))])
