import freeze, os, shutil
from distutils.dir_util import copy_tree


def del_and_rebuild():
    shutil.rmtree('build/', ignore_errors=True)
    freeze.freezer.freeze()
    os.makedirs('build', exist_ok=True)
    copy_tree('build', '../crime-in-india.github.io')

if __name__ == '__main__':
    del_and_rebuild()



