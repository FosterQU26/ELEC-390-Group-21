import json
from urllib import request

# Server details will change between lab, home, and competition, so saving them somehwere easy to edit
server_ip = "?.?"
server = f"http://{server_ip}:5000"
authKey = "21"
team = 21

# Make request to fares endpoint
res = request.urlopen(server + "/fares")
# Verify that we got HTTP OK
if res.status == 200:
    # Decode JSON data
    fares = json.loads(res.read())
    # Loop over the available fares
    for fare in fares:
        # If the fare is claimed, skip it
        if not fare['claimed']:
            # Get the ID of the fare
            toClaim = fare['id']

            # Make request to claim endpoint
            res = request.urlopen(server + "/fares/claim/" + str(toClaim) + "?auth=" + authKey)
            # Verify that we got HTTP OK
            if res.status == 200:
                # Decond JSON data
                data = json.loads(res.read())
                if data['success']:
                    # If we have a fare, exit the loop
                    print("Claimed fare id", toClaim)
                    break
                else:
                    # If the claim failed, report it and let the loop continue to the next
                    print("Failed to claim fare", toClaim, "reason:", data['message'])
            else:
                # Report HTTP request error
                print("Got status", str(res.status), "claiming fare")
else:
    # Report HTTP request error
    print("Got status", str(res.status), "requesting fares")


# Check the status of our fare
res = request.urlopen(server + "/fares/current/" + str(team))
# Verify that we got HTTP OK
if res.status == 200:
    # Decode JSON data
    data = json.loads(res.read())
    # Report fare status
    if fare is not None:
        print("Have fare", data['fare'])
    else:
        print("No fare claimed", data['message'])
else:
    # Report HTTP request error
    print("Got status", str(res.status), "checking fare")
