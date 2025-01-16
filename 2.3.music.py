class MusicPiece:
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return f"""Performer: {self.artist}
Title:     {self.title}
Album:     {self.album}
Year:      {self.year}"""


def main():
    song1 = MusicPiece("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
    song2 = MusicPiece("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

    print(song1)
    print()
    print(song2)


if __name__ == '__main__':
    main()