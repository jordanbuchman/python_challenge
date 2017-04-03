import ip
import parse
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


def process(filename, limit):
    ips = parse.parse(open(filename).read())[:limit]

    num = len(ips)

    data = []

    def workfun(adr):
        data.append(ip.IP(adr))
        print("{}/{}".format(len(data), num))
        return True

    futures = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        for work in ips:
            futures.append(executor.submit(workfun, work))
    wait(futures, return_when=ALL_COMPLETED)

    return data
