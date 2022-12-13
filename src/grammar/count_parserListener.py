# Generated from count_parser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .count_parser import count_parser
else:
    from count_parser import count_parser

import inspect
import json
import os

if not os.path.exists('counter.json'):
    with open('counter.json', 'w+') as file:
        file.write('{}')



# This class defines a complete listener for a parse tree produced by count_parser.
class count_parserListener(ParseTreeListener):

    # Enter a parse tree produced by count_parser#start.
    def enterStart(self, ctx:count_parser.StartContext):
        pass

    # Exit a parse tree produced by count_parser#start.
    def exitStart(self, ctx:count_parser.StartContext):
        pass


    # Enter a parse tree produced by count_parser#template.
    def enterTemplate(self, ctx:count_parser.TemplateContext):
        pass

    # Exit a parse tree produced by count_parser#template.
    def exitTemplate(self, ctx:count_parser.TemplateContext):
        pass


    # Enter a parse tree produced by count_parser#goaction.
    def enterGoaction(self, ctx:count_parser.GoactionContext):
        pass

    # Exit a parse tree produced by count_parser#goaction.
    def exitGoaction(self, ctx:count_parser.GoactionContext):
        pass


    # Enter a parse tree produced by count_parser#commentaction.
    def enterCommentaction(self, ctx:count_parser.CommentactionContext):
        pass

    # Exit a parse tree produced by count_parser#commentaction.
    def exitCommentaction(self, ctx:count_parser.CommentactionContext):
        pass


    # Enter a parse tree produced by count_parser#pipelineaction.
    def enterPipelineaction(self, ctx:count_parser.PipelineactionContext):
        pass

    # Exit a parse tree produced by count_parser#pipelineaction.
    def exitPipelineaction(self, ctx:count_parser.PipelineactionContext):
        pass


    # Enter a parse tree produced by count_parser#ifaction.
    def enterIfaction(self, ctx:count_parser.IfactionContext):
        pass

    # Exit a parse tree produced by count_parser#ifaction.
    def exitIfaction(self, ctx:count_parser.IfactionContext):
        pass


    # Enter a parse tree produced by count_parser#rangeaction.
    def enterRangeaction(self, ctx:count_parser.RangeactionContext):
        pass

    # Exit a parse tree produced by count_parser#rangeaction.
    def exitRangeaction(self, ctx:count_parser.RangeactionContext):
        pass


    # Enter a parse tree produced by count_parser#templateaction.
    def enterTemplateaction(self, ctx:count_parser.TemplateactionContext):
        pass

    # Exit a parse tree produced by count_parser#templateaction.
    def exitTemplateaction(self, ctx:count_parser.TemplateactionContext):
        pass


    # Enter a parse tree produced by count_parser#blockAction.
    def enterBlockAction(self, ctx:count_parser.BlockActionContext):
        pass

    # Exit a parse tree produced by count_parser#blockAction.
    def exitBlockAction(self, ctx:count_parser.BlockActionContext):
        pass


    # Enter a parse tree produced by count_parser#withAction.
    def enterWithAction(self, ctx:count_parser.WithActionContext):
        pass

    # Exit a parse tree produced by count_parser#withAction.
    def exitWithAction(self, ctx:count_parser.WithActionContext):
        pass


    # Enter a parse tree produced by count_parser#pipeline.
    def enterPipeline(self, ctx:count_parser.PipelineContext):
        pass

    # Exit a parse tree produced by count_parser#pipeline.
    def exitPipeline(self, ctx:count_parser.PipelineContext):
        pass


    # Enter a parse tree produced by count_parser#vardeclarepipeline.
    def enterVardeclarepipeline(self, ctx:count_parser.VardeclarepipelineContext):
        pass

    # Exit a parse tree produced by count_parser#vardeclarepipeline.
    def exitVardeclarepipeline(self, ctx:count_parser.VardeclarepipelineContext):
        pass


    # Enter a parse tree produced by count_parser#varassignpipeline.
    def enterVarassignpipeline(self, ctx:count_parser.VarassignpipelineContext):
        pass

    # Exit a parse tree produced by count_parser#varassignpipeline.
    def exitVarassignpipeline(self, ctx:count_parser.VarassignpipelineContext):
        pass


    # Enter a parse tree produced by count_parser#argument.
    def enterArgument(self, ctx:count_parser.ArgumentContext):
        pass

    # Exit a parse tree produced by count_parser#argument.
    def exitArgument(self, ctx:count_parser.ArgumentContext):
        pass


    # Enter a parse tree produced by count_parser#variable.
    def enterVariable(self, ctx:count_parser.VariableContext):
        pass

    # Exit a parse tree produced by count_parser#variable.
    def exitVariable(self, ctx:count_parser.VariableContext):
        pass


    # Enter a parse tree produced by count_parser#fields.
    def enterFields(self, ctx:count_parser.FieldsContext):
        pass

    # Exit a parse tree produced by count_parser#fields.
    def exitFields(self, ctx:count_parser.FieldsContext):
        pass


    # Enter a parse tree produced by count_parser#funccall.
    def enterFunccall(self, ctx:count_parser.FunccallContext):
        pass

    # Exit a parse tree produced by count_parser#funccall.
    def exitFunccall(self, ctx:count_parser.FunccallContext):
        pass


    # Enter a parse tree produced by count_parser#methodcall.
    def enterMethodcall(self, ctx:count_parser.MethodcallContext):
        pass

    # Exit a parse tree produced by count_parser#methodcall.
    def exitMethodcall(self, ctx:count_parser.MethodcallContext):
        pass


    # Enter a parse tree produced by count_parser#end.
    def enterEnd(self, ctx:count_parser.EndContext):
        pass

    # Exit a parse tree produced by count_parser#end.
    def exitEnd(self, ctx:count_parser.EndContext):
        pass


    # Enter a parse tree produced by count_parser#ld.
    def enterLd(self, ctx:count_parser.LdContext):
        pass

    # Exit a parse tree produced by count_parser#ld.
    def exitLd(self, ctx:count_parser.LdContext):
        pass


    # Enter a parse tree produced by count_parser#rd.
    def enterRd(self, ctx:count_parser.RdContext):
        pass

    # Exit a parse tree produced by count_parser#rd.
    def exitRd(self, ctx:count_parser.RdContext):
        pass


    # Enter a parse tree produced by count_parser#name.
    def enterName(self, ctx:count_parser.NameContext):
        pass

    # Exit a parse tree produced by count_parser#name.
    def exitName(self, ctx:count_parser.NameContext):
        pass



del count_parser