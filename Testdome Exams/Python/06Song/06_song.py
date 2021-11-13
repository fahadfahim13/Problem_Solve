class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self) -> bool:
        playlist = {self}
        song = self.next
        # print(self.name, end=" ")
        while song:
            # print(song.name, end=" ")
            if song in playlist:
                return True
            else:
                playlist.add(song)
                song = song.next
        return False


def main():
    first = Song("First")
    second = Song("Second")
    third = Song("Third")
    fourth = Song("Fourth")
    fifth = Song("Fifth")
    first.next_song(second)
    second.next_song(third)
    third.next_song(fourth)
    fourth.next_song(fifth)
    # fifth.next_song(first)
    print(first.is_repeating_playlist())


if __name__ == '__main__':
    main()
