import json
import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

_ = response.json()
print(_)

rate = float()
for i in _["bpi"]:
   rate1 = i["USD"]
   rate = rate1["rate_float"]

def main():
  if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit()
  elif len(sys.argv) == 2:
      try:
         bc = float(sys.argv)
         value = rate * bc
         print(f"${value}.:4f")
      except requests.RequestException:
         print("Command line argument is not a number")
         sys.exit()


if __name__ == "__main__":
  main()

