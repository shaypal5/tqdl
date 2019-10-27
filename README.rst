tqdl ⋙
######

|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

``requests``-based file downloads with ``tqdm`` progress bars.   

.. code-block:: python

  from tqdl import download
  download(file_url, target_file_path)
   19%|█▊        | 20.5M/110M [00:06<00:29, 2.98MiB/s]

.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install tqdl


Features
========

* Simple and straightforward API.
* Installable from PyPI with ``pip install tqdl``.
* `Tested on TravisCI <https://travis-ci.org/shaypal5/tqdl>`_ against Linux, Windows and macOS, and Python versions 3.5 through 3.7.
* The name - تقدّل - can be traslated as "get ahead", which is awesome. 


Use
===

``tqdl`` contains a single funcion, aptly named download, which you can use to download files with a nice progress bar by providing it with a URL and a file path. Obviously, this is only useful for downloads of large files, and where you cae about showing the user (of your code/script/whatever) the progress of the ongoing download.

Here is a very straightforward example:

.. code-block:: python

  from tqdl import download
  download(file_url, target_file_path)
   19%|█▊        | 20.5M/110M [00:06<00:29, 2.98MiB/s]


Contributing
============

Package author and current maintainer is `Shay Palachy <http://www.shaypalachy.com/>`_ (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/tqdl.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd tqdl
  pip install -e '.[test]'


Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd tqdl
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


Credits
=======

Created by `Shay Palachy <http://www.shaypalachy.com/>`_ (shay.palachy@gmail.com).

Based on a `stackoverflow answer by user leovp <https://stackoverflow.com/a/37573701/781531>`_.


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/tqdl.svg
  :target: https://pypi.python.org/pypi/tqdl

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/tqdl.svg
   :target: https://pypi.python.org/pypi/tqdl

.. |Build-Status| image:: https://travis-ci.org/shaypal5/tqdl.svg?branch=master
   :target: https://travis-ci.org/shaypal5/tqdl

.. |LICENCE| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://github.com/shaypal5/tqdl/blob/master/LICENSE

.. |Codecov| image:: https://codecov.io/github/shaypal5/tqdl/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/tqdl?branch=master

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/99e79faee7454a13a0e60219c32015ae
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/shaypal5/tqdl?utm_source=github.com&utm_medium=referral&utm_content=shaypal5/tqdl&utm_campaign=Badge_Grade_Dashboard

.. |Requirements| image:: https://requires.io/github/shaypal5/tqdl/requirements.svg?branch=master
   :target: https://requires.io/github/shaypal5/tqdl/requirements/?branch=master
   :alt: Requirements Status
     
.. |Codefactor| image:: https://www.codefactor.io/repository/github/shaypal5/tqdl/badge?style=plastic
   :target: https://www.codefactor.io/repository/github/shaypal5/tqdl
   :alt: Codefactor code quality

.. |Downloads| image:: https://pepy.tech/badge/tqdl
   :target: https://pepy.tech/project/tqdl
   :alt: PePy stats

.. .. test pypi
