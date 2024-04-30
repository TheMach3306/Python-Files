from argparse import ArgumentParser as AP

'''
Find the largest number in a file
- Version 0.1.1
- Author: Mach.33

The input file (-f) must have digits separated by a comma, later versions will have checks that
will auto-separate data with a comma if not done so already
'''

class _Main:
    
    def __init__(self):
        self.__AUTHOR__ = "Mach.33"
        self.__VERSION__ = "0.1.1"
        self.__TITLE__ = "Largest"
        self.__DESC__ = """
        Find the largest number in a file.
        """
        
    def put_banner(self):
        print (f"""
        {"#" * 35}\n\t **\n** Version: {self.__VERSION__}\t **\n** {self.__DESC__}\t **\n
        """)

class LargestNumber:
    
    def __init__(self, filename):
        self.fname = filename
        self.num_array = []
        
    def find_largest(self):
        with open(self.fname) as data_file:
            for line in data_file:
                # Add a check to see if the number is actually a number and not a letter
                line = [i.strip() for i in line.split(",")]
                res = [eval(i) for i in line]
        
        mx = max(res)
        
        # Print output
        print(f"\n=> The largest number in \"{self.fname}\" is: {mx}\n")


def main():
    # Parser variable
    parse = AP(usage="python3 largest.py -f [file]", conflict_handler="resolve")
    parse.add_argument("-f", "--file", type=str, metavar="", dest="_data_file", required=True, help="File containing numbers ONLY.")
    parse.add_argument("-b", "--banner", action="store_true", dest="_banner", required=False, help="Print a banner and exit.")
    
    args = parse.parse_args()
    
    if args._data_file:
        l = LargestNumber(filename=args._data_file)
        l.find_largest(); pass
    
    if args._banner:
        m = _Main()
        m.put_banner(); pass
        
main()
