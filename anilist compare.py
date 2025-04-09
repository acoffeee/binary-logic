import requests

def get_anilist_data(username):
    #this just sets where your getting the data from.  
    url = "https://graphql.anilist.co"
    #establishes a query or what you want and or need 
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
              tags {
                name
                rank
              }
            }
            score
          }
        }
      }
    }
    '''
    #establish what the inputs are.
    variables = {"name": username}
    #request the actual info 
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
        total_count = 0
        scores= {}
        x = 0
        for genre in data['User']['statistics']['anime']['genres']:
            unsorted_genre[genre['genre']] = genre['meanScore']
            x = genre['meanScore'] * genre['count']
            print(x)
            scores[genre['genre']] = x
            print(f"Genre: {genre['genre']} | Count: {genre['count']} | Mean Score: {genre['meanScore']}")
        
        
        #print(unsorted_genre)
        #figure out how to properly balance genre likeness with count and score somehow
        # idk i definetly want count to be a big factor. tbh maybe just like find mad then find difference from mad and count. 
        # that so if mad is 120 ten if count is 80 above, find what percent above it is and multiple that by score?.
        g = ""
        score = ""
        weight_of_genre = []
        #for i in unsorted_genre:
            

        #sorted_genre = dict(sorted(unsorted_genre.items(), key=lambda x: x[1], reverse=True)[:3])
        #print(sorted_genre)

        entries = []
        for item in data["MediaListCollection"]["lists"]:
          for entry in item["entries"]:
              media = entry["media"]
              entries.append({
                  "title": media["title"]["english"],
                  "episodes": media["episodes"],
                  "genres": media["genres"],
                  "score": entry["score"],
                  "tags":media["tags"]
              })
        # Sort by score (highest first)
        sorted_entries = sorted(entries, key=lambda x: x["score"], reverse=True)
#
        print("\nCompleted Anime List (Sorted by Score):")
        Great_anime = []
        score = 0
        relavence = 0
        for entry in sorted_entries:
            score = entry['score']
            relavence = entry['tags']
            if score < 8:
                break
            Great_anime.append({entry['title']}) 
            print(f"- {entry['title']} ({entry['episodes']} eps) | genres: {entry['tags']} Score: {entry['score']}")
            
    else:
        print("Error fetching data.")

# Prompt for username
#username = input("Enter AniList username: ")
username = "Coffeee"
get_anilist_data(username)
