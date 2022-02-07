import shutil
import subprocess as sp
from os.path import *

cur = dirname(abspath(__file__))
gofile = sp.check_output('which go', shell=True)
gofile = str(gofile, encoding='utf8').strip()
goroot = join(dirname(gofile), '..')
print(f"gofile={gofile} goroot={goroot}")
jsfile = join(goroot, 'misc/wasm/wasm_exec.js')
shutil.copyfile(jsfile, join(cur, 'dist', basename(jsfile)))
