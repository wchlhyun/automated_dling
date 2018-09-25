# Automated Downloading from a Weeb
##### Downloads character searches from https://chunagon.ninjal.ac.jp/chj/search

##### Required Python Packages:
* selenium (install with `pip install selenium`)

##### To Use
* Edit *login_template.json* with login information
* Rename *login_template.json* to *login.json*
* Type characters to search in *character_file.txt* (no white space needed)
* `python downloader.py -f FILENAME -b BROWSER`
    * `-f` file with characters, defaults to *character_file.txt*
    * `-b` True to run with browers, False to run without, defaults to False
##### Made at the request of Nick Leung