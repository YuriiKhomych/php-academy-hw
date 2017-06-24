from argparse import ArgumentParser

parser = ArgumentParser()
log_values = ["info", "warning", "debug", "error", "critical"]
parser.add_argument("-l",
                    metavar="--level",
                    dest="level",
                    help="Available logging levels: {}".format(log_values))

args = parser.parse_args()
log_level = args.level

if log_level not in log_values:
    print("Incorrect debug level!")
else:
    print("Chosen debug level is:", log_level)