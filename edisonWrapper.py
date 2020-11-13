import argparse
from argparse import RawDescriptionHelpFormatter
from fraudcatch import findfraud, findfraud2


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

# stateList = ["alabama","alaska","arizona","arkansas","california","colorado","connecticut","delaware","districtofcolumbia","florida","georgia","idaho","illinois","indiana",\
#     "iowa","jersey","kansas","kentucky","louisiana","maine","maryland","massachusetts","mexico","michigan","minnesota","mississippi","missouri","montana","nebraska","nevada",\
#         "newhamp","newyork","northcarolina","northdakota","ohio","oklahoma","oregon","pennsylvania","rhode","southcarolina","southdakota","tenn","texas","utah","vermont",\
#             "virginia","washington","westvirginia","wisconsin","wyoming"]
# for state in stateList:
#     switch = findfraud(state)
#     lost = findfraud2(state)
#     print("{},{},{}".format(state,switch,lost))

findfraud(args.state)
findfraud2(args.state)