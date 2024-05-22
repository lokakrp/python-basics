import requests
import time

channelID = 1153759629550026792                                                      # right click on channel, then copy ID
token = "                                                                      "     # use authorization token here
headers = {'Authorization': str(token)}

for i in range (100):                                                               # ENTER NUMBER  OF CHOICE
  payload = {'content': "<@344967656572715008> CAN'T CODE"}                                                          # ENTER MESSAGE OF CHOICE AS THE KEY HERE
  r = requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", data = payload, headers = headers)





# boring discord status stuff

  if r.status_code == 429:                              # handles rate limiting by waiting for the specified retry-after time
      retry_after = r.json().get('retry_after', 1)
      time.sleep(retry_after)

  elif r.status_code != 200:                            # Handle other errors here
      print(f"Error: {r.status_code} - {r.text}")

  else:
      print(f"Message {i} was sent successfully")


# delay if needed

  #time.sleep(1)