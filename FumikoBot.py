import requests
from tqdm import tqdm
import tarfile
import os
import shutil


def download(url: str, fname: str):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    # Can also replace 'file' with a io.BytesIO object
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


def extract_tar(archive_path, destination_path):
    try:
        with tarfile.open(archive_path, "r") as tar:
            tar.extractall(destination_path)
        print("Архив успешно распакован.")
    except tarfile.TarError as e:
        print(f"Ошибка при распаковке архива: {e}")


def tweak():
    os.symlink("./nadekobot-linux-x64/data", "data")


def main():
    download("https://gitlab.com/api/v4/projects/9321079/packages/generic/NadekoBot-build/4.3.17/4.3.17-linux-x64-build.tar", "nadeko.tar")
    extract_tar("nadeko.tar", ".")
    tweak()
    os.system('./nadekobot-linux-x64/NadekoBot')


main()
