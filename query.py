from movies import Movies

movies = Movies('./movies.txt')

print("q: quit")
print("sn: search movie names")
print("sc: search casts")
print("list: print all the movie names")

user_input = input()
while user_input != "q":

    
    if user_input == "list":
        for movie in movies._movies:
            print(movie['name'])
    
    print("q: quit")
    print("sn: search movie names")
    print("sc: search casts")
    print("list: print all the movie names")
    
    user_input = input()
  

