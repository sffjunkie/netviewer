import json
from pathlib import Path

from netviewer.config import _config, config_load  # type: ignore
from netviewer.context import _console  # type: ignore
from netviewer.ip import bridge, interface
from netviewer.view import rich_init
from netviewer.view.render.bridge import bridges_render


def test_render_bridge():
    config_load("netviewer.toml")
    rich_init(record=True, width=999)

    p = Path(__file__).parent / "input" / "address.json"
    with open(p, "r") as fp:
        data = json.load(fp)
        addresses = interface.parse(data)
        bridges = bridge.parse(addresses)
        bridges_render(bridges)

        c = _console.get()
        capture = c.export_text()
        lines = capture.split("\n")
        # assert lines[0] == "Bridges"
        assert lines[0] == "br-327a7ac473e4:"
        assert (
            lines[1]
            == "    devices: veth2931569, veth46468de, vetha2610aa, veth92db7f3"
        )
