import json
from pathlib import Path

from netviewer.ip import bridge, interface, link, route


def test_parse_link():
    p = Path(__file__).parent / "input" / "link.json"
    with open(p, "r") as fp:
        data = json.load(fp)
        info = link.parse(data)

        assert len(info) == 24
        assert info["lo"]["name"] == "lo"
        assert info["lo"]["mtu"] == 65536


def test_parse_address():
    p = Path(__file__).parent / "input" / "address.json"
    with open(p, "r") as fp:
        data = json.load(fp)
        info = interface.parse(data)

        assert len(info) == 24
        assert info["lo"]["name"] == "lo"
        assert info["lo"]["mtu"] == 65536


def test_parse_route():
    p = Path(__file__).parent / "input" / "route.json"
    with open(p, "r") as fp:
        data = json.load(fp)
        info = route.parse(data)

        assert len(info) == 15
        assert info["default"]["destination"] == "default"
        assert info["default"]["metric"] == 100


def test_parse_bridge():
    p = Path(__file__).parent / "input" / "address.json"
    with open(p, "r") as fp:
        data = json.load(fp)
        addresses = interface.parse(data)
        bridges = bridge.parse(addresses)
        assert len(bridges) == 5
        assert len(bridges["br-327a7ac473e4"]["devices"]) == 4
