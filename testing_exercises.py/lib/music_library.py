class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.track_list = []

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Returns:
        #   Nothing
        self.track_list.append(track)
    
    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        # a list of Track instances with titles that include the keyword
        return [track for track in self.track_list if keyword in track.title]