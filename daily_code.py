from pytube import Playlist, YouTube

playlist_url = input("Enter Playlist URL: ")
playlist = Playlist(playlist_url)

for video_url in playlist.video_urls:
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()  # Get highest resolution video stream
        print(f"Downloading: {yt.title}")
        stream.download()  # Download the video
    except pytube.exceptions.RegexMatchError:
        print(f"Error: Invalid video URL: {video_url}")
    except pytube.exceptions.VideoUnavailable:
        print(f"Error: Video unavailable: {video_url}")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")
