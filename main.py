from cache import Cache


def main():
    addrs = [800, 824, 828, 832, 790, 1640, 836, 848, 1240, 1244, 1248, 1252]
    l1 = Cache(4, 8, 4, addrs)
    debug = 10
    l1.retrieve_table(addrs, 5)

main()
