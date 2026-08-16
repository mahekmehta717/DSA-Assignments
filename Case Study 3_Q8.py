playlist = ["Song1", "Song2", "Song3"]

# 1. Insert Song4
playlist.append("Song4")

# 2. Display the playlist
print("Playlist:")
for song in playlist:
    print(song, end=" → ")

# 3. Delete Song2
playlist.remove("Song2")

# 4. Display the updated playlist
print("\n\nUpdated Playlist:")
for song in playlist:
    print(song, end=" → ")
