import asyncio
import aiohttp
import uuid
import time
import argparse


async def download_image(url):
    start = time.time()
    filename = str(uuid.uuid4()) + '.jpg'  # url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(filename, 'wb') as f:
                f.write(await response.read())
    end = time.time()
    print(f'Image {filename} downloaded in {end - start} seconds')


async def main(urls: list):
    start = time.time()
    tasks = [download_image(url) for url in urls]
    await asyncio.gather(*tasks)
    end = time.time()
    print(f'Total time taken: {end - start} seconds')

if __name__ == '__main__':
    urls = ['https://lipsum.app/random/640x360']
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', nargs='*')
    args = parser.parse_args()
    if args.urls:
        urls = args.urls
    asyncio.run(main(urls))
