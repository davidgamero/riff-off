import os
import time
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from lyricsgenius import Genius
import pickle

load_dotenv()
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
genius = Genius(os.getenv("GENIUS_ACCESS_TOKEN"))

all_time_pop_hits_id = "6Mf614QiAuop5ud9x5beBS"

# results = sp.current_user_saved_tracks()
all_time_hits_playlist = sp.playlist(all_time_pop_hits_id)

# open a file, where you stored the pickled data


def load_lyrics_cache():
    lyrics_cache = {}
    try:
        file = open('lyrics_cache', 'rb')
        lyrics_cache = pickle.load(file)
        file.close()
    except FileNotFoundError:
        file = open('lyrics_cache', 'wb')
        pickle.dump({}, file)
        file.close()
    return lyrics_cache


def save_lyrics_cache():
    file = open('lyrics_cache', 'wb')
    pickle.dump(lyrics_cache, file)
    file.close()


lyrics_cache = load_lyrics_cache()
lyrics_dict = {}


def simplify_track_name(track_name):
    no_parentheses = track_name.split("(")[0]
    no_brackets = no_parentheses.split("[")[0]
    no_hyphen = no_brackets.split("-")[0]
    return no_hyphen.strip()


def parse_tracks_to_cache(tracks):

    for idx, item in enumerate(tracks['items']):
        track = item['track']
        track_id = track['id']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

        lyrics = ""
        if track_id in lyrics_cache:
            print("Found in cache")
            lyrics = lyrics_cache[track_id]
        else:
            print("Not found in cache")
            # run ten times to avoid rate limit
            tries = 0
            while tries < 5 and lyrics == "":
                tries += 1
                try:
                    track_name = track['name']
                    if (tries > 3):
                        track_name = simplify_track_name(track_name)
                        print("Simplified track name to ", track_name)

                    genius_song = genius.search_song(
                        track_name, track['artists'][0]['name'])
                    lyrics = genius_song.lyrics
                    lyrics_cache[track_id] = lyrics
                    save_lyrics_cache()
                    print("Saved to cache")
                except:
                    print("Rate limit exceeded")
                print("Retrying in ", 2**tries, " seconds")
                time.sleep(2**tries)


tracks = all_time_hits_playlist['tracks']
while tracks['next']:
    parse_tracks_to_cache(tracks)
    tracks = sp.next(tracks)

print(len(lyrics_dict))
