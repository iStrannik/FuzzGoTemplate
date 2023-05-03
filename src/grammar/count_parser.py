# Generated from count_parser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import inspect
import json
import os

if not os.path.exists('counter.json'):
    with open('counter.json', 'w+') as file:
        file.write('{}')


def serializedATN():
    return [
        4,1,56,437,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,69,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,77,8,1,10,1,12,1,80,9,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,106,8,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,124,8,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,137,8,5,1,5,1,5,1,5,3,5,142,
        8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,154,8,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,163,8,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,171,
        8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,184,8,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,198,8,
        10,1,10,1,10,1,11,1,11,1,11,5,11,205,8,11,10,11,12,11,208,9,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,218,8,11,1,12,1,12,1,
        12,3,12,223,8,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,3,14,252,8,14,1,15,1,15,3,15,256,8,15,1,16,
        3,16,259,8,16,1,16,1,16,3,16,263,8,16,1,16,1,16,3,16,267,8,16,3,
        16,269,8,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,279,8,18,
        1,18,5,18,282,8,18,10,18,12,18,285,9,18,1,19,1,19,1,19,1,19,1,20,
        1,20,3,20,293,8,20,1,21,3,21,296,8,21,1,21,1,21,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,5,22,309,8,22,10,22,12,22,312,9,22,1,
        22,1,22,1,22,1,22,1,22,5,22,319,8,22,10,22,12,22,322,9,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,5,22,342,8,22,10,22,12,22,345,9,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,386,8,
        22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,3,23,405,8,23,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,433,8,28,1,29,1,29,1,
        29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,0,0,467,0,60,1,0,0,0,2,68,1,0,0,0,
        4,105,1,0,0,0,6,107,1,0,0,0,8,113,1,0,0,0,10,127,1,0,0,0,12,145,
        1,0,0,0,14,166,1,0,0,0,16,174,1,0,0,0,18,179,1,0,0,0,20,187,1,0,
        0,0,22,217,1,0,0,0,24,219,1,0,0,0,26,227,1,0,0,0,28,251,1,0,0,0,
        30,253,1,0,0,0,32,258,1,0,0,0,34,270,1,0,0,0,36,278,1,0,0,0,38,286,
        1,0,0,0,40,290,1,0,0,0,42,295,1,0,0,0,44,385,1,0,0,0,46,404,1,0,
        0,0,48,406,1,0,0,0,50,410,1,0,0,0,52,414,1,0,0,0,54,418,1,0,0,0,
        56,432,1,0,0,0,58,434,1,0,0,0,60,61,3,2,1,0,61,1,1,0,0,0,62,63,3,
        46,23,0,63,64,6,1,-1,0,64,69,1,0,0,0,65,66,3,4,2,0,66,67,6,1,-1,
        0,67,69,1,0,0,0,68,62,1,0,0,0,68,65,1,0,0,0,69,78,1,0,0,0,70,71,
        3,46,23,0,71,72,6,1,-1,0,72,77,1,0,0,0,73,74,3,4,2,0,74,75,6,1,-1,
        0,75,77,1,0,0,0,76,70,1,0,0,0,76,73,1,0,0,0,77,80,1,0,0,0,78,76,
        1,0,0,0,78,79,1,0,0,0,79,3,1,0,0,0,80,78,1,0,0,0,81,82,3,6,3,0,82,
        83,6,2,-1,0,83,106,1,0,0,0,84,85,3,8,4,0,85,86,6,2,-1,0,86,106,1,
        0,0,0,87,88,3,10,5,0,88,89,6,2,-1,0,89,106,1,0,0,0,90,91,3,12,6,
        0,91,92,6,2,-1,0,92,106,1,0,0,0,93,94,3,14,7,0,94,95,6,2,-1,0,95,
        106,1,0,0,0,96,97,3,18,9,0,97,98,6,2,-1,0,98,106,1,0,0,0,99,100,
        3,20,10,0,100,101,6,2,-1,0,101,106,1,0,0,0,102,103,3,16,8,0,103,
        104,6,2,-1,0,104,106,1,0,0,0,105,81,1,0,0,0,105,84,1,0,0,0,105,87,
        1,0,0,0,105,90,1,0,0,0,105,93,1,0,0,0,105,96,1,0,0,0,105,99,1,0,
        0,0,105,102,1,0,0,0,106,5,1,0,0,0,107,108,3,40,20,0,108,109,5,5,
        0,0,109,110,5,40,0,0,110,111,5,6,0,0,111,112,3,42,21,0,112,7,1,0,
        0,0,113,123,3,40,20,0,114,115,3,22,11,0,115,116,6,4,-1,0,116,124,
        1,0,0,0,117,118,3,24,12,0,118,119,6,4,-1,0,119,124,1,0,0,0,120,121,
        3,26,13,0,121,122,6,4,-1,0,122,124,1,0,0,0,123,114,1,0,0,0,123,117,
        1,0,0,0,123,120,1,0,0,0,124,125,1,0,0,0,125,126,3,42,21,0,126,9,
        1,0,0,0,127,128,3,40,20,0,128,129,5,7,0,0,129,130,3,22,11,0,130,
        131,3,42,21,0,131,141,3,2,1,0,132,133,3,40,20,0,133,136,5,8,0,0,
        134,135,5,7,0,0,135,137,3,22,11,0,136,134,1,0,0,0,136,137,1,0,0,
        0,137,138,1,0,0,0,138,139,3,42,21,0,139,140,3,2,1,0,140,142,1,0,
        0,0,141,132,1,0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,144,3,38,
        19,0,144,11,1,0,0,0,145,146,3,40,20,0,146,153,5,9,0,0,147,148,3,
        22,11,0,148,149,6,6,-1,0,149,154,1,0,0,0,150,151,3,24,12,0,151,152,
        6,6,-1,0,152,154,1,0,0,0,153,147,1,0,0,0,153,150,1,0,0,0,154,155,
        1,0,0,0,155,156,3,42,21,0,156,162,3,2,1,0,157,158,3,40,20,0,158,
        159,5,8,0,0,159,160,3,42,21,0,160,161,3,2,1,0,161,163,1,0,0,0,162,
        157,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,3,38,19,0,165,
        13,1,0,0,0,166,167,3,40,20,0,167,168,5,2,0,0,168,170,5,53,0,0,169,
        171,3,22,11,0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,
        173,3,42,21,0,173,15,1,0,0,0,174,175,3,40,20,0,175,176,5,24,0,0,
        176,177,5,53,0,0,177,178,3,42,21,0,178,17,1,0,0,0,179,180,3,40,20,
        0,180,181,5,3,0,0,181,183,5,55,0,0,182,184,3,22,11,0,183,182,1,0,
        0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,186,3,42,21,0,186,19,1,0,
        0,0,187,188,3,40,20,0,188,189,5,4,0,0,189,190,3,22,11,0,190,191,
        3,42,21,0,191,197,3,2,1,0,192,193,3,40,20,0,193,194,5,8,0,0,194,
        195,3,42,21,0,195,196,3,2,1,0,196,198,1,0,0,0,197,192,1,0,0,0,197,
        198,1,0,0,0,198,199,1,0,0,0,199,200,3,38,19,0,200,21,1,0,0,0,201,
        206,3,28,14,0,202,203,5,10,0,0,203,205,3,28,14,0,204,202,1,0,0,0,
        205,208,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,
        208,206,1,0,0,0,209,210,6,11,-1,0,210,218,1,0,0,0,211,212,3,36,18,
        0,212,213,6,11,-1,0,213,218,1,0,0,0,214,215,3,34,17,0,215,216,6,
        11,-1,0,216,218,1,0,0,0,217,201,1,0,0,0,217,211,1,0,0,0,217,214,
        1,0,0,0,218,23,1,0,0,0,219,222,3,30,15,0,220,221,5,11,0,0,221,223,
        3,30,15,0,222,220,1,0,0,0,222,223,1,0,0,0,223,224,1,0,0,0,224,225,
        5,12,0,0,225,226,3,22,11,0,226,25,1,0,0,0,227,228,3,30,15,0,228,
        229,5,13,0,0,229,230,3,22,11,0,230,27,1,0,0,0,231,232,5,14,0,0,232,
        252,6,14,-1,0,233,234,5,53,0,0,234,252,6,14,-1,0,235,236,5,54,0,
        0,236,252,6,14,-1,0,237,238,3,30,15,0,238,239,6,14,-1,0,239,252,
        1,0,0,0,240,241,3,32,16,0,241,242,6,14,-1,0,242,252,1,0,0,0,243,
        244,3,34,17,0,244,245,6,14,-1,0,245,252,1,0,0,0,246,247,5,15,0,0,
        247,248,3,28,14,0,248,249,5,16,0,0,249,250,6,14,-1,0,250,252,1,0,
        0,0,251,231,1,0,0,0,251,233,1,0,0,0,251,235,1,0,0,0,251,237,1,0,
        0,0,251,240,1,0,0,0,251,243,1,0,0,0,251,246,1,0,0,0,252,29,1,0,0,
        0,253,255,5,17,0,0,254,256,5,55,0,0,255,254,1,0,0,0,255,256,1,0,
        0,0,256,31,1,0,0,0,257,259,3,30,15,0,258,257,1,0,0,0,258,259,1,0,
        0,0,259,260,1,0,0,0,260,262,5,18,0,0,261,263,5,55,0,0,262,261,1,
        0,0,0,262,263,1,0,0,0,263,268,1,0,0,0,264,266,5,18,0,0,265,267,5,
        55,0,0,266,265,1,0,0,0,266,267,1,0,0,0,267,269,1,0,0,0,268,264,1,
        0,0,0,268,269,1,0,0,0,269,33,1,0,0,0,270,271,3,44,22,0,271,35,1,
        0,0,0,272,273,3,30,15,0,273,274,6,18,-1,0,274,279,1,0,0,0,275,276,
        3,32,16,0,276,277,6,18,-1,0,277,279,1,0,0,0,278,272,1,0,0,0,278,
        275,1,0,0,0,279,283,1,0,0,0,280,282,3,28,14,0,281,280,1,0,0,0,282,
        285,1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,37,1,0,0,0,285,283,
        1,0,0,0,286,287,3,40,20,0,287,288,5,19,0,0,288,289,3,42,21,0,289,
        39,1,0,0,0,290,292,5,20,0,0,291,293,5,21,0,0,292,291,1,0,0,0,292,
        293,1,0,0,0,293,41,1,0,0,0,294,296,5,21,0,0,295,294,1,0,0,0,295,
        296,1,0,0,0,296,297,1,0,0,0,297,298,5,22,0,0,298,43,1,0,0,0,299,
        300,5,25,0,0,300,301,3,28,14,0,301,302,3,28,14,0,302,303,1,0,0,0,
        303,304,6,22,-1,0,304,386,1,0,0,0,305,306,5,35,0,0,306,310,3,28,
        14,0,307,309,3,28,14,0,308,307,1,0,0,0,309,312,1,0,0,0,310,308,1,
        0,0,0,310,311,1,0,0,0,311,313,1,0,0,0,312,310,1,0,0,0,313,314,6,
        22,-1,0,314,386,1,0,0,0,315,316,5,36,0,0,316,320,3,28,14,0,317,319,
        3,28,14,0,318,317,1,0,0,0,319,322,1,0,0,0,320,318,1,0,0,0,320,321,
        1,0,0,0,321,323,1,0,0,0,322,320,1,0,0,0,323,324,6,22,-1,0,324,386,
        1,0,0,0,325,326,5,32,0,0,326,327,3,28,14,0,327,328,6,22,-1,0,328,
        386,1,0,0,0,329,330,5,33,0,0,330,331,3,28,14,0,331,332,6,22,-1,0,
        332,386,1,0,0,0,333,334,5,34,0,0,334,335,3,28,14,0,335,336,3,28,
        14,0,336,337,6,22,-1,0,337,386,1,0,0,0,338,339,5,37,0,0,339,343,
        3,28,14,0,340,342,3,28,14,0,341,340,1,0,0,0,342,345,1,0,0,0,343,
        341,1,0,0,0,343,344,1,0,0,0,344,346,1,0,0,0,345,343,1,0,0,0,346,
        347,6,22,-1,0,347,386,1,0,0,0,348,349,5,26,0,0,349,350,3,28,14,0,
        350,351,3,28,14,0,351,352,6,22,-1,0,352,386,1,0,0,0,353,354,5,29,
        0,0,354,355,3,28,14,0,355,356,3,28,14,0,356,357,6,22,-1,0,357,386,
        1,0,0,0,358,359,5,27,0,0,359,360,3,28,14,0,360,361,3,28,14,0,361,
        362,6,22,-1,0,362,386,1,0,0,0,363,364,5,28,0,0,364,365,3,28,14,0,
        365,366,3,28,14,0,366,367,6,22,-1,0,367,386,1,0,0,0,368,369,5,30,
        0,0,369,370,3,28,14,0,370,371,3,28,14,0,371,372,1,0,0,0,372,373,
        6,22,-1,0,373,386,1,0,0,0,374,375,5,31,0,0,375,376,3,28,14,0,376,
        377,3,28,14,0,377,378,6,22,-1,0,378,386,1,0,0,0,379,380,5,39,0,0,
        380,386,6,22,-1,0,381,382,5,38,0,0,382,383,3,28,14,0,383,384,6,22,
        -1,0,384,386,1,0,0,0,385,299,1,0,0,0,385,305,1,0,0,0,385,315,1,0,
        0,0,385,325,1,0,0,0,385,329,1,0,0,0,385,333,1,0,0,0,385,338,1,0,
        0,0,385,348,1,0,0,0,385,353,1,0,0,0,385,358,1,0,0,0,385,363,1,0,
        0,0,385,368,1,0,0,0,385,374,1,0,0,0,385,379,1,0,0,0,385,381,1,0,
        0,0,386,45,1,0,0,0,387,388,5,1,0,0,388,405,6,23,-1,0,389,390,3,48,
        24,0,390,391,6,23,-1,0,391,405,1,0,0,0,392,393,3,50,25,0,393,394,
        6,23,-1,0,394,405,1,0,0,0,395,396,3,52,26,0,396,397,6,23,-1,0,397,
        405,1,0,0,0,398,399,3,54,27,0,399,400,6,23,-1,0,400,405,1,0,0,0,
        401,402,3,56,28,0,402,403,6,23,-1,0,403,405,1,0,0,0,404,387,1,0,
        0,0,404,389,1,0,0,0,404,392,1,0,0,0,404,395,1,0,0,0,404,398,1,0,
        0,0,404,401,1,0,0,0,405,47,1,0,0,0,406,407,5,46,0,0,407,408,3,4,
        2,0,408,409,5,47,0,0,409,49,1,0,0,0,410,411,5,44,0,0,411,412,3,4,
        2,0,412,413,5,45,0,0,413,51,1,0,0,0,414,415,5,50,0,0,415,416,3,4,
        2,0,416,417,5,52,0,0,417,53,1,0,0,0,418,419,5,48,0,0,419,420,3,4,
        2,0,420,421,5,49,0,0,421,55,1,0,0,0,422,423,5,41,0,0,423,424,3,4,
        2,0,424,425,5,51,0,0,425,426,6,28,-1,0,426,433,1,0,0,0,427,428,5,
        42,0,0,428,429,3,4,2,0,429,430,5,43,0,0,430,431,6,28,-1,0,431,433,
        1,0,0,0,432,422,1,0,0,0,432,427,1,0,0,0,433,57,1,0,0,0,434,435,5,
        55,0,0,435,59,1,0,0,0,31,68,76,78,105,123,136,141,153,162,170,183,
        197,206,217,222,251,255,258,262,266,268,278,283,292,295,310,320,
        343,385,404,432
    ]

class count_parser ( Parser ):

    grammarFileName = "count_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TEXT'", "'template'", "'block'", "'with'", 
                     "'/*'", "'*/'", "'if'", "'else'", "'range'", "'|'", 
                     "','", "':='", "'='", "'nil'", "'('", "')'", "'$'", 
                     "'.'", "'end'", "'{{'", "'-'", "'}}'", "'CONSTANT'", 
                     "'define'", "'and'", "'eq'", "'lt'", "'le'", "'ne'", 
                     "'gt'", "'ge'", "'len'", "'not'", "'or'", "'index'", 
                     "'slice'", "'printf'", "'print'", "'random_string'", 
                     "'Comment'", "'<a href=\"#\">'", "'<a href=\"'", "'\">abc</a>'", 
                     "'<script>'", "'</script>'", "'<style>'", "'</style>'", 
                     "'<br>'", "'</br>'", "'<img src=xx:'", "'</a>'", "'>'" ]

    symbolicNames = [ "<INVALID>", "Text", "Template", "Block", "With", 
                      "CommentBegin", "CommentEnd", "If", "Else", "Range", 
                      "Pipe", "Comma", "Assignment", "Equal", "Nil", "LeftParenthesis", 
                      "RightParenthesis", "Dollar", "Dot", "End", "BlockStart", 
                      "Dash", "BlockEnd", "Constant", "Define", "And", "Eq", 
                      "Lt", "Le", "Ne", "Gt", "Ge", "Len", "Not", "Or", 
                      "Index", "Slice", "Printf", "Myprint", "Random", "AnyText", 
                      "AStart", "HrefStart", "HrefEnd", "ScriptStart", "ScriptEnd", 
                      "StyleStart", "StyleEnd", "BrStart", "BrEnd", "ImgStart", 
                      "AEnd", "ImgEnd", "StringConstant", "NumberConstant", 
                      "Name", "WS" ]

    RULE_start = 0
    RULE_template = 1
    RULE_goaction = 2
    RULE_commentaction = 3
    RULE_pipelineaction = 4
    RULE_ifaction = 5
    RULE_rangeaction = 6
    RULE_templateaction = 7
    RULE_defineAction = 8
    RULE_blockAction = 9
    RULE_withAction = 10
    RULE_pipeline = 11
    RULE_vardeclarepipeline = 12
    RULE_varassignpipeline = 13
    RULE_argument = 14
    RULE_variable = 15
    RULE_fields = 16
    RULE_funccall = 17
    RULE_methodcall = 18
    RULE_end = 19
    RULE_ld = 20
    RULE_rd = 21
    RULE_globalfunctions = 22
    RULE_text = 23
    RULE_style = 24
    RULE_js = 25
    RULE_img = 26
    RULE_default = 27
    RULE_href = 28
    RULE_local = 29

    ruleNames =  [ "start", "template", "goaction", "commentaction", "pipelineaction", 
                   "ifaction", "rangeaction", "templateaction", "defineAction", 
                   "blockAction", "withAction", "pipeline", "vardeclarepipeline", 
                   "varassignpipeline", "argument", "variable", "fields", 
                   "funccall", "methodcall", "end", "ld", "rd", "globalfunctions", 
                   "text", "style", "js", "img", "default", "href", "local" ]

    EOF = Token.EOF
    Text=1
    Template=2
    Block=3
    With=4
    CommentBegin=5
    CommentEnd=6
    If=7
    Else=8
    Range=9
    Pipe=10
    Comma=11
    Assignment=12
    Equal=13
    Nil=14
    LeftParenthesis=15
    RightParenthesis=16
    Dollar=17
    Dot=18
    End=19
    BlockStart=20
    Dash=21
    BlockEnd=22
    Constant=23
    Define=24
    And=25
    Eq=26
    Lt=27
    Le=28
    Ne=29
    Gt=30
    Ge=31
    Len=32
    Not=33
    Or=34
    Index=35
    Slice=36
    Printf=37
    Myprint=38
    Random=39
    AnyText=40
    AStart=41
    HrefStart=42
    HrefEnd=43
    ScriptStart=44
    ScriptEnd=45
    StyleStart=46
    StyleEnd=47
    BrStart=48
    BrEnd=49
    ImgStart=50
    AEnd=51
    ImgEnd=52
    StringConstant=53
    NumberConstant=54
    Name=55
    WS=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        with open('counter.json', 'r+') as f:
            self.counter = json.load(f)
        self.counter['template'] = self.counter['template'] if 'template' in self.counter else {};
        self.counter['goaction'] = self.counter['goaction'] if 'goaction' in self.counter else {};
        self.counter['pipelineaction'] = self.counter['pipelineaction'] if 'pipelineaction' in self.counter else {};
        self.counter['rangeaction'] = self.counter['rangeaction'] if 'rangeaction' in self.counter else {};
        self.counter['pipeline'] = self.counter['pipeline'] if 'pipeline' in self.counter else {};
        self.counter['argument'] = self.counter['argument'] if 'argument' in self.counter else {};
        self.counter['methodcall'] = self.counter['methodcall'] if 'methodcall' in self.counter else {};
        self.counter['globalfunctions'] = self.counter['globalfunctions'] if 'globalfunctions' in self.counter else {};
        self.counter['text'] = self.counter['text'] if 'text' in self.counter else {};
        self.counter['href'] = self.counter['href'] if 'href' in self.counter else {};
        self.counter['globalfunctions']['myprint'] = self.counter['globalfunctions'].get('myprint', 0);
        self.counter['globalfunctions']['random'] = self.counter['globalfunctions'].get('random', 0);



    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def template(self):
            return self.getTypedRuleContext(count_parser.TemplateContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = count_parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.template()
            self._ctx.stop = self._input.LT(-1)

            print(self.counter); 
            with open('counter.json', 'w') as f:
                json.dump(self.counter, f)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.TextContext)
            else:
                return self.getTypedRuleContext(count_parser.TextContext,i)


        def goaction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.GoactionContext)
            else:
                return self.getTypedRuleContext(count_parser.GoactionContext,i)


        def getRuleIndex(self):
            return count_parser.RULE_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate" ):
                listener.enterTemplate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate" ):
                listener.exitTemplate(self)




    def template(self):

        localctx = count_parser.TemplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_template)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 41, 42, 44, 46, 48, 50]:
                self.state = 62
                self.text()
                self.counter[inspect.stack()[0][3]]['text'] = self.counter[inspect.stack()[0][3]]['text'] + 1 if 'text' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [20]:
                self.state = 65
                self.goaction()
                self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1
                pass
            else:
                raise NoViableAltException(self)

            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 76
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 41, 42, 44, 46, 48, 50]:
                        self.state = 70
                        self.text()
                        self.counter[inspect.stack()[0][3]]['text'] = self.counter[inspect.stack()[0][3]]['text'] + 1 if 'text' in self.counter[inspect.stack()[0][3]] else 1
                        pass
                    elif token in [20]:
                        self.state = 73
                        self.goaction()
                        self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commentaction(self):
            return self.getTypedRuleContext(count_parser.CommentactionContext,0)


        def pipelineaction(self):
            return self.getTypedRuleContext(count_parser.PipelineactionContext,0)


        def ifaction(self):
            return self.getTypedRuleContext(count_parser.IfactionContext,0)


        def rangeaction(self):
            return self.getTypedRuleContext(count_parser.RangeactionContext,0)


        def templateaction(self):
            return self.getTypedRuleContext(count_parser.TemplateactionContext,0)


        def blockAction(self):
            return self.getTypedRuleContext(count_parser.BlockActionContext,0)


        def withAction(self):
            return self.getTypedRuleContext(count_parser.WithActionContext,0)


        def defineAction(self):
            return self.getTypedRuleContext(count_parser.DefineActionContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_goaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoaction" ):
                listener.enterGoaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoaction" ):
                listener.exitGoaction(self)




    def goaction(self):

        localctx = count_parser.GoactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_goaction)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.commentaction()
                self.counter[inspect.stack()[0][3]]['commentaction'] = self.counter[inspect.stack()[0][3]]['commentaction'] + 1 if 'commentaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.pipelineaction()
                self.counter[inspect.stack()[0][3]]['pipelineaction'] = self.counter[inspect.stack()[0][3]]['pipelineaction'] + 1 if 'pipelineaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.ifaction()
                self.counter[inspect.stack()[0][3]]['ifaction'] = self.counter[inspect.stack()[0][3]]['ifaction'] + 1 if 'ifaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.rangeaction()
                self.counter[inspect.stack()[0][3]]['rangeaction'] = self.counter[inspect.stack()[0][3]]['rangeaction'] + 1 if 'rangeaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.templateaction()
                self.counter[inspect.stack()[0][3]]['templateaction'] = self.counter[inspect.stack()[0][3]]['templateaction'] + 1 if 'templateaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.blockAction()
                self.counter[inspect.stack()[0][3]]['blockAction'] = self.counter[inspect.stack()[0][3]]['blockAction'] + 1 if 'blockAction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 99
                self.withAction()
                self.counter[inspect.stack()[0][3]]['withAction'] = self.counter[inspect.stack()[0][3]]['withAction'] + 1 if 'withAction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 102
                self.defineAction()
                self.counter[inspect.stack()[0][3]]['defineAction'] = self.counter[inspect.stack()[0][3]]['defineAction'] + 1 if 'defineAction' in self.counter[inspect.stack()[0][3]] else 1
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self):
            return self.getTypedRuleContext(count_parser.LdContext,0)


        def CommentBegin(self):
            return self.getToken(count_parser.CommentBegin, 0)

        def AnyText(self):
            return self.getToken(count_parser.AnyText, 0)

        def CommentEnd(self):
            return self.getToken(count_parser.CommentEnd, 0)

        def rd(self):
            return self.getTypedRuleContext(count_parser.RdContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_commentaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentaction" ):
                listener.enterCommentaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentaction" ):
                listener.exitCommentaction(self)




    def commentaction(self):

        localctx = count_parser.CommentactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_commentaction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.ld()
            self.state = 108
            self.match(count_parser.CommentBegin)
            self.state = 109
            self.match(count_parser.AnyText)
            self.state = 110
            self.match(count_parser.CommentEnd)
            self.state = 111
            self.rd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipelineactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self):
            return self.getTypedRuleContext(count_parser.LdContext,0)


        def rd(self):
            return self.getTypedRuleContext(count_parser.RdContext,0)


        def pipeline(self):
            return self.getTypedRuleContext(count_parser.PipelineContext,0)


        def vardeclarepipeline(self):
            return self.getTypedRuleContext(count_parser.VardeclarepipelineContext,0)


        def varassignpipeline(self):
            return self.getTypedRuleContext(count_parser.VarassignpipelineContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_pipelineaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipelineaction" ):
                listener.enterPipelineaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipelineaction" ):
                listener.exitPipelineaction(self)




    def pipelineaction(self):

        localctx = count_parser.PipelineactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pipelineaction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.ld()
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 114
                self.pipeline()
                self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 117
                self.vardeclarepipeline()
                self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.state = 120
                self.varassignpipeline()
                self.counter[inspect.stack()[0][3]]['varassignpipeline'] = self.counter[inspect.stack()[0][3]]['varassignpipeline'] + 1 if 'varassignpipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 125
            self.rd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.LdContext)
            else:
                return self.getTypedRuleContext(count_parser.LdContext,i)


        def If(self, i:int=None):
            if i is None:
                return self.getTokens(count_parser.If)
            else:
                return self.getToken(count_parser.If, i)

        def pipeline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.PipelineContext)
            else:
                return self.getTypedRuleContext(count_parser.PipelineContext,i)


        def rd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.RdContext)
            else:
                return self.getTypedRuleContext(count_parser.RdContext,i)


        def template(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.TemplateContext)
            else:
                return self.getTypedRuleContext(count_parser.TemplateContext,i)


        def end(self):
            return self.getTypedRuleContext(count_parser.EndContext,0)


        def Else(self):
            return self.getToken(count_parser.Else, 0)

        def getRuleIndex(self):
            return count_parser.RULE_ifaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfaction" ):
                listener.enterIfaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfaction" ):
                listener.exitIfaction(self)




    def ifaction(self):

        localctx = count_parser.IfactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifaction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.ld()
            self.state = 128
            self.match(count_parser.If)
            self.state = 129
            self.pipeline()
            self.state = 130
            self.rd()
            self.state = 131
            self.template()
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 132
                self.ld()
                self.state = 133
                self.match(count_parser.Else)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 134
                    self.match(count_parser.If)
                    self.state = 135
                    self.pipeline()


                self.state = 138
                self.rd()
                self.state = 139
                self.template()


            self.state = 143
            self.end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.LdContext)
            else:
                return self.getTypedRuleContext(count_parser.LdContext,i)


        def Range(self):
            return self.getToken(count_parser.Range, 0)

        def rd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.RdContext)
            else:
                return self.getTypedRuleContext(count_parser.RdContext,i)


        def template(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.TemplateContext)
            else:
                return self.getTypedRuleContext(count_parser.TemplateContext,i)


        def end(self):
            return self.getTypedRuleContext(count_parser.EndContext,0)


        def pipeline(self):
            return self.getTypedRuleContext(count_parser.PipelineContext,0)


        def vardeclarepipeline(self):
            return self.getTypedRuleContext(count_parser.VardeclarepipelineContext,0)


        def Else(self):
            return self.getToken(count_parser.Else, 0)

        def getRuleIndex(self):
            return count_parser.RULE_rangeaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeaction" ):
                listener.enterRangeaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeaction" ):
                listener.exitRangeaction(self)




    def rangeaction(self):

        localctx = count_parser.RangeactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rangeaction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.ld()
            self.state = 146
            self.match(count_parser.Range)
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 147
                self.pipeline()
                self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 150
                self.vardeclarepipeline()
                self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 155
            self.rd()
            self.state = 156
            self.template()
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 157
                self.ld()
                self.state = 158
                self.match(count_parser.Else)
                self.state = 159
                self.rd()
                self.state = 160
                self.template()


            self.state = 164
            self.end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self):
            return self.getTypedRuleContext(count_parser.LdContext,0)


        def Template(self):
            return self.getToken(count_parser.Template, 0)

        def StringConstant(self):
            return self.getToken(count_parser.StringConstant, 0)

        def rd(self):
            return self.getTypedRuleContext(count_parser.RdContext,0)


        def pipeline(self):
            return self.getTypedRuleContext(count_parser.PipelineContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_templateaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateaction" ):
                listener.enterTemplateaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateaction" ):
                listener.exitTemplateaction(self)




    def templateaction(self):

        localctx = count_parser.TemplateactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_templateaction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.ld()
            self.state = 167
            self.match(count_parser.Template)
            self.state = 168
            self.match(count_parser.StringConstant)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 27022697242738688) != 0):
                self.state = 169
                self.pipeline()


            self.state = 172
            self.rd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self):
            return self.getTypedRuleContext(count_parser.LdContext,0)


        def Define(self):
            return self.getToken(count_parser.Define, 0)

        def StringConstant(self):
            return self.getToken(count_parser.StringConstant, 0)

        def rd(self):
            return self.getTypedRuleContext(count_parser.RdContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_defineAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineAction" ):
                listener.enterDefineAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineAction" ):
                listener.exitDefineAction(self)




    def defineAction(self):

        localctx = count_parser.DefineActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_defineAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.ld()
            self.state = 175
            self.match(count_parser.Define)
            self.state = 176
            self.match(count_parser.StringConstant)
            self.state = 177
            self.rd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self):
            return self.getTypedRuleContext(count_parser.LdContext,0)


        def Block(self):
            return self.getToken(count_parser.Block, 0)

        def Name(self):
            return self.getToken(count_parser.Name, 0)

        def rd(self):
            return self.getTypedRuleContext(count_parser.RdContext,0)


        def pipeline(self):
            return self.getTypedRuleContext(count_parser.PipelineContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_blockAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockAction" ):
                listener.enterBlockAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockAction" ):
                listener.exitBlockAction(self)




    def blockAction(self):

        localctx = count_parser.BlockActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_blockAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.ld()
            self.state = 180
            self.match(count_parser.Block)
            self.state = 181
            self.match(count_parser.Name)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 27022697242738688) != 0):
                self.state = 182
                self.pipeline()


            self.state = 185
            self.rd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.LdContext)
            else:
                return self.getTypedRuleContext(count_parser.LdContext,i)


        def With(self):
            return self.getToken(count_parser.With, 0)

        def pipeline(self):
            return self.getTypedRuleContext(count_parser.PipelineContext,0)


        def rd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.RdContext)
            else:
                return self.getTypedRuleContext(count_parser.RdContext,i)


        def template(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.TemplateContext)
            else:
                return self.getTypedRuleContext(count_parser.TemplateContext,i)


        def end(self):
            return self.getTypedRuleContext(count_parser.EndContext,0)


        def Else(self):
            return self.getToken(count_parser.Else, 0)

        def getRuleIndex(self):
            return count_parser.RULE_withAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithAction" ):
                listener.enterWithAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithAction" ):
                listener.exitWithAction(self)




    def withAction(self):

        localctx = count_parser.WithActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_withAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.ld()
            self.state = 188
            self.match(count_parser.With)
            self.state = 189
            self.pipeline()
            self.state = 190
            self.rd()
            self.state = 191
            self.template()
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 192
                self.ld()
                self.state = 193
                self.match(count_parser.Else)
                self.state = 194
                self.rd()
                self.state = 195
                self.template()


            self.state = 199
            self.end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipelineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.ArgumentContext)
            else:
                return self.getTypedRuleContext(count_parser.ArgumentContext,i)


        def Pipe(self, i:int=None):
            if i is None:
                return self.getTokens(count_parser.Pipe)
            else:
                return self.getToken(count_parser.Pipe, i)

        def methodcall(self):
            return self.getTypedRuleContext(count_parser.MethodcallContext,0)


        def funccall(self):
            return self.getTypedRuleContext(count_parser.FunccallContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_pipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipeline" ):
                listener.enterPipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipeline" ):
                listener.exitPipeline(self)




    def pipeline(self):

        localctx = count_parser.PipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pipeline)
        self._la = 0 # Token type
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.argument()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 202
                    self.match(count_parser.Pipe)
                    self.state = 203
                    self.argument()
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.counter[inspect.stack()[0][3]]['argument'] = self.counter[inspect.stack()[0][3]]['argument'] + 1 if 'argument' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.methodcall()
                self.counter[inspect.stack()[0][3]]['methodcall'] = self.counter[inspect.stack()[0][3]]['methodcall'] + 1 if 'methodcall' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.funccall()
                self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclarepipelineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.VariableContext)
            else:
                return self.getTypedRuleContext(count_parser.VariableContext,i)


        def Assignment(self):
            return self.getToken(count_parser.Assignment, 0)

        def pipeline(self):
            return self.getTypedRuleContext(count_parser.PipelineContext,0)


        def Comma(self):
            return self.getToken(count_parser.Comma, 0)

        def getRuleIndex(self):
            return count_parser.RULE_vardeclarepipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardeclarepipeline" ):
                listener.enterVardeclarepipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardeclarepipeline" ):
                listener.exitVardeclarepipeline(self)




    def vardeclarepipeline(self):

        localctx = count_parser.VardeclarepipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vardeclarepipeline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.variable()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 220
                self.match(count_parser.Comma)
                self.state = 221
                self.variable()


            self.state = 224
            self.match(count_parser.Assignment)
            self.state = 225
            self.pipeline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarassignpipelineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(count_parser.VariableContext,0)


        def Equal(self):
            return self.getToken(count_parser.Equal, 0)

        def pipeline(self):
            return self.getTypedRuleContext(count_parser.PipelineContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_varassignpipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarassignpipeline" ):
                listener.enterVarassignpipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarassignpipeline" ):
                listener.exitVarassignpipeline(self)




    def varassignpipeline(self):

        localctx = count_parser.VarassignpipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varassignpipeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.variable()
            self.state = 228
            self.match(count_parser.Equal)
            self.state = 229
            self.pipeline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Nil(self):
            return self.getToken(count_parser.Nil, 0)

        def StringConstant(self):
            return self.getToken(count_parser.StringConstant, 0)

        def NumberConstant(self):
            return self.getToken(count_parser.NumberConstant, 0)

        def variable(self):
            return self.getTypedRuleContext(count_parser.VariableContext,0)


        def fields(self):
            return self.getTypedRuleContext(count_parser.FieldsContext,0)


        def funccall(self):
            return self.getTypedRuleContext(count_parser.FunccallContext,0)


        def LeftParenthesis(self):
            return self.getToken(count_parser.LeftParenthesis, 0)

        def argument(self):
            return self.getTypedRuleContext(count_parser.ArgumentContext,0)


        def RightParenthesis(self):
            return self.getToken(count_parser.RightParenthesis, 0)

        def getRuleIndex(self):
            return count_parser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = count_parser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argument)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(count_parser.Nil)
                self.counter[inspect.stack()[0][3]]['Nil'] = self.counter[inspect.stack()[0][3]]['Nil'] + 1 if 'Nil' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(count_parser.StringConstant)
                self.counter[inspect.stack()[0][3]]['StringConstant'] = self.counter[inspect.stack()[0][3]]['StringConstant'] + 1 if 'StringConstant' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.match(count_parser.NumberConstant)
                self.counter[inspect.stack()[0][3]]['NumberConstant'] = self.counter[inspect.stack()[0][3]]['NumberConstant'] + 1 if 'NumberConstant' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.variable()
                self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.fields()
                self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 243
                self.funccall()
                self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 246
                self.match(count_parser.LeftParenthesis)
                self.state = 247
                self.argument()
                self.state = 248
                self.match(count_parser.RightParenthesis)
                self.counter[inspect.stack()[0][3]]['LeftParenthesis'] = self.counter[inspect.stack()[0][3]]['LeftParenthesis'] + 1 if 'LeftParenthesis' in self.counter[inspect.stack()[0][3]] else 1
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Dollar(self):
            return self.getToken(count_parser.Dollar, 0)

        def Name(self):
            return self.getToken(count_parser.Name, 0)

        def getRuleIndex(self):
            return count_parser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = count_parser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(count_parser.Dollar)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 254
                self.match(count_parser.Name)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(count_parser.Dot)
            else:
                return self.getToken(count_parser.Dot, i)

        def variable(self):
            return self.getTypedRuleContext(count_parser.VariableContext,0)


        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(count_parser.Name)
            else:
                return self.getToken(count_parser.Name, i)

        def getRuleIndex(self):
            return count_parser.RULE_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFields" ):
                listener.enterFields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFields" ):
                listener.exitFields(self)




    def fields(self):

        localctx = count_parser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 257
                self.variable()


            self.state = 260
            self.match(count_parser.Dot)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 261
                self.match(count_parser.Name)


            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 264
                self.match(count_parser.Dot)
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 265
                    self.match(count_parser.Name)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalfunctions(self):
            return self.getTypedRuleContext(count_parser.GlobalfunctionsContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_funccall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunccall" ):
                listener.enterFunccall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunccall" ):
                listener.exitFunccall(self)




    def funccall(self):

        localctx = count_parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.globalfunctions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(count_parser.VariableContext,0)


        def fields(self):
            return self.getTypedRuleContext(count_parser.FieldsContext,0)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.ArgumentContext)
            else:
                return self.getTypedRuleContext(count_parser.ArgumentContext,i)


        def getRuleIndex(self):
            return count_parser.RULE_methodcall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodcall" ):
                listener.enterMethodcall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodcall" ):
                listener.exitMethodcall(self)




    def methodcall(self):

        localctx = count_parser.MethodcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_methodcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 272
                self.variable()
                self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 275
                self.fields()
                self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 27022697242738688) != 0):
                self.state = 280
                self.argument()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self):
            return self.getTypedRuleContext(count_parser.LdContext,0)


        def End(self):
            return self.getToken(count_parser.End, 0)

        def rd(self):
            return self.getTypedRuleContext(count_parser.RdContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)




    def end(self):

        localctx = count_parser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.ld()
            self.state = 287
            self.match(count_parser.End)
            self.state = 288
            self.rd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BlockStart(self):
            return self.getToken(count_parser.BlockStart, 0)

        def Dash(self):
            return self.getToken(count_parser.Dash, 0)

        def getRuleIndex(self):
            return count_parser.RULE_ld

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLd" ):
                listener.enterLd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLd" ):
                listener.exitLd(self)




    def ld(self):

        localctx = count_parser.LdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ld)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(count_parser.BlockStart)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 291
                self.match(count_parser.Dash)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BlockEnd(self):
            return self.getToken(count_parser.BlockEnd, 0)

        def Dash(self):
            return self.getToken(count_parser.Dash, 0)

        def getRuleIndex(self):
            return count_parser.RULE_rd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRd" ):
                listener.enterRd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRd" ):
                listener.exitRd(self)




    def rd(self):

        localctx = count_parser.RdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_rd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 294
                self.match(count_parser.Dash)


            self.state = 297
            self.match(count_parser.BlockEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalfunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def And(self):
            return self.getToken(count_parser.And, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.ArgumentContext)
            else:
                return self.getTypedRuleContext(count_parser.ArgumentContext,i)


        def Index(self):
            return self.getToken(count_parser.Index, 0)

        def Slice(self):
            return self.getToken(count_parser.Slice, 0)

        def Len(self):
            return self.getToken(count_parser.Len, 0)

        def Not(self):
            return self.getToken(count_parser.Not, 0)

        def Or(self):
            return self.getToken(count_parser.Or, 0)

        def Printf(self):
            return self.getToken(count_parser.Printf, 0)

        def Eq(self):
            return self.getToken(count_parser.Eq, 0)

        def Ne(self):
            return self.getToken(count_parser.Ne, 0)

        def Lt(self):
            return self.getToken(count_parser.Lt, 0)

        def Le(self):
            return self.getToken(count_parser.Le, 0)

        def Gt(self):
            return self.getToken(count_parser.Gt, 0)

        def Ge(self):
            return self.getToken(count_parser.Ge, 0)

        def Random(self):
            return self.getToken(count_parser.Random, 0)

        def Myprint(self):
            return self.getToken(count_parser.Myprint, 0)

        def getRuleIndex(self):
            return count_parser.RULE_globalfunctions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalfunctions" ):
                listener.enterGlobalfunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalfunctions" ):
                listener.exitGlobalfunctions(self)




    def globalfunctions(self):

        localctx = count_parser.GlobalfunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_globalfunctions)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(count_parser.And)
                self.state = 300
                self.argument()
                self.state = 301
                self.argument()
                self.counter[inspect.stack()[0][3]]['And'] = self.counter[inspect.stack()[0][3]]['And'] + 1 if 'And' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.match(count_parser.Index)
                self.state = 306
                self.argument()
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 307
                        self.argument() 
                    self.state = 312
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                self.counter[inspect.stack()[0][3]]['Index'] = self.counter[inspect.stack()[0][3]]['Index'] + 1 if 'Index' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.match(count_parser.Slice)
                self.state = 316
                self.argument()
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 317
                        self.argument() 
                    self.state = 322
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.counter[inspect.stack()[0][3]]['Slice'] = self.counter[inspect.stack()[0][3]]['Slice'] + 1 if 'Slice' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
                self.match(count_parser.Len)
                self.state = 326
                self.argument()
                self.counter[inspect.stack()[0][3]]['Len'] = self.counter[inspect.stack()[0][3]]['Len'] + 1 if 'Len' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.match(count_parser.Not)
                self.state = 330
                self.argument()
                self.counter[inspect.stack()[0][3]]['Len'] = self.counter[inspect.stack()[0][3]]['Len'] + 1 if 'Len' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 333
                self.match(count_parser.Or)
                self.state = 334
                self.argument()
                self.state = 335
                self.argument()
                self.counter[inspect.stack()[0][3]]['Or'] = self.counter[inspect.stack()[0][3]]['Or'] + 1 if 'Or' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 7)
                self.state = 338
                self.match(count_parser.Printf)
                self.state = 339
                self.argument()
                self.state = 343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 340
                        self.argument() 
                    self.state = 345
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.counter[inspect.stack()[0][3]]['Printf'] = self.counter[inspect.stack()[0][3]]['Printf'] + 1 if 'Printf' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 8)
                self.state = 348
                self.match(count_parser.Eq)
                self.state = 349
                self.argument()
                self.state = 350
                self.argument()
                self.counter[inspect.stack()[0][3]]['Eq'] = self.counter[inspect.stack()[0][3]]['Eq'] + 1 if 'Eq' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 9)
                self.state = 353
                self.match(count_parser.Ne)
                self.state = 354
                self.argument()
                self.state = 355
                self.argument()
                self.counter[inspect.stack()[0][3]]['Ne'] = self.counter[inspect.stack()[0][3]]['Ne'] + 1 if 'Ne' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 10)
                self.state = 358
                self.match(count_parser.Lt)
                self.state = 359
                self.argument()
                self.state = 360
                self.argument()
                self.counter[inspect.stack()[0][3]]['Lt'] = self.counter[inspect.stack()[0][3]]['Lt'] + 1 if 'Lt' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 11)
                self.state = 363
                self.match(count_parser.Le)
                self.state = 364
                self.argument()
                self.state = 365
                self.argument()
                self.counter[inspect.stack()[0][3]]['Le'] = self.counter[inspect.stack()[0][3]]['Le'] + 1 if 'Le' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 12)
                self.state = 368
                self.match(count_parser.Gt)
                self.state = 369
                self.argument()
                self.state = 370
                self.argument()
                self.counter[inspect.stack()[0][3]]['Gt'] = self.counter[inspect.stack()[0][3]]['Gt'] + 1 if 'Gt' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 13)
                self.state = 374
                self.match(count_parser.Ge)
                self.state = 375
                self.argument()
                self.state = 376
                self.argument()
                self.counter[inspect.stack()[0][3]]['Ge'] = self.counter[inspect.stack()[0][3]]['Ge'] + 1 if 'Ge' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 14)
                self.state = 379
                self.match(count_parser.Random)
                self.counter[inspect.stack()[0][3]]['random'] = self.counter[inspect.stack()[0][3]]['random'] + 1 if 'random' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 15)
                self.state = 381
                self.match(count_parser.Myprint)
                self.state = 382
                self.argument()
                self.counter[inspect.stack()[0][3]]['myprint'] = self.counter[inspect.stack()[0][3]]['myprint'] + 1 if 'myprint' in self.counter[inspect.stack()[0][3]] else 1
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Text(self):
            return self.getToken(count_parser.Text, 0)

        def style(self):
            return self.getTypedRuleContext(count_parser.StyleContext,0)


        def js(self):
            return self.getTypedRuleContext(count_parser.JsContext,0)


        def img(self):
            return self.getTypedRuleContext(count_parser.ImgContext,0)


        def default(self):
            return self.getTypedRuleContext(count_parser.DefaultContext,0)


        def href(self):
            return self.getTypedRuleContext(count_parser.HrefContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)




    def text(self):

        localctx = count_parser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_text)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(count_parser.Text)
                self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.style()
                self.counter[inspect.stack()[0][3]]['style'] = self.counter[inspect.stack()[0][3]]['style'] + 1 if 'style' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.js()
                self.counter[inspect.stack()[0][3]]['js'] = self.counter[inspect.stack()[0][3]]['js'] + 1 if 'js' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                self.img()
                self.counter[inspect.stack()[0][3]]['img'] = self.counter[inspect.stack()[0][3]]['img'] + 1 if 'img' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 5)
                self.state = 398
                self.default()
                self.counter[inspect.stack()[0][3]]['default'] = self.counter[inspect.stack()[0][3]]['default'] + 1 if 'default' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [41, 42]:
                self.enterOuterAlt(localctx, 6)
                self.state = 401
                self.href()
                self.counter[inspect.stack()[0][3]]['href'] = self.counter[inspect.stack()[0][3]]['href'] + 1 if 'href' in self.counter[inspect.stack()[0][3]] else 1
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StyleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StyleStart(self):
            return self.getToken(count_parser.StyleStart, 0)

        def goaction(self):
            return self.getTypedRuleContext(count_parser.GoactionContext,0)


        def StyleEnd(self):
            return self.getToken(count_parser.StyleEnd, 0)

        def getRuleIndex(self):
            return count_parser.RULE_style

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStyle" ):
                listener.enterStyle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStyle" ):
                listener.exitStyle(self)




    def style(self):

        localctx = count_parser.StyleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_style)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(count_parser.StyleStart)
            self.state = 407
            self.goaction()
            self.state = 408
            self.match(count_parser.StyleEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ScriptStart(self):
            return self.getToken(count_parser.ScriptStart, 0)

        def goaction(self):
            return self.getTypedRuleContext(count_parser.GoactionContext,0)


        def ScriptEnd(self):
            return self.getToken(count_parser.ScriptEnd, 0)

        def getRuleIndex(self):
            return count_parser.RULE_js

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJs" ):
                listener.enterJs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJs" ):
                listener.exitJs(self)




    def js(self):

        localctx = count_parser.JsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_js)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(count_parser.ScriptStart)
            self.state = 411
            self.goaction()
            self.state = 412
            self.match(count_parser.ScriptEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ImgStart(self):
            return self.getToken(count_parser.ImgStart, 0)

        def goaction(self):
            return self.getTypedRuleContext(count_parser.GoactionContext,0)


        def ImgEnd(self):
            return self.getToken(count_parser.ImgEnd, 0)

        def getRuleIndex(self):
            return count_parser.RULE_img

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImg" ):
                listener.enterImg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImg" ):
                listener.exitImg(self)




    def img(self):

        localctx = count_parser.ImgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_img)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(count_parser.ImgStart)
            self.state = 415
            self.goaction()
            self.state = 416
            self.match(count_parser.ImgEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BrStart(self):
            return self.getToken(count_parser.BrStart, 0)

        def goaction(self):
            return self.getTypedRuleContext(count_parser.GoactionContext,0)


        def BrEnd(self):
            return self.getToken(count_parser.BrEnd, 0)

        def getRuleIndex(self):
            return count_parser.RULE_default

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault" ):
                listener.enterDefault(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault" ):
                listener.exitDefault(self)




    def default(self):

        localctx = count_parser.DefaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(count_parser.BrStart)
            self.state = 419
            self.goaction()
            self.state = 420
            self.match(count_parser.BrEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HrefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AStart(self):
            return self.getToken(count_parser.AStart, 0)

        def goaction(self):
            return self.getTypedRuleContext(count_parser.GoactionContext,0)


        def AEnd(self):
            return self.getToken(count_parser.AEnd, 0)

        def HrefStart(self):
            return self.getToken(count_parser.HrefStart, 0)

        def HrefEnd(self):
            return self.getToken(count_parser.HrefEnd, 0)

        def getRuleIndex(self):
            return count_parser.RULE_href

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHref" ):
                listener.enterHref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHref" ):
                listener.exitHref(self)




    def href(self):

        localctx = count_parser.HrefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_href)
        try:
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.match(count_parser.AStart)
                self.state = 423
                self.goaction()
                self.state = 424
                self.match(count_parser.AEnd)
                self.counter[inspect.stack()[0][3]]['AStart'] = self.counter[inspect.stack()[0][3]]['AStart'] + 1 if 'AStart' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(count_parser.HrefStart)
                self.state = 428
                self.goaction()
                self.state = 429
                self.match(count_parser.HrefEnd)
                self.counter[inspect.stack()[0][3]]['HrefStart'] = self.counter[inspect.stack()[0][3]]['HrefStart'] + 1 if 'HrefStart' in self.counter[inspect.stack()[0][3]] else 1
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(count_parser.Name, 0)

        def getRuleIndex(self):
            return count_parser.RULE_local

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal" ):
                listener.enterLocal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal" ):
                listener.exitLocal(self)




    def local(self):

        localctx = count_parser.LocalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_local)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(count_parser.Name)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





