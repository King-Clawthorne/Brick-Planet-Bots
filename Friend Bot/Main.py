import requests
from time import sleep as wait

count = 0

print(
  "Friend All Bot By elevator, (every 10k friends takes around 8 hours 15 minutes)"
)

cookie = input("Input the brickplanet_session cookie:\n")

token = input("Input Your bp token:\n")

while True:
  try:
    startAt = input(
      "What ID do you want to start at? (start at 1 if you've never used this: "
    )
    count = (int(startAt))
    break
  except:
    print("Please enter a valid number")


def returnPlrName(url):
  last_segment = url.split('/')[-1]
  plrName = last_segment.replace('-', ' ')

  return plrName


try:
  while True:
    response = requests.post(
      f"https://www.brickplanet.com/friends/send-request/{str(count)}",
      cookies={'brickplanet_session': cookie},
      data={"_token": token})
    wait(2.5)
    count += 1
    print(response.status_code)
    if response.status_code != 419 and response.status_code != 429:
      if response.url == 'https://www.brickplanet.com/players':
        print(f"error friending ID {str(count)}")
      else:
        plrName = returnPlrName(response.url)

        print(
          f"Successfully sent friend request to {plrName}! ID: {str(count - 1)}"
        )

    elif response.status_code == 419:
      print("Cookie Or Token is invalid, stopping.")
      break
    elif response.status_code == 429:
      print("Being rate limited.")
except:
  print(f"There was an error, you're currently at ID {count}")

input("press enter to stop program")
