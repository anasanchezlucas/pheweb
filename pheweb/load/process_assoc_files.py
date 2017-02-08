


# TODO: color lines with ==> using colors like $(tput setab 3 2>/dev/null; tput setaf 0 2>/dev/null) $text $(tput sgr0 2>/dev/null)

from .. import utils
conf = utils.conf

import time
import os.path
import importlib

scripts = '''
get_cpras
merge_cpras
download_rsids
download_genes
add_rsids
add_genes
make_tries
standardize_phenos
make_manhattan
make_qq
make_matrix
bgzip_phenos
top_hits
'''.split()

def run(argv):
    for script in scripts:
        print('==> Starting', script)
        start_time = time.time()
        module = importlib.import_module('.{}'.format(script), __package__)
        try:
            module.run([])
        except Exception:
            print('==> failed after {:.0f} seconds'.format(time.time() - start_time))
            raise
        else:
            print('==> Completed in {:.0f} seconds'.format(time.time() - start_time), end='\n\n')
