from berthdeploy.manifest import Slot, total_teu, reefer_share, manifest


def test_total_teu():
    assert total_teu() == 7800


def test_reefer_share():
    assert reefer_share() == 0.6923


def test_empty_is_zero():
    assert reefer_share([]) == 0.0


def test_manifest_keys():
    m = manifest()
    assert set(m) == {"berths", "total_teu", "reefer_share"}
    assert m["berths"] == 3
