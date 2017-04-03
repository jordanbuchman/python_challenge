import re


def parse(instr):
    ips = re.findall(
        r'((?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]|[0-9])(?:\.|\b)){4})\b', instr)
    return ips
