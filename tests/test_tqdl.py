"""Test tqdl."""

from tqdl import download


def test_tqdl():
    download("http://www.ovh.net/files/10Mb.dat", '/tmp/temp.dat')
