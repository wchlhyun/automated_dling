import os
currDirectory = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(currDirectory)

import helper as h
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", default= "character_file.txt",
                    help="file with string of characters (no white space). Default is \'character_file.txt\'",
                    metavar="FILE")
parser.add_argument("-b", "--browser", dest="browser", default= False,
                    help="Open in brower or not. Default is false (no browser)",
                    metavar="BROWSER")
args = parser.parse_args()

def main(filename, browser):
    characters = h.get_list_characters(filename)
    driver = h.open_driver(browser)
    h.login(driver)
    h.move_to_search(driver)

    for c in characters:
        h.search_term(driver, c)
    sys.stdout.write("Done. Closing Program.")

if __name__ == "__main__":
    main(args.filename, args.browser)