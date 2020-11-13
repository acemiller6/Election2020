import json



def findfraudTrump(NAME):
    with open(NAME + '.json', encoding="utf8") as f:
        x = json.load(f)
    TotalVotesLost = 0
    print("Total vote updates: {}".format(len(x["data"]["races"][0]["timeseries"])))
    for i in range(len(x["data"]["races"][0]["timeseries"])):
        if i != 0 and x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] < x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"]:
            if x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["bidenj"] > x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["bidenj"]:
                print ("Timestamp: {}".format(x["data"]["races"][0]["timeseries"][i]["timestamp"]))
                print ("    Index : " + str(i) + " < " + str(i-1))
                print ("    Votes switched: {}".format(x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] - x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"]))
                TotalVotesLost += x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] - x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"]
    print ("Total Votes Switched: {}\n".format(TotalVotesLost))
    return TotalVotesLost

def findfraud2(NAME):
    with open(NAME + '.json', encoding="utf8") as f:
        x = json.load(f)
    TotalVotesLost = 0
    for i in range(len(x["data"]["races"][0]["timeseries"])):
        if i != 0 and x["data"]["races"][0]["timeseries"][i]["votes"] < x["data"]["races"][0]["timeseries"][i-1]["votes"]:
            TotalVotesLost += x["data"]["races"][0]["timeseries"][i]["votes"] - x["data"]["races"][0]["timeseries"][i-1]["votes"]
            print("index where Votes lost: {}".format(i))
    print("Total Votes Lost: {}".format(TotalVotesLost))
    return TotalVotesLost

def findfraudBiden(NAME):
    with open(NAME + '.json', encoding="utf8") as f:
        x = json.load(f)
    TotalVotesLost = 0
    print("Total vote updates: {}".format(len(x["data"]["races"][0]["timeseries"])))
    for i in range(len(x["data"]["races"][0]["timeseries"])):
        if i != 0 and x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["bidenj"] < x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["bidenj"]:
            if x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] > x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"]:
                print ("Timestamp: {}".format(x["data"]["races"][0]["timeseries"][i]["timestamp"]))
                print ("    Index : " + str(i) + " < " + str(i-1))
                print ("    Votes switched: {}".format(x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["bidenj"] - x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["bidenj"]))
                TotalVotesLost += x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["bidenj"] - x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["bidenj"]
    print ("Total Votes Switched: {}\n".format(TotalVotesLost))
    return TotalVotesLost

