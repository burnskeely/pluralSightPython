currentMovies = {"The Grinch": "11:00am",
                 "Rudolph": "1:00pm",
                 "Frosty the Snowman": "3:00pm",
                 "Christmas Vacation": "5:00pm"}

print("We're showing the following movies:")
for key in currentMovies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = currentMovies.get(movie)

if showtime == None:
    print("Requested movie is not playing.")
else:
    print(showtime)