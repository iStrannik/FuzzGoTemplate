# Generated from count_parser.g4 by ANTLR 4.11.1
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
        4,1,26,292,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,1,1,1,1,
        1,1,1,1,1,5,1,59,8,1,10,1,12,1,62,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,85,
        8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,103,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        116,8,5,1,5,1,5,1,5,3,5,121,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,133,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,142,8,6,1,6,
        1,6,1,7,1,7,1,7,1,7,3,7,150,8,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,158,
        8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,172,8,9,
        1,9,1,9,1,10,1,10,1,10,5,10,179,8,10,10,10,12,10,182,9,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,5,10,191,8,10,10,10,12,10,194,9,10,1,
        10,1,10,1,10,3,10,199,8,10,1,11,1,11,1,11,3,11,204,8,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,230,8,13,1,13,
        1,13,3,13,234,8,13,1,14,1,14,3,14,238,8,14,1,15,3,15,241,8,15,1,
        15,1,15,3,15,245,8,15,1,15,1,15,3,15,249,8,15,3,15,251,8,15,1,16,
        1,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,261,8,17,1,17,5,17,264,8,
        17,10,17,12,17,267,9,17,1,18,1,18,1,18,1,18,1,19,1,19,3,19,275,8,
        19,1,20,3,20,278,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,5,21,287,
        8,21,10,21,12,21,290,9,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,0,0,309,0,44,1,0,0,0,2,51,1,0,0,
        0,4,84,1,0,0,0,6,86,1,0,0,0,8,92,1,0,0,0,10,106,1,0,0,0,12,124,1,
        0,0,0,14,145,1,0,0,0,16,153,1,0,0,0,18,161,1,0,0,0,20,198,1,0,0,
        0,22,200,1,0,0,0,24,208,1,0,0,0,26,233,1,0,0,0,28,235,1,0,0,0,30,
        240,1,0,0,0,32,252,1,0,0,0,34,260,1,0,0,0,36,268,1,0,0,0,38,272,
        1,0,0,0,40,277,1,0,0,0,42,281,1,0,0,0,44,45,3,2,1,0,45,1,1,0,0,0,
        46,47,5,1,0,0,47,52,6,1,-1,0,48,49,3,4,2,0,49,50,6,1,-1,0,50,52,
        1,0,0,0,51,46,1,0,0,0,51,48,1,0,0,0,52,60,1,0,0,0,53,54,5,1,0,0,
        54,59,6,1,-1,0,55,56,3,4,2,0,56,57,6,1,-1,0,57,59,1,0,0,0,58,53,
        1,0,0,0,58,55,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,
        61,3,1,0,0,0,62,60,1,0,0,0,63,64,3,6,3,0,64,65,6,2,-1,0,65,85,1,
        0,0,0,66,67,3,8,4,0,67,68,6,2,-1,0,68,85,1,0,0,0,69,70,3,10,5,0,
        70,71,6,2,-1,0,71,85,1,0,0,0,72,73,3,12,6,0,73,74,6,2,-1,0,74,85,
        1,0,0,0,75,76,3,14,7,0,76,77,6,2,-1,0,77,85,1,0,0,0,78,79,3,16,8,
        0,79,80,6,2,-1,0,80,85,1,0,0,0,81,82,3,18,9,0,82,83,6,2,-1,0,83,
        85,1,0,0,0,84,63,1,0,0,0,84,66,1,0,0,0,84,69,1,0,0,0,84,72,1,0,0,
        0,84,75,1,0,0,0,84,78,1,0,0,0,84,81,1,0,0,0,85,5,1,0,0,0,86,87,3,
        38,19,0,87,88,5,5,0,0,88,89,5,1,0,0,89,90,5,6,0,0,90,91,3,40,20,
        0,91,7,1,0,0,0,92,102,3,38,19,0,93,94,3,20,10,0,94,95,6,4,-1,0,95,
        103,1,0,0,0,96,97,3,22,11,0,97,98,6,4,-1,0,98,103,1,0,0,0,99,100,
        3,24,12,0,100,101,6,4,-1,0,101,103,1,0,0,0,102,93,1,0,0,0,102,96,
        1,0,0,0,102,99,1,0,0,0,103,104,1,0,0,0,104,105,3,40,20,0,105,9,1,
        0,0,0,106,107,3,38,19,0,107,108,5,7,0,0,108,109,3,20,10,0,109,110,
        3,40,20,0,110,120,3,2,1,0,111,112,3,38,19,0,112,115,5,8,0,0,113,
        114,5,7,0,0,114,116,3,20,10,0,115,113,1,0,0,0,115,116,1,0,0,0,116,
        117,1,0,0,0,117,118,3,40,20,0,118,119,3,2,1,0,119,121,1,0,0,0,120,
        111,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,3,36,18,0,123,
        11,1,0,0,0,124,125,3,38,19,0,125,132,5,9,0,0,126,127,3,20,10,0,127,
        128,6,6,-1,0,128,133,1,0,0,0,129,130,3,22,11,0,130,131,6,6,-1,0,
        131,133,1,0,0,0,132,126,1,0,0,0,132,129,1,0,0,0,133,134,1,0,0,0,
        134,135,3,40,20,0,135,141,3,2,1,0,136,137,3,38,19,0,137,138,5,8,
        0,0,138,139,3,40,20,0,139,140,3,2,1,0,140,142,1,0,0,0,141,136,1,
        0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,144,3,36,18,0,144,13,1,
        0,0,0,145,146,3,38,19,0,146,147,5,2,0,0,147,149,3,42,21,0,148,150,
        3,20,10,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,
        3,40,20,0,152,15,1,0,0,0,153,154,3,38,19,0,154,155,5,3,0,0,155,157,
        3,42,21,0,156,158,3,20,10,0,157,156,1,0,0,0,157,158,1,0,0,0,158,
        159,1,0,0,0,159,160,3,40,20,0,160,17,1,0,0,0,161,162,3,38,19,0,162,
        163,5,4,0,0,163,164,3,20,10,0,164,165,3,40,20,0,165,171,3,2,1,0,
        166,167,3,38,19,0,167,168,5,8,0,0,168,169,3,40,20,0,169,170,3,2,
        1,0,170,172,1,0,0,0,171,166,1,0,0,0,171,172,1,0,0,0,172,173,1,0,
        0,0,173,174,3,36,18,0,174,19,1,0,0,0,175,180,3,26,13,0,176,177,5,
        10,0,0,177,179,3,26,13,0,178,176,1,0,0,0,179,182,1,0,0,0,180,178,
        1,0,0,0,180,181,1,0,0,0,181,183,1,0,0,0,182,180,1,0,0,0,183,184,
        6,10,-1,0,184,199,1,0,0,0,185,186,3,34,17,0,186,187,6,10,-1,0,187,
        199,1,0,0,0,188,192,3,32,16,0,189,191,3,26,13,0,190,189,1,0,0,0,
        191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,
        194,192,1,0,0,0,195,196,3,34,17,0,196,197,6,10,-1,0,197,199,1,0,
        0,0,198,175,1,0,0,0,198,185,1,0,0,0,198,188,1,0,0,0,199,21,1,0,0,
        0,200,203,3,28,14,0,201,202,5,11,0,0,202,204,3,28,14,0,203,201,1,
        0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,5,12,0,0,206,207,3,
        20,10,0,207,23,1,0,0,0,208,209,3,28,14,0,209,210,5,13,0,0,210,211,
        3,20,10,0,211,25,1,0,0,0,212,213,5,23,0,0,213,234,6,13,-1,0,214,
        215,5,14,0,0,215,234,6,13,-1,0,216,217,3,28,14,0,217,218,6,13,-1,
        0,218,234,1,0,0,0,219,220,3,30,15,0,220,221,6,13,-1,0,221,234,1,
        0,0,0,222,223,3,32,16,0,223,224,6,13,-1,0,224,234,1,0,0,0,225,226,
        5,15,0,0,226,227,3,26,13,0,227,229,5,16,0,0,228,230,3,30,15,0,229,
        228,1,0,0,0,229,230,1,0,0,0,230,231,1,0,0,0,231,232,6,13,-1,0,232,
        234,1,0,0,0,233,212,1,0,0,0,233,214,1,0,0,0,233,216,1,0,0,0,233,
        219,1,0,0,0,233,222,1,0,0,0,233,225,1,0,0,0,234,27,1,0,0,0,235,237,
        5,17,0,0,236,238,3,42,21,0,237,236,1,0,0,0,237,238,1,0,0,0,238,29,
        1,0,0,0,239,241,3,28,14,0,240,239,1,0,0,0,240,241,1,0,0,0,241,242,
        1,0,0,0,242,244,5,18,0,0,243,245,3,42,21,0,244,243,1,0,0,0,244,245,
        1,0,0,0,245,250,1,0,0,0,246,248,5,18,0,0,247,249,3,42,21,0,248,247,
        1,0,0,0,248,249,1,0,0,0,249,251,1,0,0,0,250,246,1,0,0,0,250,251,
        1,0,0,0,251,31,1,0,0,0,252,253,3,42,21,0,253,33,1,0,0,0,254,255,
        3,28,14,0,255,256,6,17,-1,0,256,261,1,0,0,0,257,258,3,30,15,0,258,
        259,6,17,-1,0,259,261,1,0,0,0,260,254,1,0,0,0,260,257,1,0,0,0,261,
        265,1,0,0,0,262,264,3,26,13,0,263,262,1,0,0,0,264,267,1,0,0,0,265,
        263,1,0,0,0,265,266,1,0,0,0,266,35,1,0,0,0,267,265,1,0,0,0,268,269,
        3,38,19,0,269,270,5,19,0,0,270,271,3,40,20,0,271,37,1,0,0,0,272,
        274,5,20,0,0,273,275,5,21,0,0,274,273,1,0,0,0,274,275,1,0,0,0,275,
        39,1,0,0,0,276,278,5,21,0,0,277,276,1,0,0,0,277,278,1,0,0,0,278,
        279,1,0,0,0,279,280,5,22,0,0,280,41,1,0,0,0,281,288,5,24,0,0,282,
        283,5,24,0,0,283,287,6,21,-1,0,284,285,5,25,0,0,285,287,6,21,-1,
        0,286,282,1,0,0,0,286,284,1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,
        0,288,289,1,0,0,0,289,43,1,0,0,0,290,288,1,0,0,0,29,51,58,60,84,
        102,115,120,132,141,149,157,171,180,192,198,203,229,233,237,240,
        244,248,250,260,265,274,277,286,288
    ]

class count_parser ( Parser ):

    grammarFileName = "count_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TEXT'", "'template'", "'block'", "'with'", 
                     "'/*'", "'*/'", "'if'", "'else'", "'range'", "'|'", 
                     "','", "':='", "'='", "'nil'", "'('", "')'", "'$'", 
                     "'.'", "'end'", "'{{'", "'-'", "'}}'", "'CONSTANT'" ]

    symbolicNames = [ "<INVALID>", "Text", "Template", "Block", "With", 
                      "CommentBegin", "CommentEnd", "If", "Else", "Range", 
                      "Pipe", "Comma", "Assignment", "Equal", "Nil", "LeftParenthesis", 
                      "RightParenthesis", "Dollar", "Dot", "End", "BlockStart", 
                      "Dash", "BlockEnd", "Constant", "Letter", "Digit", 
                      "WS" ]

    RULE_start = 0
    RULE_template = 1
    RULE_goaction = 2
    RULE_commentaction = 3
    RULE_pipelineaction = 4
    RULE_ifaction = 5
    RULE_rangeaction = 6
    RULE_templateaction = 7
    RULE_blockAction = 8
    RULE_withAction = 9
    RULE_pipeline = 10
    RULE_vardeclarepipeline = 11
    RULE_varassignpipeline = 12
    RULE_argument = 13
    RULE_variable = 14
    RULE_fields = 15
    RULE_funccall = 16
    RULE_methodcall = 17
    RULE_end = 18
    RULE_ld = 19
    RULE_rd = 20
    RULE_name = 21

    ruleNames =  [ "start", "template", "goaction", "commentaction", "pipelineaction", 
                   "ifaction", "rangeaction", "templateaction", "blockAction", 
                   "withAction", "pipeline", "vardeclarepipeline", "varassignpipeline", 
                   "argument", "variable", "fields", "funccall", "methodcall", 
                   "end", "ld", "rd", "name" ]

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
    Letter=24
    Digit=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
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
        self.counter['name'] = self.counter['name'] if 'name' in self.counter else {};



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
            self.state = 44
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 46
                self.match(count_parser.Text)
                self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1
                pass
            elif token in [20]:
                self.state = 48
                self.goaction()
                self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1
                pass
            else:
                raise NoViableAltException(self)

            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 58
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 53
                        self.match(count_parser.Text)
                        self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1
                        pass
                    elif token in [20]:
                        self.state = 55
                        self.goaction()
                        self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 62
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
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.commentaction()
                self.counter[inspect.stack()[0][3]]['commentaction'] = self.counter[inspect.stack()[0][3]]['commentaction'] + 1 if 'commentaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.pipelineaction()
                self.counter[inspect.stack()[0][3]]['pipelineaction'] = self.counter[inspect.stack()[0][3]]['pipelineaction'] + 1 if 'pipelineaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.ifaction()
                self.counter[inspect.stack()[0][3]]['ifaction'] = self.counter[inspect.stack()[0][3]]['ifaction'] + 1 if 'ifaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.rangeaction()
                self.counter[inspect.stack()[0][3]]['rangeaction'] = self.counter[inspect.stack()[0][3]]['rangeaction'] + 1 if 'rangeaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.templateaction()
                self.counter[inspect.stack()[0][3]]['templateaction'] = self.counter[inspect.stack()[0][3]]['templateaction'] + 1 if 'templateaction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.blockAction()
                self.counter[inspect.stack()[0][3]]['blockAction'] = self.counter[inspect.stack()[0][3]]['blockAction'] + 1 if 'blockAction' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.withAction()
                self.counter[inspect.stack()[0][3]]['withAction'] = self.counter[inspect.stack()[0][3]]['withAction'] + 1 if 'withAction' in self.counter[inspect.stack()[0][3]] else 1
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

        def Text(self):
            return self.getToken(count_parser.Text, 0)

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
            self.state = 86
            self.ld()
            self.state = 87
            self.match(count_parser.CommentBegin)
            self.state = 88
            self.match(count_parser.Text)
            self.state = 89
            self.match(count_parser.CommentEnd)
            self.state = 90
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
            self.state = 92
            self.ld()
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 93
                self.pipeline()
                self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 96
                self.vardeclarepipeline()
                self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.state = 99
                self.varassignpipeline()
                self.counter[inspect.stack()[0][3]]['varassignpipeline'] = self.counter[inspect.stack()[0][3]]['varassignpipeline'] + 1 if 'varassignpipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 104
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
            self.state = 106
            self.ld()
            self.state = 107
            self.match(count_parser.If)
            self.state = 108
            self.pipeline()
            self.state = 109
            self.rd()
            self.state = 110
            self.template()
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 111
                self.ld()
                self.state = 112
                self.match(count_parser.Else)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 113
                    self.match(count_parser.If)
                    self.state = 114
                    self.pipeline()


                self.state = 117
                self.rd()
                self.state = 118
                self.template()


            self.state = 122
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
            self.state = 124
            self.ld()
            self.state = 125
            self.match(count_parser.Range)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 126
                self.pipeline()
                self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 129
                self.vardeclarepipeline()
                self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 134
            self.rd()
            self.state = 135
            self.template()
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 136
                self.ld()
                self.state = 137
                self.match(count_parser.Else)
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


    class TemplateactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ld(self):
            return self.getTypedRuleContext(count_parser.LdContext,0)


        def Template(self):
            return self.getToken(count_parser.Template, 0)

        def name(self):
            return self.getTypedRuleContext(count_parser.NameContext,0)


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
            self.state = 145
            self.ld()
            self.state = 146
            self.match(count_parser.Template)
            self.state = 147
            self.name()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 25608192) != 0:
                self.state = 148
                self.pipeline()


            self.state = 151
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

        def name(self):
            return self.getTypedRuleContext(count_parser.NameContext,0)


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
        self.enterRule(localctx, 16, self.RULE_blockAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.ld()
            self.state = 154
            self.match(count_parser.Block)
            self.state = 155
            self.name()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 25608192) != 0:
                self.state = 156
                self.pipeline()


            self.state = 159
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
        self.enterRule(localctx, 18, self.RULE_withAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.ld()
            self.state = 162
            self.match(count_parser.With)
            self.state = 163
            self.pipeline()
            self.state = 164
            self.rd()
            self.state = 165
            self.template()
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 166
                self.ld()
                self.state = 167
                self.match(count_parser.Else)
                self.state = 168
                self.rd()
                self.state = 169
                self.template()


            self.state = 173
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
        self.enterRule(localctx, 20, self.RULE_pipeline)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.argument()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 176
                    self.match(count_parser.Pipe)
                    self.state = 177
                    self.argument()
                    self.state = 182
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.counter[inspect.stack()[0][3]]['argument'] = self.counter[inspect.stack()[0][3]]['argument'] + 1 if 'argument' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.methodcall()
                self.counter[inspect.stack()[0][3]]['methodcall'] = self.counter[inspect.stack()[0][3]]['methodcall'] + 1 if 'methodcall' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.funccall()
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 189
                        self.argument() 
                    self.state = 194
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                self.state = 195
                self.methodcall()
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
        self.enterRule(localctx, 22, self.RULE_vardeclarepipeline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.variable()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 201
                self.match(count_parser.Comma)
                self.state = 202
                self.variable()


            self.state = 205
            self.match(count_parser.Assignment)
            self.state = 206
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
        self.enterRule(localctx, 24, self.RULE_varassignpipeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.variable()
            self.state = 209
            self.match(count_parser.Equal)
            self.state = 210
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

        def Constant(self):
            return self.getToken(count_parser.Constant, 0)

        def Nil(self):
            return self.getToken(count_parser.Nil, 0)

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
        self.enterRule(localctx, 26, self.RULE_argument)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(count_parser.Constant)
                self.counter[inspect.stack()[0][3]]['Constant'] = self.counter[inspect.stack()[0][3]]['Constant'] + 1 if 'Constant' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(count_parser.Nil)
                self.counter[inspect.stack()[0][3]]['Nil'] = self.counter[inspect.stack()[0][3]]['Nil'] + 1 if 'Nil' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.variable()
                self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.fields()
                self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.funccall()
                self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 225
                self.match(count_parser.LeftParenthesis)
                self.state = 226
                self.argument()
                self.state = 227
                self.match(count_parser.RightParenthesis)
                self.state = 229
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 228
                    self.fields()


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

        def name(self):
            return self.getTypedRuleContext(count_parser.NameContext,0)


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
        self.enterRule(localctx, 28, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(count_parser.Dollar)
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 236
                self.name()


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


        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(count_parser.NameContext)
            else:
                return self.getTypedRuleContext(count_parser.NameContext,i)


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
        self.enterRule(localctx, 30, self.RULE_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 239
                self.variable()


            self.state = 242
            self.match(count_parser.Dot)
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 243
                self.name()


            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 246
                self.match(count_parser.Dot)
                self.state = 248
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 247
                    self.name()




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

        def name(self):
            return self.getTypedRuleContext(count_parser.NameContext,0)


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
        self.enterRule(localctx, 32, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.name()
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
        self.enterRule(localctx, 34, self.RULE_methodcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 254
                self.variable()
                self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1
                pass

            elif la_ == 2:
                self.state = 257
                self.fields()
                self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1
                pass


            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 25608192) != 0:
                self.state = 262
                self.argument()
                self.state = 267
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
        self.enterRule(localctx, 36, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.ld()
            self.state = 269
            self.match(count_parser.End)
            self.state = 270
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
        self.enterRule(localctx, 38, self.RULE_ld)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(count_parser.BlockStart)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 273
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
        self.enterRule(localctx, 40, self.RULE_rd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 276
                self.match(count_parser.Dash)


            self.state = 279
            self.match(count_parser.BlockEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Letter(self, i:int=None):
            if i is None:
                return self.getTokens(count_parser.Letter)
            else:
                return self.getToken(count_parser.Letter, i)

        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(count_parser.Digit)
            else:
                return self.getToken(count_parser.Digit, i)

        def getRuleIndex(self):
            return count_parser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = count_parser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(count_parser.Letter)
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 286
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [24]:
                        self.state = 282
                        self.match(count_parser.Letter)
                        self.counter[inspect.stack()[0][3]]['Letter'] = self.counter[inspect.stack()[0][3]]['Letter'] + 1 if 'Letter' in self.counter[inspect.stack()[0][3]] else 1
                        pass
                    elif token in [25]:
                        self.state = 284
                        self.match(count_parser.Digit)
                        self.counter[inspect.stack()[0][3]]['Digit'] = self.counter[inspect.stack()[0][3]]['Digit'] + 1 if 'Digit' in self.counter[inspect.stack()[0][3]] else 1
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





