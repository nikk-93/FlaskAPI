import argparse
import multiprocessing
import requests
import uuid
import time


def download_image(url):
    start = time.time()
    filename = str(uuid.uuid4()) + '.jpg'  # url.split('/')[-1]
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    end = time.time()
    print(f'Image {filename} downloaded in {end - start} seconds')


def main(urls: list):
    start = time.time()
    pool = multiprocessing.Pool()
    pool.map(download_image, urls)
    pool.close()
    pool.join()
    end = time.time()
    print(f'Total time taken: {end - start} seconds')


if __name__ == '__main__':
    urls = ['https://lipsum.app/random/640x360']
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', nargs='*')
    args = parser.parse_args()
    if args.urls:
        urls = args.urls
    main(urls)
