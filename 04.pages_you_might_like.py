import json

# Loading the data
def loadData(file):
    with open(file, "r") as f:
        return json.load(f)

def pages_you_might_like(userid, data):
    userpages = {}
    
    # Build the userpages dictionary
    for user in data["users"]:
        userpages[user["id"]] = set(user["liked_pages"])
    
    # Check if the user exists
    if userid not in userpages:
        print(f"User {userid} not found in data")
        return []
    
    given_user_liked = userpages[userid]
    suggestions = {}
    
    # Iterate through all other users
    for user in data["users"]:
        other_userid = user["id"]
        if other_userid != userid:
            other_user_pages = set(user["liked_pages"])
            shared = given_user_liked.intersection(other_user_pages)
            
            # For each page liked by this other user
            for page in other_user_pages:
                # If the given user hasn't liked this page yet
                if page not in given_user_liked:
                    # Add weight based on number of shared pages
                    suggestions[page] = suggestions.get(page, 0) + len(shared)
    
    # Sorting in decreasing order of recommendation score
    sorted_sug = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    
    # Return only the page IDs
    return [pageid for pageid, _ in sorted_sug]


data = loadData("huge.json")  # Replace your json filename here
userid = 17  # A random user selected for now
page_recmndn = pages_you_might_like(userid, data)
print(f"Pages user with ID {userid} might like: {page_recmndn}")