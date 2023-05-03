// Generated from count_parser.g4 by ANTLR 4.12.0

import inspect
import json
import os

if not os.path.exists('counter.json'):
    with open('counter.json', 'w+') as file:
        file.write('{}')


import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link count_parser}.
 */
public interface count_parserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link count_parser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(count_parser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(count_parser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#template}.
	 * @param ctx the parse tree
	 */
	void enterTemplate(count_parser.TemplateContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#template}.
	 * @param ctx the parse tree
	 */
	void exitTemplate(count_parser.TemplateContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#goaction}.
	 * @param ctx the parse tree
	 */
	void enterGoaction(count_parser.GoactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#goaction}.
	 * @param ctx the parse tree
	 */
	void exitGoaction(count_parser.GoactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#commentaction}.
	 * @param ctx the parse tree
	 */
	void enterCommentaction(count_parser.CommentactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#commentaction}.
	 * @param ctx the parse tree
	 */
	void exitCommentaction(count_parser.CommentactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#pipelineaction}.
	 * @param ctx the parse tree
	 */
	void enterPipelineaction(count_parser.PipelineactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#pipelineaction}.
	 * @param ctx the parse tree
	 */
	void exitPipelineaction(count_parser.PipelineactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#ifaction}.
	 * @param ctx the parse tree
	 */
	void enterIfaction(count_parser.IfactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#ifaction}.
	 * @param ctx the parse tree
	 */
	void exitIfaction(count_parser.IfactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#rangeaction}.
	 * @param ctx the parse tree
	 */
	void enterRangeaction(count_parser.RangeactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#rangeaction}.
	 * @param ctx the parse tree
	 */
	void exitRangeaction(count_parser.RangeactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#templateaction}.
	 * @param ctx the parse tree
	 */
	void enterTemplateaction(count_parser.TemplateactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#templateaction}.
	 * @param ctx the parse tree
	 */
	void exitTemplateaction(count_parser.TemplateactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#defineAction}.
	 * @param ctx the parse tree
	 */
	void enterDefineAction(count_parser.DefineActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#defineAction}.
	 * @param ctx the parse tree
	 */
	void exitDefineAction(count_parser.DefineActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#blockAction}.
	 * @param ctx the parse tree
	 */
	void enterBlockAction(count_parser.BlockActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#blockAction}.
	 * @param ctx the parse tree
	 */
	void exitBlockAction(count_parser.BlockActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#withAction}.
	 * @param ctx the parse tree
	 */
	void enterWithAction(count_parser.WithActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#withAction}.
	 * @param ctx the parse tree
	 */
	void exitWithAction(count_parser.WithActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#pipeline}.
	 * @param ctx the parse tree
	 */
	void enterPipeline(count_parser.PipelineContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#pipeline}.
	 * @param ctx the parse tree
	 */
	void exitPipeline(count_parser.PipelineContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#vardeclarepipeline}.
	 * @param ctx the parse tree
	 */
	void enterVardeclarepipeline(count_parser.VardeclarepipelineContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#vardeclarepipeline}.
	 * @param ctx the parse tree
	 */
	void exitVardeclarepipeline(count_parser.VardeclarepipelineContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#varassignpipeline}.
	 * @param ctx the parse tree
	 */
	void enterVarassignpipeline(count_parser.VarassignpipelineContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#varassignpipeline}.
	 * @param ctx the parse tree
	 */
	void exitVarassignpipeline(count_parser.VarassignpipelineContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(count_parser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(count_parser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(count_parser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(count_parser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#fields}.
	 * @param ctx the parse tree
	 */
	void enterFields(count_parser.FieldsContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#fields}.
	 * @param ctx the parse tree
	 */
	void exitFields(count_parser.FieldsContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#funccall}.
	 * @param ctx the parse tree
	 */
	void enterFunccall(count_parser.FunccallContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#funccall}.
	 * @param ctx the parse tree
	 */
	void exitFunccall(count_parser.FunccallContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#methodcall}.
	 * @param ctx the parse tree
	 */
	void enterMethodcall(count_parser.MethodcallContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#methodcall}.
	 * @param ctx the parse tree
	 */
	void exitMethodcall(count_parser.MethodcallContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#end}.
	 * @param ctx the parse tree
	 */
	void enterEnd(count_parser.EndContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#end}.
	 * @param ctx the parse tree
	 */
	void exitEnd(count_parser.EndContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#ld}.
	 * @param ctx the parse tree
	 */
	void enterLd(count_parser.LdContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#ld}.
	 * @param ctx the parse tree
	 */
	void exitLd(count_parser.LdContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#rd}.
	 * @param ctx the parse tree
	 */
	void enterRd(count_parser.RdContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#rd}.
	 * @param ctx the parse tree
	 */
	void exitRd(count_parser.RdContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#globalfunctions}.
	 * @param ctx the parse tree
	 */
	void enterGlobalfunctions(count_parser.GlobalfunctionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#globalfunctions}.
	 * @param ctx the parse tree
	 */
	void exitGlobalfunctions(count_parser.GlobalfunctionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#text}.
	 * @param ctx the parse tree
	 */
	void enterText(count_parser.TextContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#text}.
	 * @param ctx the parse tree
	 */
	void exitText(count_parser.TextContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#style}.
	 * @param ctx the parse tree
	 */
	void enterStyle(count_parser.StyleContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#style}.
	 * @param ctx the parse tree
	 */
	void exitStyle(count_parser.StyleContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#js}.
	 * @param ctx the parse tree
	 */
	void enterJs(count_parser.JsContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#js}.
	 * @param ctx the parse tree
	 */
	void exitJs(count_parser.JsContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#img}.
	 * @param ctx the parse tree
	 */
	void enterImg(count_parser.ImgContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#img}.
	 * @param ctx the parse tree
	 */
	void exitImg(count_parser.ImgContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#default}.
	 * @param ctx the parse tree
	 */
	void enterDefault(count_parser.DefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#default}.
	 * @param ctx the parse tree
	 */
	void exitDefault(count_parser.DefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#href}.
	 * @param ctx the parse tree
	 */
	void enterHref(count_parser.HrefContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#href}.
	 * @param ctx the parse tree
	 */
	void exitHref(count_parser.HrefContext ctx);
	/**
	 * Enter a parse tree produced by {@link count_parser#local}.
	 * @param ctx the parse tree
	 */
	void enterLocal(count_parser.LocalContext ctx);
	/**
	 * Exit a parse tree produced by {@link count_parser#local}.
	 * @param ctx the parse tree
	 */
	void exitLocal(count_parser.LocalContext ctx);
}