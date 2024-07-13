import json
import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

_ = response.json()

rate = float()
rate = _["bpi"]["USD"]["rate_float"]


def main():
  if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
  elif len(sys.argv) == 2:
      try:
         bc = float(sys.argv[1])
         value = rate * bc
         print(f"${value:,}")
      except (requests.RequestException, ValueError):
         print("Command line argument is not a number")
         sys.exit(1)


if __name__ == "__main__":
  main()
