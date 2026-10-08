# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    # TODO: add an optional flag -i / --ignore-case  (use action="store_true")\
    parser.add_argument("-i", "--ignore-case", action="store_true")
    

    args = parser.parse_args()

    if args.ignore_case:
        print("case insensitive mode is: ON")
    else: {
        print("case insensitive mode is: OFF")
    }

    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).
    if args.sample.txt == 1: {
        print("1. apple")
    }
    elif args.sample.txt == 2: {
        print("2. Banana")
    }
    elif args.sample.txt == 3: {
        print("3. cherry") 
    }
    elif args.sample.txt == 4: {
        print("4. apple pie")
    }
    elif args.sample.txt == 5: {
        print("5. grape")
    }
    elif args.sample.txt == 6: {
        print("6. Apple juice")
    }
    else: {
        print("not a valid index: number and word not found")
    }




if __name__ == "__main__":
    main()
