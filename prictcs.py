class movie:
    def __init__(self,title,mins,hero):
        self.title = title
        self.runtime = mins
        self.hero = hero
        
    def printer(self):
        print(f"Title is : {self.title} runtime is : {self.runtime} hero is: {self.hero}")    
        
list_of_movies=[]
# while True:
#     title = input("Enter the title of movie:")            
#     mins = input("Enter the runtime of movie:")            
#     hero = input("Enter the name of hero of  movie:")

for move in range(3):
    input("enter movie name")
    list_of_movies.append(move)
    print("Movie added into the list")


   
    

    ans = input("Do you want to add another movie(y/n)")
    if ans!='y':
          break

print("All movies information")
for obj in list_of_movies:
    obj.printer()