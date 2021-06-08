import speedtest


def to_Mbps(val):
    return round(val/10**6, 2)

def to_ping(val):
    return round(val, 2)

def speed_test(args):
    st = speedtest.Speedtest()

    res = ""
    res += "download {} Mbps\n".format(to_Mbps(st.download()))
    res += "upload {} Mbps\n".format(to_Mbps(st.upload()))
    res += "ping {} ms\n".format(to_ping(st.results.ping))

    return res

if __name__ == '__main__':
    speed_test(None)