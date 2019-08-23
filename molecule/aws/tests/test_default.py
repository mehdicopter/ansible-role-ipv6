import pytest


@pytest.mark.parametrize('sysctl_name', [
    'net.ipv6.conf.all.disable_ipv6',
    'net.ipv6.conf.default.disable_ipv6',
    'net.ipv6.conf.lo.disable_ipv6'
])
def test_sysctl_ipv6(host, sysctl_name):
    s = host.sysctl(sysctl_name)

    assert s == 1
