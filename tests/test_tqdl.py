"""Test tqdl."""

import os

from tqdl import download


HOMEPATH = os.path.expanduser('~')


def test_tqdl():
    download(
        url="http://www.ovh.net/files/10Mb.dat",
        fpath=os.path.join(HOMEPATH, 'tmp.dat'),
    )
