import requests
import logging
from typing import List


# logging configuration
logging.basicConfig(
    filename='exaple.log',
    encoding='utf-8',
    level=logging.INFO
)


def mylogger(func):
    def wrapper(url, **kwargs):
        try:
            logging.info(f"we are hitting URL - {url}")
            result_ = func(url)
            logging.info(f"success - {result_.status_code}")
        except Exception:
            logging.error(f"there are issue fetching details")

        return result_

    return wrapper


@mylogger
def hit_url(url):
    #print(f"hiting this url {url}")
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    else:
        return response


def fetch_data(urls: List) -> List:
    """ fetching data from urls """
    data = []
    for url in urls:
        res = hit_url(url)
        data.append(res.json())

    return data


if __name__ == "__main__":
    result = ["https://swapi.dev/api/people/1/"]
    output = fetch_data(result)
    print(output)

