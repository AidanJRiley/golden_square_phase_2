import pytest
from lib.music_listening import *

def test_add_track_non_string_number():
    music = MusicListening()
    with pytest.raises(Exception) as e:
        music.add_track(7)
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_add_track_non_string_none():
    music = MusicListening()
    with pytest.raises(Exception) as e:
        music.add_track(None)
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_add_track_correctly():
    music = MusicListening()
    music.add_track('Happy')
    result = music.show_tracks()
    assert result == ['Happy']

def test_show_empty_tracklist():
    music = MusicListening()
    with pytest.raises(Exception) as e:
        music.show_tracks()
    error_message = str(e.value)
    assert error_message == 'No tracks in list'

def test_add_three_tracks_correctly():
    music = MusicListening()
    music.add_track('Happy')
    music.add_track('Sad')
    music.add_track('Excited')
    result = music.show_tracks()
    assert result == ['Happy','Sad','Excited']

