from pytube import Playlist

playlist_url = input('Enter Playlist: ')
playlist = Playlist(playlist_url)

for video in playlist.videos:
    video.streams.get_lowest_resolution().download()