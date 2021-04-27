import speedtest


def to_Mbps(val):
    return round(val/10**6, 2)


def speed_test():
    st = speedtest.Speedtest()
    print("download:", to_Mbps(st.download()), "Mbps")
    print("upload:  ", to_Mbps(st.upload()), "Mbps")
    print("ping:    ", round(st.results.ping, 2), "ms")




if __name__ == '__main__':
    speed_test()