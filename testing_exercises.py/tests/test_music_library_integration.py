from lib.music_library import MusicLibrary
from lib.track import Track

"""
When we add two tracks
We get the tracks back in the track list
"""
def test_two_tracks_req_tracks():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.track_list == [track_1,track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
def test_two_tracks_search_word_tracks():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    result = library.search_by_title("Way")
    assert result == [track_1]


"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
def test_two_tracks_search_part_word_tracks():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    result = library.search_by_title("lace")
    assert result == [track_2]


"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
def test_two_tracks_empty_search_tracks():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    result = library.search_by_title("zzz")
    assert result == []

"""
Given a track with a title and artist
#format returns a string like TITLE by ARTIST
"""
def test_track_format():
    track = Track("Higher Place", "Malevolence")
    assert track.format() == 'Higher Place by Malevolence'