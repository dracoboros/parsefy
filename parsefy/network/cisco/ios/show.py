import re
from typing import Dict, List


def show_ip_interface_brief(data: str) -> List[Dict[str, str]]:
    ret = list()
    pattern = re.compile(
        r"^(?P<intf>\S+)\s+(?P<ipaddr>\S+)\s+\w+\s+\w+\s+(?P<status>up|down|administratively down)\s+(?P<proto>up|down)"
    )
    for line in data.splitlines():
        if pattern.match(line):
            intf, ipaddr, status, proto = pattern.match(line).groups()
            ret.append(
                {"intf": intf, "ipaddr": ipaddr, "status": status, "proto": proto}
            )
    return ret
