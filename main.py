#!python3
from src.domain.locator import glob
import requests
import json

def main():
    locator = glob()
    tg = locator.tg()
    tg.tg.infinity_polling()

if __name__ == '__main__':
  main()


# end