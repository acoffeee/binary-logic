import requests

def get_anilist_data(username):
    url = "https://graphql.anilist.co"
    
    query = '''
    query ($name: String) {
      User(name: $name) {
        id
        name
        avatar {
          large
        }
        statistics {
          anime {
            count
            minutesWatched
            genres { 
              genre
              count
              meanScore
            }
          }
        }
      }
      MediaListCollection(userName: $name, type: ANIME, status: COMPLETED) {
        lists {
          entries {
            media {
              title {
                romaji
                english
                native
              }
              episodes
              genres
            }
            score
          }
        }
      }
    }
    '''
    
    variables = {"name": username}
    response = requests.post(url, json={'query': query, 'variables': variables})
    
    unsorted_genre = {}
    if response.status_code == 200:
        data = response.json()["data"]
        user = data["User"]
        print(f"\nAniList Profile for {user['name']}:")
        print(f"User ID: {user['id']}")
        print(f"Avatar URL: {user['avatar']['large']}")
        print(f"Anime Watched: {user['statistics']['anime']['count']}")
        print(f"Minutes Watched: {user['statistics']['anime']['minutesWatched']}")
        
        # Loop through the genres to access each one
        n = 0 
        for genre in data['User']['statistics']['anime']['genres']:
            unsorted_genre[genre['genre']] = genre['meanScore']
            print(f"Genre: {genre['genre']} | Count: {genre['count']} | Mean Score: {genre['meanScore']}")
        
        print(unsorted_genre)
        sorted_genre = dict(sorted(unsorted_genre.items(), key=lambda x: x[1], reverse=True)[:3])
        print(sorted_genre)

        entries = []
        for item in data["MediaListCollection"]["lists"]:
            for entry in item["entries"]:
                media = entry["media"]
                entries.append({
                    "title": media["title"]["english"],
                    "episodes": media["episodes"],
                    "genres": media["genres"],
                    "score": entry["score"],
                    
                })

        # Sort by score (highest first)
        sorted_entries = sorted(entries, key=lambda x: x["score"], reverse=True)

        print("\nCompleted Anime List (Sorted by Score):")
        Great_anime = []
        score = 0
        for entry in sorted_entries:
            score = entry['score']
            if score < 8:
                break
            Great_anime.append({entry['title']}) 
            print(f"- {entry['title']} ({entry['episodes']} eps) | genres: {entry['genres']} Score: {entry['score']}")
            
    else:
        print("Error fetching data.")

# Prompt for username
username = input("Enter AniList username: ")
get_anilist_data(username)
