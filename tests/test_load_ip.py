import netviewer.ip


def test_load_ip_link():
    _ = netviewer.ip.load("link")


def test_load_ip_address():
    _ = netviewer.ip.load("address")


def test_load_ip_route():
    _ = netviewer.ip.load("route")
