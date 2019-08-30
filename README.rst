=======================
crl.doc guide
=======================


Installation via pip
====================

Install as usual from https://pypi.dynamic.nsn-net.net/crl/prod/+simple::

  # pip install crl.doc




Generation of documentation with the tool
=========================================

The procedure for generating the documention is the following:

    - Create directory *sphinxdocs*.

    - Install packages you like to be documented

    - Run the command::

        # crl_doc_generate_rst (builtin, api and crl documentation)
        # crl_doc_generate_rst -d builtin -d crl (only builtin and crl documentation)



The documentation ReST source is generated under *sphinxdocs* directory in the
following fashion:

   - *sphinxdocs/builtin*:  Robot Framework built-in ReST source files

   - *sphinxdocs/ute_common_api*: UTE common libraries Python API ReST source
     files

   - *sphinxdocs/crl*: Common Robot Libraries Robot Framework keyword
     documentation ReST source files.

Generation of HTML documentation
================================

Please use the following procedure to generate HTML documentation:

   - create Sphinx configuration *conf.py* and *index.rst* so that it links to
     the sources described above. Examples can be found from
     https://gerrite1.ext.net.nokia.com/gitweb?p=crl/crl-doc.git;a=tree;f=sphinxdocs;hb=refs/heads/master.

   - Run *sphinx-build*.
