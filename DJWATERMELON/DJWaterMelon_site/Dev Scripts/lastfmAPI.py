import requests
import json

API_KEY = ""
API_URL = "http://ws.audioscrobbler.com/2.0/"

def lastfm_get(data):
    headers = {
        "User-Agent":"MyApp/2.0"
    }

    try:
        response = requests.get(
            API_URL,
            headers=headers,
            params=data,
            timeout=5
        )
        response.raise_for_status()
        data_req = response.json()
        return data_req
    except requests.exceptions.RequestException as e:
        print(f'Запрос провален с ошибкой {e}')
        return None
    
if __name__ == "__main__":

    """
    mbid (Optional) : The musicbrainz id for the track
    track (Required (unless mbid)] : The track name
    artist (Required (unless mbid)] : The artist name
    username (Optional) : The username for the context of the request. If supplied, the user's playcount for this track and whether they have loved the track is included in the response.
    autocorrect[0|1] (Optional) : Transform misspelled artist and track names into correct artist and track names, returning the correct version instead. The corrected artist and track name will be returned in the response.
    api_key (Required) : A Last.fm API key.
    """

    params = {
        "api_key" : API_KEY,
        "format" : "json",
        "method": "track.getInfo",
        "autocorrect": 1,
    }
    
    list_of_songs = [
    [["Исполнитель", "Chase Atlantic"], ["Песня", "Angels"], ["Испонитель", "Arctic Monkeys "], ["Песня", "Knee socks "], ["Испонитель", "Charli xcx"], ["Песня", "Mean girls"]],
    [["Исполнитель", "Marilyn Manson"], ["Песня", "Deep Six"], ["Испонитель", "Три дня дождя"], ["Песня", "Не виноваты планеты"], ["Испонитель", "Tokio Hotel"], ["Песня", "Final Day"]],
    [["Исполнитель", "Led Zeppelin "], ["Песня", "Good Times Bad Times"], ["Испонитель", "ALI"], ["Песня", "Lost in paradise"], ["Испонитель", "The Beatles"], ["Песня", "Back In The U.S.S.R."]],
    [["Исполнитель", "Rammstein"], ["Песня", " Ausländer"], ["Испонитель", "Гражданская оборона"], ["Песня", "Любо"], ["Испонитель", "Plamenev"], ["Песня", "Головы с плеч!"]],
    [["Исполнитель", "MACAN"], ["Песня", "ASPHALT 8"], ["Испонитель", " Linkin Park"], ["Песня", "Given Up"], ["Испонитель", " СЕРЕГА ПИРАТ"], ["Песня", "Мой байк"]],
    [["Исполнитель", "ANNA ASTI"], ["Песня", "ЦАРИЦА"], ["Испонитель", "Скриптонит, Ёлка"], ["Песня", "Цепи-ленты"], ["Испонитель", "Дайте танк (!)"], ["Песня", "Мы"]],
    [["Исполнитель", "MORGENSHTERN"], ["Песня", "ICE"], ["Испонитель", "ANNA ASTI"], ["Песня", "Царица"], ["Испонитель", "PIZZA"], ["Песня", "Романс"]],
    [["Исполнитель", "Rocket"], ["Песня", "Bomb"], ["Испонитель", "Friendly Thug 52 ngg"], ["Песня", "DreamKeeperc"], ["Испонитель", "Friendly Thug 52 ngg"], ["Песня", "Cherni FlaG 3"]]
    ]

    dict_of_songs = {}
    results_dict = {}
    for item in list_of_songs:
        for i in range(0, len(item)):
            if item[i][0] == 'Исполнитель' and item[i+1][0] == 'Песня':
                artist = item[i][1]
                song = item[i+1][1]
                dict_of_songs[artist]=song
            """
            if artist in dict_of_songs:
                dict_of_songs[artist] = song
            else:
                dict_of_songs[artist]=song
            """

    print(dict_of_songs)

    for item in dict_of_songs.keys():
        params["artist"] = str(item).strip()
        params['track'] = dict_of_songs[item].strip()

    #print(params)
        result_track = lastfm_get(params)
        if result_track:
            #print("Название песни: ", result_track['track']['name'], '\nMbid Песни: ',
                #result_track['track']['mbid'], '\nПродолжительность: ', 
                #result_track['track']['duration'], '\nИсполнитель Mbid: ', 
                #result_track['track']['artist']['mbid'], '\nИмя исполнителя: ', 
                #result_track['track']['artist']['name'], '\nMbid альбома: ', 
                #result_track['track']['album']['mbid'], '\nНазвание альбома: ', 
                #result_track['track']['album']['title'], '\nДата выпуска: ',)
                #result_track['track']['wiki']['published'], '\nЖанр: ', )
                #f"{[result_track['track']['toptags']['tag'][i] for i in result_track['track']['toptags']['tag']]}", '\n')
    
            results_dict['track'] = result_track['track']['name']
            results_dict['track_duraction']=result_track['track']['duration']
            if 'wiki' in result_track:
                results_dict['track_release_date']= result_track['track']['wiki']['published']
            results_dict['author_name'] = result_track['track']['artist']['name']
            results_dict['album_name'] = result_track['track']['album']['title']

        params_artist = {
            "api_key" : API_KEY,
            "format" : "json",
            "method": "artist.getInfo",
            "autocorrect": 1,
        }
        params_artist['artist']=result_track['track']['artist']['name']
        result_artist = lastfm_get(params_artist)   

        results_dict['author_image'] = result_artist['artist']['image']

        params_album = {
            "api_key" : API_KEY,
            "format" : "json",
            "method": "album.getInfo",
            "autocorrect": 1,
        }
        params_album['artist'] = result_track['track']['name']
        params_album['album'] = result_track['track']['album']['title']
        result_album = lastfm_get(params_album)  
        if result_album:
            if 'releasedate' in result_album:
                results_dict['album_release'] = result_album['album']['releasedate']

        print(results_dict)