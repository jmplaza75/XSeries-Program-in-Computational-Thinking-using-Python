#!/usr/bin/env python3

def song_playlist(songs, max_size):
	"""
	songs: list of tuples, ('song_name', song_len, song_size)
	max_size: float, maximum size of total songs that you can fit

	Start with the song first in the 'songs' list, then pick the next 
	song to be the one with the lowest file size not already picked, repeat

	Returns: a list of a subset of songs fitting in 'max_size' in the order 
			in which they were chosen.
	"""
	playlist = []
	if songs[0][2] <= max_size:
		playlist.append(songs[0][0])
	else:
		return playlist
	sl = sorted(songs, key = lambda x: x[2])
	sl.remove(songs[0])
	room = max_size - songs[0][2]
	for i in sl:
		if i[2] <= room:
			playlist.append(i[0])
			room -= i[2]
		else:
			break
	return playlist