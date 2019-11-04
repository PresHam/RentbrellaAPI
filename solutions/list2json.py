#Functions to process data, and deliver the required format


def list2json(list):
    jsonlist = []
    for i in range(len(list)):
        json = {"id": list[i][0],
                "name": list[i][1],
                "address": list[i][2]
               }
        jsonlist.insert(i, json)
    jsonappended = {"entries": jsonlist}
    return jsonappended

def stationslist2json(list):
    jsonlist = []
    for i in range(len(list)):
        json = {"serial": list[i][0],
                "premise_id": list[i][1],
                "name": list[i][2]
               }
        jsonlist.insert(i, json)
    jsonappended = {"entries": jsonlist}
    return jsonappended