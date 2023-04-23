#!/usr/bin/python3  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

# python -m pip install --user -r requirements.txt  	  	  
from bs4 import BeautifulSoup  	  	  
from urllib.parse import urlparse, urljoin, urldefrag  	  	  
import requests  	  	  
import sys  	  	  
import time  	  	  




def crawl(url, depth, maxdepth, visited):
    """  	  	  
    Given an absolute URL, print each hyperlink found within the document.  	  	  
    This function will need more parameters.  	  	  

    Your task is to make this into a recursive function that follows hyperlinks  	  	  
    until one of two base cases are reached:  	  	  

    0) No new, unvisited links are found  	  	  
    1) The maximum depth of recursion is reached  	  	  
    """  	  	  

    if (depth > maxdepth):
        return
    if (url in visited):
        return
    numSpaces = "    " * depth
    print(numSpaces + url)
    visited.add(url)
    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
        return
    try:
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.find_all('a')
        if links:
            for link in links:
                if link.get('href'):
                    new_url = str(link.get('href'))
                    parsed = urlparse(new_url)
                    if not (parsed.scheme and parsed.netloc):
                        new_url = urljoin(url, new_url)
                    if parsed.fragment:
                        new_url = new_url.split('#')[0]
                    crawl(new_url, depth + 1, maxdepth, visited)
                else:
                    continue
        else:
            return
    except Exception as e:
        print(e)
        return


# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool  	  	  
if __name__ == "__main__":  	  	  

    ## If no arguments are given...  	  	  
    if len(sys.argv) < 2:  	  	  
        print("Error: no URL supplied", file=sys.stderr)
        exit(0)  	  	  
    else:  	  	  
        url = sys.argv[1]  	  	  

    parsed = urlparse(url)
    if not ((parsed.scheme == 'http://' or 'https://') and parsed.netloc):
        print("Error: Invalid URL supplied.")
        print("Please supply an absolute URL")
        exit(0)

    maxDepth = 3
    if len(sys.argv) >= 3:
        if (sys.argv[2].isdigit() and (not '.' in sys.argv[2])):
            if int(sys.argv[2]) >= 0:
                maxDepth = int(sys.argv[2])
        else:
            maxDepth = 3
    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")  	  	  

    before = time.time()
    visited = set()
    try:
        crawl(url, 0, maxDepth, visited)
    except KeyboardInterrupt:
        #ensure 'control c' will not be printed to console
        sys.stderr.write("\r")
    lvisited = len(visited)
    after = time.time()
    time = after - before
    plural = 's' if lvisited != 1 else ''
    print(f"Visited {lvisited} unique page{plural} in {round(time, 4)}.")