import json
import requests
import sys

_ = request.get("https://api.coindesk.com/v1/bpi/currentprice.json")

def main():
  if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit()
  elif len(sys.argv) == 2:
      try:
         bc = float(sys.argv)


if __name__ == "__main__":
  main()
