import sys

from hello import say_hello


def main(args):
   if len(args) > 1:
      say_hello(args[1:])
   else:
      print("You need to pass at least one name on the command line.")


if __name__ == '__main__':
   main(sys.argv)

