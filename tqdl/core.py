"""Core functionality of tqdl."""

from tqdm import tqdm
import requests


def download(url, fpath):
    """Download a file from the given url to the target file path.

    Parameters
    ----------
    url : str
        The url of the file to download.
    fpath : str
        The fully-qualified path where the file will be downloaded.
    """
    # Streaming, so we can iterate over the response.
    r = requests.get(url, stream=True)
    # Total size in bytes.
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    t = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(fpath, 'wb') as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    if total_size != 0 and t.n != total_size:  # pragma: no cover
        print("Error! Something went wrong during download.")
