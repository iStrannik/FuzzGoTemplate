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
        4,1,42,379,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,
        1,56,8,1,1,1,1,1,1,1,1,1,1,1,5,1,63,8,1,10,1,12,1,66,9,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,110,8,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,123,8,5,1,5,1,5,1,5,3,5,128,8,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,140,8,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,149,8,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,157,8,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,170,8,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,184,8,10,1,
        10,1,10,1,11,1,11,1,11,5,11,191,8,11,10,11,12,11,194,9,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,204,8,11,1,12,1,12,1,12,3,
        12,209,8,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,3,14,238,8,14,1,15,1,15,3,15,242,8,15,1,16,3,16,
        245,8,16,1,16,1,16,3,16,249,8,16,1,16,1,16,3,16,253,8,16,3,16,255,
        8,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,265,8,18,1,18,
        5,18,268,8,18,10,18,12,18,271,9,18,1,19,1,19,1,19,1,19,1,20,1,20,
        3,20,279,8,20,1,21,3,21,282,8,21,1,21,1,21,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,5,22,295,8,22,10,22,12,22,298,9,22,1,22,1,
        22,1,22,1,22,1,22,5,22,305,8,22,10,22,12,22,308,9,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,5,22,328,8,22,10,22,12,22,331,9,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,5,22,368,8,22,10,22,12,22,371,9,22,1,
        22,1,22,3,22,375,8,22,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,0,409,0,48,1,0,0,
        0,2,55,1,0,0,0,4,91,1,0,0,0,6,93,1,0,0,0,8,99,1,0,0,0,10,113,1,0,
        0,0,12,131,1,0,0,0,14,152,1,0,0,0,16,160,1,0,0,0,18,165,1,0,0,0,
        20,173,1,0,0,0,22,203,1,0,0,0,24,205,1,0,0,0,26,213,1,0,0,0,28,237,
        1,0,0,0,30,239,1,0,0,0,32,244,1,0,0,0,34,256,1,0,0,0,36,264,1,0,
        0,0,38,272,1,0,0,0,40,276,1,0,0,0,42,281,1,0,0,0,44,374,1,0,0,0,
        46,376,1,0,0,0,48,49,3,2,1,0,49,1,1,0,0,0,50,51,5,1,0,0,51,56,6,
        1,-1,0,52,53,3,4,2,0,53,54,6,1,-1,0,54,56,1,0,0,0,55,50,1,0,0,0,
        55,52,1,0,0,0,56,64,1,0,0,0,57,58,5,1,0,0,58,63,6,1,-1,0,59,60,3,
        4,2,0,60,61,6,1,-1,0,61,63,1,0,0,0,62,57,1,0,0,0,62,59,1,0,0,0,63,
        66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,3,1,0,0,0,66,64,1,0,0,
        0,67,68,3,6,3,0,68,69,6,2,-1,0,69,92,1,0,0,0,70,71,3,8,4,0,71,72,
        6,2,-1,0,72,92,1,0,0,0,73,74,3,10,5,0,74,75,6,2,-1,0,75,92,1,0,0,
        0,76,77,3,12,6,0,77,78,6,2,-1,0,78,92,1,0,0,0,79,80,3,14,7,0,80,
        81,6,2,-1,0,81,92,1,0,0,0,82,83,3,18,9,0,83,84,6,2,-1,0,84,92,1,
        0,0,0,85,86,3,20,10,0,86,87,6,2,-1,0,87,92,1,0,0,0,88,89,3,16,8,
        0,89,90,6,2,-1,0,90,92,1,0,0,0,91,67,1,0,0,0,91,70,1,0,0,0,91,73,
        1,0,0,0,91,76,1,0,0,0,91,79,1,0,0,0,91,82,1,0,0,0,91,85,1,0,0,0,
        91,88,1,0,0,0,92,5,1,0,0,0,93,94,3,40,20,0,94,95,5,5,0,0,95,96,5,
        38,0,0,96,97,5,6,0,0,97,98,3,42,21,0,98,7,1,0,0,0,99,109,3,40,20,
        0,100,101,3,22,11,0,101,102,6,4,-1,0,102,110,1,0,0,0,103,104,3,24,
        12,0,104,105,6,4,-1,0,105,110,1,0,0,0,106,107,3,26,13,0,107,108,
        6,4,-1,0,108,110,1,0,0,0,109,100,1,0,0,0,109,103,1,0,0,0,109,106,
        1,0,0,0,110,111,1,0,0,0,111,112,3,42,21,0,112,9,1,0,0,0,113,114,
        3,40,20,0,114,115,5,7,0,0,115,116,3,22,11,0,116,117,3,42,21,0,117,
        127,3,2,1,0,118,119,3,40,20,0,119,122,5,8,0,0,120,121,5,7,0,0,121,
        123,3,22,11,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,
        125,3,42,21,0,125,126,3,2,1,0,126,128,1,0,0,0,127,118,1,0,0,0,127,
        128,1,0,0,0,128,129,1,0,0,0,129,130,3,38,19,0,130,11,1,0,0,0,131,
        132,3,40,20,0,132,139,5,9,0,0,133,134,3,22,11,0,134,135,6,6,-1,0,
        135,140,1,0,0,0,136,137,3,24,12,0,137,138,6,6,-1,0,138,140,1,0,0,
        0,139,133,1,0,0,0,139,136,1,0,0,0,140,141,1,0,0,0,141,142,3,42,21,
        0,142,148,3,2,1,0,143,144,3,40,20,0,144,145,5,8,0,0,145,146,3,42,
        21,0,146,147,3,2,1,0,147,149,1,0,0,0,148,143,1,0,0,0,148,149,1,0,
        0,0,149,150,1,0,0,0,150,151,3,38,19,0,151,13,1,0,0,0,152,153,3,40,
        20,0,153,154,5,2,0,0,154,156,5,39,0,0,155,157,3,22,11,0,156,155,
        1,0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,159,3,42,21,0,159,15,
        1,0,0,0,160,161,3,40,20,0,161,162,5,24,0,0,162,163,5,39,0,0,163,
        164,3,42,21,0,164,17,1,0,0,0,165,166,3,40,20,0,166,167,5,3,0,0,167,
        169,5,41,0,0,168,170,3,22,11,0,169,168,1,0,0,0,169,170,1,0,0,0,170,
        171,1,0,0,0,171,172,3,42,21,0,172,19,1,0,0,0,173,174,3,40,20,0,174,
        175,5,4,0,0,175,176,3,22,11,0,176,177,3,42,21,0,177,183,3,2,1,0,
        178,179,3,40,20,0,179,180,5,8,0,0,180,181,3,42,21,0,181,182,3,2,
        1,0,182,184,1,0,0,0,183,178,1,0,0,0,183,184,1,0,0,0,184,185,1,0,
        0,0,185,186,3,38,19,0,186,21,1,0,0,0,187,192,3,28,14,0,188,189,5,
        10,0,0,189,191,3,28,14,0,190,188,1,0,0,0,191,194,1,0,0,0,192,190,
        1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,192,1,0,0,0,195,196,
        6,11,-1,0,196,204,1,0,0,0,197,198,3,36,18,0,198,199,6,11,-1,0,199,
        204,1,0,0,0,200,201,3,34,17,0,201,202,6,11,-1,0,202,204,1,0,0,0,
        203,187,1,0,0,0,203,197,1,0,0,0,203,200,1,0,0,0,204,23,1,0,0,0,205,
        208,3,30,15,0,206,207,5,11,0,0,207,209,3,30,15,0,208,206,1,0,0,0,
        208,209,1,0,0,0,209,210,1,0,0,0,210,211,5,12,0,0,211,212,3,22,11,
        0,212,25,1,0,0,0,213,214,3,30,15,0,214,215,5,13,0,0,215,216,3,22,
        11,0,216,27,1,0,0,0,217,218,5,14,0,0,218,238,6,14,-1,0,219,220,5,
        39,0,0,220,238,6,14,-1,0,221,222,5,40,0,0,222,238,6,14,-1,0,223,
        224,3,30,15,0,224,225,6,14,-1,0,225,238,1,0,0,0,226,227,3,32,16,
        0,227,228,6,14,-1,0,228,238,1,0,0,0,229,230,3,34,17,0,230,231,6,
        14,-1,0,231,238,1,0,0,0,232,233,5,15,0,0,233,234,3,28,14,0,234,235,
        5,16,0,0,235,236,6,14,-1,0,236,238,1,0,0,0,237,217,1,0,0,0,237,219,
        1,0,0,0,237,221,1,0,0,0,237,223,1,0,0,0,237,226,1,0,0,0,237,229,
        1,0,0,0,237,232,1,0,0,0,238,29,1,0,0,0,239,241,5,17,0,0,240,242,
        5,41,0,0,241,240,1,0,0,0,241,242,1,0,0,0,242,31,1,0,0,0,243,245,
        3,30,15,0,244,243,1,0,0,0,244,245,1,0,0,0,245,246,1,0,0,0,246,248,
        5,18,0,0,247,249,5,41,0,0,248,247,1,0,0,0,248,249,1,0,0,0,249,254,
        1,0,0,0,250,252,5,18,0,0,251,253,5,41,0,0,252,251,1,0,0,0,252,253,
        1,0,0,0,253,255,1,0,0,0,254,250,1,0,0,0,254,255,1,0,0,0,255,33,1,
        0,0,0,256,257,3,44,22,0,257,35,1,0,0,0,258,259,3,30,15,0,259,260,
        6,18,-1,0,260,265,1,0,0,0,261,262,3,32,16,0,262,263,6,18,-1,0,263,
        265,1,0,0,0,264,258,1,0,0,0,264,261,1,0,0,0,265,269,1,0,0,0,266,
        268,3,28,14,0,267,266,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,
        270,1,0,0,0,270,37,1,0,0,0,271,269,1,0,0,0,272,273,3,40,20,0,273,
        274,5,19,0,0,274,275,3,42,21,0,275,39,1,0,0,0,276,278,5,20,0,0,277,
        279,5,21,0,0,278,277,1,0,0,0,278,279,1,0,0,0,279,41,1,0,0,0,280,
        282,5,21,0,0,281,280,1,0,0,0,281,282,1,0,0,0,282,283,1,0,0,0,283,
        284,5,22,0,0,284,43,1,0,0,0,285,286,5,25,0,0,286,287,3,28,14,0,287,
        288,3,28,14,0,288,289,1,0,0,0,289,290,6,22,-1,0,290,375,1,0,0,0,
        291,292,5,35,0,0,292,296,3,28,14,0,293,295,3,28,14,0,294,293,1,0,
        0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,299,1,0,
        0,0,298,296,1,0,0,0,299,300,6,22,-1,0,300,375,1,0,0,0,301,302,5,
        36,0,0,302,306,3,28,14,0,303,305,3,28,14,0,304,303,1,0,0,0,305,308,
        1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,309,1,0,0,0,308,306,
        1,0,0,0,309,310,6,22,-1,0,310,375,1,0,0,0,311,312,5,32,0,0,312,313,
        3,28,14,0,313,314,6,22,-1,0,314,375,1,0,0,0,315,316,5,33,0,0,316,
        317,3,28,14,0,317,318,6,22,-1,0,318,375,1,0,0,0,319,320,5,34,0,0,
        320,321,3,28,14,0,321,322,3,28,14,0,322,323,6,22,-1,0,323,375,1,
        0,0,0,324,325,5,37,0,0,325,329,3,28,14,0,326,328,3,28,14,0,327,326,
        1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,1,0,0,0,330,332,
        1,0,0,0,331,329,1,0,0,0,332,333,6,22,-1,0,333,375,1,0,0,0,334,335,
        5,26,0,0,335,336,3,28,14,0,336,337,3,28,14,0,337,338,6,22,-1,0,338,
        375,1,0,0,0,339,340,5,29,0,0,340,341,3,28,14,0,341,342,3,28,14,0,
        342,343,6,22,-1,0,343,375,1,0,0,0,344,345,5,27,0,0,345,346,3,28,
        14,0,346,347,3,28,14,0,347,348,6,22,-1,0,348,375,1,0,0,0,349,350,
        5,28,0,0,350,351,3,28,14,0,351,352,3,28,14,0,352,353,6,22,-1,0,353,
        375,1,0,0,0,354,355,5,30,0,0,355,356,3,28,14,0,356,357,3,28,14,0,
        357,358,1,0,0,0,358,359,6,22,-1,0,359,375,1,0,0,0,360,361,5,31,0,
        0,361,362,3,28,14,0,362,363,3,28,14,0,363,364,6,22,-1,0,364,375,
        1,0,0,0,365,369,3,46,23,0,366,368,3,28,14,0,367,366,1,0,0,0,368,
        371,1,0,0,0,369,367,1,0,0,0,369,370,1,0,0,0,370,372,1,0,0,0,371,
        369,1,0,0,0,372,373,6,22,-1,0,373,375,1,0,0,0,374,285,1,0,0,0,374,
        291,1,0,0,0,374,301,1,0,0,0,374,311,1,0,0,0,374,315,1,0,0,0,374,
        319,1,0,0,0,374,324,1,0,0,0,374,334,1,0,0,0,374,339,1,0,0,0,374,
        344,1,0,0,0,374,349,1,0,0,0,374,354,1,0,0,0,374,360,1,0,0,0,374,
        365,1,0,0,0,375,45,1,0,0,0,376,377,5,41,0,0,377,47,1,0,0,0,30,55,
        62,64,91,109,122,127,139,148,156,169,183,192,203,208,237,241,244,
        248,252,254,264,269,278,281,296,306,329,369,374
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
                     "'slice'", "'printf'", "'Comment'" ]

    symbolicNames = [ "<INVALID>", "Text", "Template", "Block", "With", 
                      "CommentBegin", "CommentEnd", "If", "Else", "Range", 
                      "Pipe", "Comma", "Assignment", "Equal", "Nil", "LeftParenthesis", 
                      "RightParenthesis", "Dollar", "Dot", "End", "BlockStart", 
                      "Dash", "BlockEnd", "Constant", "Define", "And", "Eq", 
                      "Lt", "Le", "Ne", "Gt", "Ge", "Len", "Not", "Or", 
                      "Index", "Slice", "Printf", "AnyText", "StringConstant", 
                      "NumberConstant", "Name", "WS" ]

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
    RULE_globalFunctions = 22
    RULE_local = 23

    ruleNames =  [ "start", "template", "goaction", "commentaction", "pipelineaction", 
                   "ifaction", "rangeaction", "templateaction", "defineAction", 
                   "blockAction", "withAction", "pipeline", "vardeclarepipeline", 
                   "varassignpipeline", "argument", "variable", "fields", 
                   "funccall", "methodcall", "end", "ld", "rd", "globalFunctions", 
                   "local" ]

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
    AnyText=38
    StringConstant=39
    NumberConstant=40
    Name=41
    WS=42

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
        self.counter['globalFunctions'] = self.counter['globalFunctions'] if 'globalFunctions' in self.counter else {};



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
            self.state = 48
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

        def Text(self, i:int=None):
            if i is None:
                return self.getTokens(count_parser.Text)
            else:
                return self.getToken(count_parser.Text, i)

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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 50
                self.match(count_parser.Text)
                self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [20]:
                self.state = 52
                self.goaction()
                self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1
                pass
            else:
                raise NoViableAltException(self)

            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 57
                        self.match(count_parser.Text)
                        self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1
                        pass
                    elif token in [20]:
                        self.state = 59
                        self.goaction()
                        self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 66
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.commentaction()
                self.counter[inspect.stack()[0][3]]['commentaction'] = self.counter[inspect.stack()[0][3]]['commentaction'] + 1 if 'commentaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.pipelineaction()
                self.counter[inspect.stack()[0][3]]['pipelineaction'] = self.counter[inspect.stack()[0][3]]['pipelineaction'] + 1 if 'pipelineaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.ifaction()
                self.counter[inspect.stack()[0][3]]['ifaction'] = self.counter[inspect.stack()[0][3]]['ifaction'] + 1 if 'ifaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.rangeaction()
                self.counter[inspect.stack()[0][3]]['rangeaction'] = self.counter[inspect.stack()[0][3]]['rangeaction'] + 1 if 'rangeaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.templateaction()
                self.counter[inspect.stack()[0][3]]['templateaction'] = self.counter[inspect.stack()[0][3]]['templateaction'] + 1 if 'templateaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.blockAction()
                self.counter[inspect.stack()[0][3]]['blockAction'] = self.counter[inspect.stack()[0][3]]['blockAction'] + 1 if 'blockAction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 85
                self.withAction()
                self.counter[inspect.stack()[0][3]]['withAction'] = self.counter[inspect.stack()[0][3]]['withAction'] + 1 if 'withAction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 88
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
            self.state = 93
            self.ld()
            self.state = 94
            self.match(count_parser.CommentBegin)
            self.state = 95
            self.match(count_parser.AnyText)
            self.state = 96
            self.match(count_parser.CommentEnd)
            self.state = 97
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
            self.state = 99
            self.ld()
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 100
                self.pipeline()
                self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 103
                self.vardeclarepipeline()
                self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.state = 106
                self.varassignpipeline()
                self.counter[inspect.stack()[0][3]]['varassignpipeline'] = self.counter[inspect.stack()[0][3]]['varassignpipeline'] + 1 if 'varassignpipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 111
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
            self.state = 113
            self.ld()
            self.state = 114
            self.match(count_parser.If)
            self.state = 115
            self.pipeline()
            self.state = 116
            self.rd()
            self.state = 117
            self.template()
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 118
                self.ld()
                self.state = 119
                self.match(count_parser.Else)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 120
                    self.match(count_parser.If)
                    self.state = 121
                    self.pipeline()


                self.state = 124
                self.rd()
                self.state = 125
                self.template()


            self.state = 129
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
            self.state = 131
            self.ld()
            self.state = 132
            self.match(count_parser.Range)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 133
                self.pipeline()
                self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 136
                self.vardeclarepipeline()
                self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 141
            self.rd()
            self.state = 142
            self.template()
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 143
                self.ld()
                self.state = 144
                self.match(count_parser.Else)
                self.state = 145
                self.rd()
                self.state = 146
                self.template()


            self.state = 150
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
            self.state = 152
            self.ld()
            self.state = 153
            self.match(count_parser.Template)
            self.state = 154
            self.match(count_parser.StringConstant)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4123135492096) != 0):
                self.state = 155
                self.pipeline()


            self.state = 158
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
            self.state = 160
            self.ld()
            self.state = 161
            self.match(count_parser.Define)
            self.state = 162
            self.match(count_parser.StringConstant)
            self.state = 163
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
            self.state = 165
            self.ld()
            self.state = 166
            self.match(count_parser.Block)
            self.state = 167
            self.match(count_parser.Name)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4123135492096) != 0):
                self.state = 168
                self.pipeline()


            self.state = 171
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
            self.state = 173
            self.ld()
            self.state = 174
            self.match(count_parser.With)
            self.state = 175
            self.pipeline()
            self.state = 176
            self.rd()
            self.state = 177
            self.template()
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 178
                self.ld()
                self.state = 179
                self.match(count_parser.Else)
                self.state = 180
                self.rd()
                self.state = 181
                self.template()


            self.state = 185
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
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.argument()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 188
                    self.match(count_parser.Pipe)
                    self.state = 189
                    self.argument()
                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.counter[inspect.stack()[0][3]]['argument'] = self.counter[inspect.stack()[0][3]]['argument'] + 1 if 'argument' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.methodcall()
                self.counter[inspect.stack()[0][3]]['methodcall'] = self.counter[inspect.stack()[0][3]]['methodcall'] + 1 if 'methodcall' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
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
            self.state = 205
            self.variable()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 206
                self.match(count_parser.Comma)
                self.state = 207
                self.variable()


            self.state = 210
            self.match(count_parser.Assignment)
            self.state = 211
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
            self.state = 213
            self.variable()
            self.state = 214
            self.match(count_parser.Equal)
            self.state = 215
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
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(count_parser.Nil)
                self.counter[inspect.stack()[0][3]]['Nil'] = self.counter[inspect.stack()[0][3]]['Nil'] + 1 if 'Nil' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(count_parser.StringConstant)
                self.counter[inspect.stack()[0][3]]['StringConstant'] = self.counter[inspect.stack()[0][3]]['StringConstant'] + 1 if 'StringConstant' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(count_parser.NumberConstant)
                self.counter[inspect.stack()[0][3]]['NumberConstant'] = self.counter[inspect.stack()[0][3]]['NumberConstant'] + 1 if 'NumberConstant' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.variable()
                self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 226
                self.fields()
                self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 229
                self.funccall()
                self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 232
                self.match(count_parser.LeftParenthesis)
                self.state = 233
                self.argument()
                self.state = 234
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(count_parser.Dollar)
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 240
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
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 243
                self.variable()


            self.state = 246
            self.match(count_parser.Dot)
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 247
                self.match(count_parser.Name)


            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 250
                self.match(count_parser.Dot)
                self.state = 252
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 251
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

        def globalFunctions(self):
            return self.getTypedRuleContext(count_parser.GlobalFunctionsContext,0)


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
            self.state = 256
            self.globalFunctions()
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
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 258
                self.variable()
                self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 261
                self.fields()
                self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4123135492096) != 0):
                self.state = 266
                self.argument()
                self.state = 271
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
            self.state = 272
            self.ld()
            self.state = 273
            self.match(count_parser.End)
            self.state = 274
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
            self.state = 276
            self.match(count_parser.BlockStart)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 277
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
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 280
                self.match(count_parser.Dash)


            self.state = 283
            self.match(count_parser.BlockEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalFunctionsContext(ParserRuleContext):
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

        def local(self):
            return self.getTypedRuleContext(count_parser.LocalContext,0)


        def getRuleIndex(self):
            return count_parser.RULE_globalFunctions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalFunctions" ):
                listener.enterGlobalFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalFunctions" ):
                listener.exitGlobalFunctions(self)




    def globalFunctions(self):

        localctx = count_parser.GlobalFunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_globalFunctions)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(count_parser.And)
                self.state = 286
                self.argument()
                self.state = 287
                self.argument()
                self.counter[inspect.stack()[0][3]]['And'] = self.counter[inspect.stack()[0][3]]['And'] + 1 if 'And' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(count_parser.Index)
                self.state = 292
                self.argument()
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 293
                        self.argument() 
                    self.state = 298
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                self.counter[inspect.stack()[0][3]]['Index'] = self.counter[inspect.stack()[0][3]]['Index'] + 1 if 'Index' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.match(count_parser.Slice)
                self.state = 302
                self.argument()
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 303
                        self.argument() 
                    self.state = 308
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.counter[inspect.stack()[0][3]]['Slice'] = self.counter[inspect.stack()[0][3]]['Slice'] + 1 if 'Slice' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 311
                self.match(count_parser.Len)
                self.state = 312
                self.argument()
                self.counter[inspect.stack()[0][3]]['Len'] = self.counter[inspect.stack()[0][3]]['Len'] + 1 if 'Len' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 315
                self.match(count_parser.Not)
                self.state = 316
                self.argument()
                self.counter[inspect.stack()[0][3]]['Len'] = self.counter[inspect.stack()[0][3]]['Len'] + 1 if 'Len' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 319
                self.match(count_parser.Or)
                self.state = 320
                self.argument()
                self.state = 321
                self.argument()
                self.counter[inspect.stack()[0][3]]['Or'] = self.counter[inspect.stack()[0][3]]['Or'] + 1 if 'Or' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 7)
                self.state = 324
                self.match(count_parser.Printf)
                self.state = 325
                self.argument()
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 326
                        self.argument() 
                    self.state = 331
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.counter[inspect.stack()[0][3]]['Printf'] = self.counter[inspect.stack()[0][3]]['Printf'] + 1 if 'Printf' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 8)
                self.state = 334
                self.match(count_parser.Eq)
                self.state = 335
                self.argument()
                self.state = 336
                self.argument()
                self.counter[inspect.stack()[0][3]]['Eq'] = self.counter[inspect.stack()[0][3]]['Eq'] + 1 if 'Eq' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 9)
                self.state = 339
                self.match(count_parser.Ne)
                self.state = 340
                self.argument()
                self.state = 341
                self.argument()
                self.counter[inspect.stack()[0][3]]['Ne'] = self.counter[inspect.stack()[0][3]]['Ne'] + 1 if 'Ne' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 10)
                self.state = 344
                self.match(count_parser.Lt)
                self.state = 345
                self.argument()
                self.state = 346
                self.argument()
                self.counter[inspect.stack()[0][3]]['Lt'] = self.counter[inspect.stack()[0][3]]['Lt'] + 1 if 'Lt' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 11)
                self.state = 349
                self.match(count_parser.Le)
                self.state = 350
                self.argument()
                self.state = 351
                self.argument()
                self.counter[inspect.stack()[0][3]]['Le'] = self.counter[inspect.stack()[0][3]]['Le'] + 1 if 'Le' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 12)
                self.state = 354
                self.match(count_parser.Gt)
                self.state = 355
                self.argument()
                self.state = 356
                self.argument()
                self.counter[inspect.stack()[0][3]]['Gt'] = self.counter[inspect.stack()[0][3]]['Gt'] + 1 if 'Gt' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 13)
                self.state = 360
                self.match(count_parser.Ge)
                self.state = 361
                self.argument()
                self.state = 362
                self.argument()
                self.counter[inspect.stack()[0][3]]['Ge'] = self.counter[inspect.stack()[0][3]]['Ge'] + 1 if 'Ge' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 14)
                self.state = 365
                self.local()
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 366
                        self.argument() 
                    self.state = 371
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                self.counter[inspect.stack()[0][3]]['local'] = self.counter[inspect.stack()[0][3]]['local'] + 1 if 'local' in self.counter[inspect.stack()[0][3]] else 1
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
        self.enterRule(localctx, 46, self.RULE_local)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(count_parser.Name)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





