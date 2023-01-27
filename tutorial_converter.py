## Title  : Tutorial Converter
## Author : Leo Werneck
## Desc   : Generates tutorial notebooks from NRPy+ modules (and vice-versa)
## Refs   :

from re import search
from sys import argv

class header():
    

## Step 1: Parsing the header
def parse_header(string):
    """
      Inputs
      ------
        string : str
          Input file string

      Returns
      -------
        header : namedtuple
          

      Raises
      ------
        TypeError  : if string is not of type str
        ValueError : if core header contents are not found
    """

    match = search(r" *## *[Tt]itle *: *(.*)", string)
    if not match:
        raise ValueError("No title found")
    title = match.group(1)
    print(f"## Title  : {title}")
    
    match = search(r" *## +[Aa]uthor *: *(.*)", string)
    if not match:
        raise ValueError("No authors found")
    author = match.group(1)
    print(f"## Author : {author}")
    
    match = search(r" *## +[Dd]esc *: *(.*)", string)
    if not match:
        raise ValueError("No description found")
    desc = match.group(1)
    print(f"## Desc   : {desc}")

if __name__ == '__main__':
    with open(argv[1], "r") as f:
        string = f.read()
    parse_header(string)
