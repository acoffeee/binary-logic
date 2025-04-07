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
            }
            score
          }
        }
      }
    }
    '''
    
    variables = {"name": username}
    response = requests.post(url, json={'query': query, 'variables': variables})
    
    if response.status_code == 200:
        data = response.json()["data"]
        user = data["User"]
        print(f"\nAniList Profile for {user['name']}:")
        print(f"User ID: {user['id']}")
        print(f"Avatar URL: {user['avatar']['large']}")
        print(f"Anime Watched: {user['statistics']['anime']['count']}")
        print(f"Minutes Watched: {user['statistics']['anime']['minutesWatched']}")
        
        entries = []
        for item in data["MediaListCollection"]["lists"]:
            for entry in item["entries"]:
                media = entry["media"]
                entries.append({
                    "title": media["title"]["english"],
                    "episodes": media["episodes"],
                    "score": entry["score"]
                })

        # Sort by score (highest first)
        sorted_entries = sorted(entries, key=lambda x: x["score"], reverse=True)

        print("\nCompleted Anime List (Sorted by Score):")
        score = 0
        for entry in sorted_entries:
            score = entry['score']
            if score < 8:
                break
            print(f"- {entry['title']} ({entry['episodes']} eps) | Score: {entry['score']}")

    else:
        print("Error fetching data.")

# Prompt for username
username = input("Enter AniList username: ")
get_anilist_data(username)
