import pytest
from pythonic_garage_band.garage_band import Musician, Guitarist, Bassist, Drummer, Band

def test_abstract_musician():
    with pytest.raises(TypeError):
        x = Musician("?","?")
    
def test_guitarist():
    jimi =Guitarist("Jimi")
    assert jimi.name == "Jimi"
    assert jimi.instrument == "guitar"

def test_bassist():
    jaco =Bassist("Jaco")
    assert jaco.name == "Jaco"
    assert jaco.instrument == "bass"

def test_drums():
    sheila =Drummer("Sheila")
    assert sheila.name == "Sheila"
    assert sheila.instrument == "drums"

def test_playsolos():
    #ramones = Band("The Ramones")
    pass

def test_play_solos(some_band):
    solos = some_band.test_play_solos()
    assert solos == "?????"

@pytest.fixture
def some_band():
    assert some_band.name == "Nirvana"

    nirvana = Band("Nirvana",
    [Guitarist("Curt Kobian"),
    Bassist("Kris Nov"),
    Drummer("Dave")

    ])

    return nirvana
