import json

#Loads the json file
def loadData(file):
    with open(file,"r") as f:
        data=json.load(f)
    return data

#Display the details
def displayDetails(data):
    print("Users and their connections:")
    for user in data["users"]:
        print(f"{user["name"]} (ID: {user["id"]}) - Friends: {user["friends"]} - Liked Pages: {user["liked_pages"]}")
        
    print("\nPages\n")
    for page in data["pages"]:
        print(f"{page["id"]} ; {page["name"]}")


#Main calls
data=loadData("workers.json")
displayDetails(data)
        



    
    