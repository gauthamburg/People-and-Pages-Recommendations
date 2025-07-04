import json

#Loading thr data
def loadData(file):
    with open(file,"r") as f:
        return json.load(f)


def ppl_you_may_know(userid,data):
    user_friends={}
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])

    if userid not in user_friends:
        return []

    directFriends=user_friends[userid]
    suggestions={}

    for friend in directFriends: #All direct friends of the user
        if friend in user_friends: # Check whether that friend exists        
           for mutual in user_friends[friend]: #Finding mutual friends
              if mutual != userid and mutual not in directFriends:
                suggestions[mutual]=suggestions.get(mutual,0)+1 #Checking, incrementing mutual count

    #Sorting the mutual count in decreasing order
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [user_id for user_id, _ in sorted_suggestions]


data=loadData("cleaned_data.json") #Replace your json filename here
userid=1 #A random user for now, could be changedQ
recmded=ppl_you_may_know(userid,data)
print(f"People person with ID {userid} might know: {recmded}")
