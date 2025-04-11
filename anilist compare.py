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
        temp = 0
        usersystem = 0
        def findlowerandupperbound():
            for scores in entries:
                score = scores["score"]
                temp += score
            
        print("\nCompleted Anime List (Sorted by Score):")
        
        Great_anime = []
        score = 0
        relavence = 0
        #when good or bad is 0, that implys bad and the top tags will start to become "dont pick if anime has alof of this tag"
        #1 implys mediocre anime, this will tell it that "high percent tags here are honestly jsut to balance it out and give more weight. but it may show a hit or miss genre if one is detected alot in which case i may try, when making the bot that anime with alot of those tags are to be completely randomly chosen"
        #2 implys good, high percent tags in this will say "please reccomend me anime with these"
        #still have to decide if i should use combos or have each tag maybe have an indiviual weight. 
        #if i do individual tbh ill probably make a part in the script to combind tags to make anime to reccomend any way so maybe combos are the way to go lmao
        #gob = good or bad
        # 1 is bad 2 is mid 3 is good
        gob = 0
        # create a dict thats like {tags: lgbtq: {2,23,4,5,32} harem:{3.4.2.1.3.5}}
        #these tags may be named good bad or mid, but really their just like the amount of times the tag shwos up in anime that youve rated above 8, 5, or 0.
        #also only counting tags above 50% FOR NOW
        # this scans if the tag is above a percent, then what the anime is rated that the tag is in.
        #may change the header to be good mid and bad anime then have relavence tracking.
        #good mid or bad relates to what the anime is rated
        tag_weighting = {
            "good":{"very relavent":{}, "mid relavent":{}, "hardly":{}},
            "mid": {"very relavent":{}, "mid relavent":{}, "hardly":{}},
            "bad":{"very relavent":{}, "mid relavent":{}, "hardly":{}}
          }
        
        #relavence= {
        #    "very_relavent":{
        #      "good_tags":{},
        #      "mid_tags":{},
        #      "bad_tags":{}
        #    }, 
        #      "mid_relavence":{
        #        "good_tags":{},
        #        "mid_tags":{},
        #        "bad_tags":{}
        #    },
        #      "not_relavence":{
        #          "good_tags":{},
        #          "mid_tags":{},
        #          "bad_tags":{}
        #    }
        #      
        #}
        temp = 0
        mrt = ()
        p = 0
        n = 0
        tag_set = []
        for entry in sorted_entries:
            score = entry['score']
            name = entry['title']
            if name == 'None':
                name = entry['title']['native']
            tag_set.append([name])
            relavence = entry['tags']
            if score >= 8:
                gob = 3
            elif score >=5:
                gob=2
            else:
                gob =1
                
                #tag_set.append(entry['title'])
                #print(tag_set)
            #print(f"- {entry['title']} ({entry['episodes']} eps) Score: {entry['score']}")
            for tag in entry['tags']:
                relavent = tag['rank']
                #print(tag_set)
                if p == 1:
                    ber = ber + "," + tag['name']
                else:
                    ber = tag['name']
                thing =  tag['name']
                p =1
                if relavent <= 80:
                    n+=1
                    break
                else:
                    tag_set[n].append(thing)
        for i in tag_set:
            print(i)
        url = "https://graphql.anilist.co"
        ql ='''
         query ($tag: String){
              Media(tag: $tag){
                title{
                  english
                } 
              }
            }
            '''
        yeah = "a"
        no = 'harem'
        variables = {"tag_in": "ecchi"}
        yurrrr = requests.post(url, json= {'query': ql, 'variables': variables})
        yurrrr.json()
        print(yurrrr)
    else:
        print("Error fetching data.")

# Prompt for username
#username = input("Enter AniList username: ")
username = "Coffeee"
get_anilist_data(username)

