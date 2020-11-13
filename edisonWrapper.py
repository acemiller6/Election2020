import argparse
from argparse import RawDescriptionHelpFormatter
from fraudcatch import findfraudTrump, findfraud2, findfraudBiden


description = "Parse Edison Json data from 2020 election for all states.  Full list of states to use on the command line (note names are not always complete):\n\
    alabama\n\
    alaska\n\
    arizona\n\
    arkansas\n\
    california\n\
    colorado\n\
    connecticut\n\
    delaware\n\
    districtofcolumbia\n\
    florida\n\
    georgia\n\
    hawaii\n\
    idaho\n\
    illinois\n\
    indiana\n\
    iowa\n\
    kansas\n\
    kentucky\n\
    louisiana\n\
    maine\n\
    maryland\n\
    massachusetts\n\
    michigan\n\
    minnesota\n\
    mississippi\n\
    missouri\n\
    montana\n\
    nebraska\n\
    nevada\n\
    newhampshire\n\
    newjersey\n\
    newmexico\n\
    newyork\n\
    northcarolina\n\
    northdakota\n\
    ohio\n\
    oklahoma\n\
    oregon\n\
    pennsylvania\n\
    rhodeisland\n\
    southcarolina\n\
    southdakota\n\
    tennessee\n\
    texas\n\
    utah\n\
    vermont\n\
    virginia\n\
    washington\n\
    westvirginia\n\
    wisconsin\n\
    wyoming\n"

parser = argparse.ArgumentParser(description=description, formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('state', help='state name to look at data (see list above)')
args = parser.parse_args()


findfraudTrump(args.state)
findfraud2(args.state)
findfraudBiden(args.state)
