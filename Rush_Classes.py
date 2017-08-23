
class Artist:
    albums = []
    
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album_name):
        self.albums.append(album_name)


class Album:

    songs = []

    def __init__(self, name):
        self.name = name


class Song:

    lyrics = ''

    def __init__(self, name):
        self.name = name


rush = Artist('Rush')
