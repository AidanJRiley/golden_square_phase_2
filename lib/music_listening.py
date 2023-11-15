class MusicListening:
    def __init__(self):
        self.track_list = []

    def add_track(self,name):
        if type(name) != str:
            raise Exception('This is not a string!')
        self.track_list.append(name)
        

    def show_tracks(self):
        if self.track_list == []:
            raise Exception('No tracks in list')
        return self.track_list