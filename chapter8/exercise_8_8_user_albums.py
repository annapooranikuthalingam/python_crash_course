"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users
to enter an album’s artist and title. Once you have that information, call make_album() with the
user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
"""

def make_album(name,title,songs=None):
    if songs== None:
        album={"artist_name":name,"album_title":title}
    else:
        album = {"artist_name": name, "album_title": title,"Number_of_songs":songs}
    return album

flag=True
while flag==True:
    name=input("Enter the albums's artist name: ")
    title= input("Enter the album's title: ")
    response= input("Type 'no' for quitting, else type 'yes' to continue: ")
    if response=="no":
        flag=False
    album= make_album(name,title)
    print(album)