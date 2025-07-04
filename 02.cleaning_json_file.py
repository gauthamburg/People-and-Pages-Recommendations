import json

def cleanData(data):
    #Users with no name are removed
    data["users"] = [user for user in data["users"] if user["name"].strip()]
    
    #Removing duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    #Removing inactive users
    data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]

    # Removing duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]] = page
    data["pages"] = list(unique_pages.values())
    
    return data


data=json.load(open("dirty.json","r"))
cleanData(data)
json.dump(data,open("cleaned_data.json","w"),indent=4)
print("Done")