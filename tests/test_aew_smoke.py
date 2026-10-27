from aew_smoke.check import smoke_check


def test_smoke_check():
    assert smoke_check() == "delivered"
