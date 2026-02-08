import sys


def get_input():
    ips = []

    ip_cnt = int(sys.stdin.readline().strip())

    for _ in range(ip_cnt):
        ip = sum(int(num) << (8 * (3 - idx)) for idx, num in enumerate(sys.stdin.readline().split('.')))
        ips.append(ip)

    return ips

def decimal_to_ip(decimal):
    octets = []
    num = int(decimal)
    for i in range(3, -1, -1):
        octet = num // (256**i)
        num %= 256**i
        octets.append(str(octet))
    return ".".join(octets)

def get_mask(ips):
    min_ip = min(ips)
    max_ip = max(ips)
    diff_ip = min_ip ^ max_ip
    mask = 0

    for idx in range(diff_ip.bit_length(), 32):
        mask |= 1 << idx

    ip = min_ip & mask

    ip = decimal_to_ip(ip)
    mask = decimal_to_ip(mask)

    print(ip)
    print(mask)


if __name__ == '__main__':
    ips = get_input()
    get_mask(ips=ips)

