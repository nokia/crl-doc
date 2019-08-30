import os
import pkg_resources


TEMPLATE_DIR = os.path.join(
    pkg_resources.resource_filename('crl.doc', os.path.join('resource', 'templates')))


UTE_TEMPLATE_DIR = os.path.join(
    pkg_resources.resource_filename('ute_doc', os.path.join('resource', 'templates')))


UTE_TOC_TEMPLATE = os.path.join(UTE_TEMPLATE_DIR, 'toc.rst')
