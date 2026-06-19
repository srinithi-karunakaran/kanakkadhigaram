from kanakkadhigaram.nilam.chathuram_nilam_alavu import NilamNarSathuraAlavu
from kanakkadhigaram.nilam.vatta_nila_murai import VattamKootalNilaMurai


def test_chathuram():
    assert (
        NilamNarSathuraAlavu.nilam_alavu_107(
            16,
            24,
            100
        )
        == 225
    )


def test_vattam():
    obj = VattamKootalNilaMurai()

    assert obj.vatta_nila_parappu(8) == 48