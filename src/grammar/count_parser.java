// Generated from count_parser.g4 by ANTLR 4.12.0

import inspect
import json
import os

if not os.path.exists('counter.json'):
    with open('counter.json', 'w+') as file:
        file.write('{}')


import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class count_parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.12.0", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Text=1, Template=2, Block=3, With=4, CommentBegin=5, CommentEnd=6, If=7, 
		Else=8, Range=9, Pipe=10, Comma=11, Assignment=12, Equal=13, Nil=14, LeftParenthesis=15, 
		RightParenthesis=16, Dollar=17, Dot=18, End=19, BlockStart=20, Dash=21, 
		BlockEnd=22, Constant=23, Define=24, And=25, Eq=26, Lt=27, Le=28, Ne=29, 
		Gt=30, Ge=31, Len=32, Not=33, Or=34, Index=35, Slice=36, Printf=37, Myprint=38, 
		Random=39, AnyText=40, AStart=41, HrefStart=42, HrefEnd=43, ScriptStart=44, 
		ScriptEnd=45, StyleStart=46, StyleEnd=47, BrStart=48, BrEnd=49, ImgStart=50, 
		AEnd=51, ImgEnd=52, StringConstant=53, NumberConstant=54, Name=55, WS=56;
	public static final int
		RULE_start = 0, RULE_template = 1, RULE_goaction = 2, RULE_commentaction = 3, 
		RULE_pipelineaction = 4, RULE_ifaction = 5, RULE_rangeaction = 6, RULE_templateaction = 7, 
		RULE_defineAction = 8, RULE_blockAction = 9, RULE_withAction = 10, RULE_pipeline = 11, 
		RULE_vardeclarepipeline = 12, RULE_varassignpipeline = 13, RULE_argument = 14, 
		RULE_variable = 15, RULE_fields = 16, RULE_funccall = 17, RULE_methodcall = 18, 
		RULE_end = 19, RULE_ld = 20, RULE_rd = 21, RULE_globalfunctions = 22, 
		RULE_text = 23, RULE_style = 24, RULE_js = 25, RULE_img = 26, RULE_default = 27, 
		RULE_href = 28, RULE_local = 29;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "template", "goaction", "commentaction", "pipelineaction", "ifaction", 
			"rangeaction", "templateaction", "defineAction", "blockAction", "withAction", 
			"pipeline", "vardeclarepipeline", "varassignpipeline", "argument", "variable", 
			"fields", "funccall", "methodcall", "end", "ld", "rd", "globalfunctions", 
			"text", "style", "js", "img", "default", "href", "local"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'TEXT'", "'template'", "'block'", "'with'", "'/*'", "'*/'", "'if'", 
			"'else'", "'range'", "'|'", "','", "':='", "'='", "'nil'", "'('", "')'", 
			"'$'", "'.'", "'end'", "'{{'", "'-'", "'}}'", "'CONSTANT'", "'define'", 
			"'and'", "'eq'", "'lt'", "'le'", "'ne'", "'gt'", "'ge'", "'len'", "'not'", 
			"'or'", "'index'", "'slice'", "'printf'", "'print'", "'random_string'", 
			"'Comment'", "'<a href=\"#\">'", "'<a href=\"'", "'\">abc</a>'", "'<script>'", 
			"'</script>'", "'<style>'", "'</style>'", "'<br>'", "'</br>'", "'<img src=xx:'", 
			"'</a>'", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "Text", "Template", "Block", "With", "CommentBegin", "CommentEnd", 
			"If", "Else", "Range", "Pipe", "Comma", "Assignment", "Equal", "Nil", 
			"LeftParenthesis", "RightParenthesis", "Dollar", "Dot", "End", "BlockStart", 
			"Dash", "BlockEnd", "Constant", "Define", "And", "Eq", "Lt", "Le", "Ne", 
			"Gt", "Ge", "Len", "Not", "Or", "Index", "Slice", "Printf", "Myprint", 
			"Random", "AnyText", "AStart", "HrefStart", "HrefEnd", "ScriptStart", 
			"ScriptEnd", "StyleStart", "StyleEnd", "BrStart", "BrEnd", "ImgStart", 
			"AEnd", "ImgEnd", "StringConstant", "NumberConstant", "Name", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "count_parser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


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

	public count_parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartContext extends ParserRuleContext {
		public TemplateContext template() {
			return getRuleContext(TemplateContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			template();
			}
			_ctx.stop = _input.LT(-1);

			print(self.counter); 
			with open('counter.json', 'w') as f:
			    json.dump(self.counter, f)
			    
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TemplateContext extends ParserRuleContext {
		public List<TextContext> text() {
			return getRuleContexts(TextContext.class);
		}
		public TextContext text(int i) {
			return getRuleContext(TextContext.class,i);
		}
		public List<GoactionContext> goaction() {
			return getRuleContexts(GoactionContext.class);
		}
		public GoactionContext goaction(int i) {
			return getRuleContext(GoactionContext.class,i);
		}
		public TemplateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_template; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterTemplate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitTemplate(this);
		}
	}

	public final TemplateContext template() throws RecognitionException {
		TemplateContext _localctx = new TemplateContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_template);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Text:
			case AStart:
			case HrefStart:
			case ScriptStart:
			case StyleStart:
			case BrStart:
			case ImgStart:
				{
				setState(62);
				text();
				self.counter[inspect.stack()[0][3]]['text'] = self.counter[inspect.stack()[0][3]]['text'] + 1 if 'text' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case BlockStart:
				{
				setState(65);
				goaction();
				self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(78);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(76);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case Text:
					case AStart:
					case HrefStart:
					case ScriptStart:
					case StyleStart:
					case BrStart:
					case ImgStart:
						{
						setState(70);
						text();
						self.counter[inspect.stack()[0][3]]['text'] = self.counter[inspect.stack()[0][3]]['text'] + 1 if 'text' in self.counter[inspect.stack()[0][3]] else 1
						}
						break;
					case BlockStart:
						{
						setState(73);
						goaction();
						self.counter[inspect.stack()[0][3]]['goaction'] = self.counter[inspect.stack()[0][3]]['goaction'] + 1 if 'goaction' in self.counter[inspect.stack()[0][3]] else 1
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(80);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GoactionContext extends ParserRuleContext {
		public CommentactionContext commentaction() {
			return getRuleContext(CommentactionContext.class,0);
		}
		public PipelineactionContext pipelineaction() {
			return getRuleContext(PipelineactionContext.class,0);
		}
		public IfactionContext ifaction() {
			return getRuleContext(IfactionContext.class,0);
		}
		public RangeactionContext rangeaction() {
			return getRuleContext(RangeactionContext.class,0);
		}
		public TemplateactionContext templateaction() {
			return getRuleContext(TemplateactionContext.class,0);
		}
		public BlockActionContext blockAction() {
			return getRuleContext(BlockActionContext.class,0);
		}
		public WithActionContext withAction() {
			return getRuleContext(WithActionContext.class,0);
		}
		public DefineActionContext defineAction() {
			return getRuleContext(DefineActionContext.class,0);
		}
		public GoactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_goaction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterGoaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitGoaction(this);
		}
	}

	public final GoactionContext goaction() throws RecognitionException {
		GoactionContext _localctx = new GoactionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_goaction);
		try {
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				commentaction();
				self.counter[inspect.stack()[0][3]]['commentaction'] = self.counter[inspect.stack()[0][3]]['commentaction'] + 1 if 'commentaction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(84);
				pipelineaction();
				self.counter[inspect.stack()[0][3]]['pipelineaction'] = self.counter[inspect.stack()[0][3]]['pipelineaction'] + 1 if 'pipelineaction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(87);
				ifaction();
				self.counter[inspect.stack()[0][3]]['ifaction'] = self.counter[inspect.stack()[0][3]]['ifaction'] + 1 if 'ifaction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(90);
				rangeaction();
				self.counter[inspect.stack()[0][3]]['rangeaction'] = self.counter[inspect.stack()[0][3]]['rangeaction'] + 1 if 'rangeaction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(93);
				templateaction();
				self.counter[inspect.stack()[0][3]]['templateaction'] = self.counter[inspect.stack()[0][3]]['templateaction'] + 1 if 'templateaction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(96);
				blockAction();
				self.counter[inspect.stack()[0][3]]['blockAction'] = self.counter[inspect.stack()[0][3]]['blockAction'] + 1 if 'blockAction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(99);
				withAction();
				self.counter[inspect.stack()[0][3]]['withAction'] = self.counter[inspect.stack()[0][3]]['withAction'] + 1 if 'withAction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(102);
				defineAction();
				self.counter[inspect.stack()[0][3]]['defineAction'] = self.counter[inspect.stack()[0][3]]['defineAction'] + 1 if 'defineAction' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommentactionContext extends ParserRuleContext {
		public LdContext ld() {
			return getRuleContext(LdContext.class,0);
		}
		public TerminalNode CommentBegin() { return getToken(count_parser.CommentBegin, 0); }
		public TerminalNode AnyText() { return getToken(count_parser.AnyText, 0); }
		public TerminalNode CommentEnd() { return getToken(count_parser.CommentEnd, 0); }
		public RdContext rd() {
			return getRuleContext(RdContext.class,0);
		}
		public CommentactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commentaction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterCommentaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitCommentaction(this);
		}
	}

	public final CommentactionContext commentaction() throws RecognitionException {
		CommentactionContext _localctx = new CommentactionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_commentaction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			ld();
			setState(108);
			match(CommentBegin);
			setState(109);
			match(AnyText);
			setState(110);
			match(CommentEnd);
			setState(111);
			rd();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipelineactionContext extends ParserRuleContext {
		public LdContext ld() {
			return getRuleContext(LdContext.class,0);
		}
		public RdContext rd() {
			return getRuleContext(RdContext.class,0);
		}
		public PipelineContext pipeline() {
			return getRuleContext(PipelineContext.class,0);
		}
		public VardeclarepipelineContext vardeclarepipeline() {
			return getRuleContext(VardeclarepipelineContext.class,0);
		}
		public VarassignpipelineContext varassignpipeline() {
			return getRuleContext(VarassignpipelineContext.class,0);
		}
		public PipelineactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipelineaction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterPipelineaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitPipelineaction(this);
		}
	}

	public final PipelineactionContext pipelineaction() throws RecognitionException {
		PipelineactionContext _localctx = new PipelineactionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_pipelineaction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			ld();
			setState(123);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(114);
				pipeline();
				self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 2:
				{
				setState(117);
				vardeclarepipeline();
				self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 3:
				{
				setState(120);
				varassignpipeline();
				self.counter[inspect.stack()[0][3]]['varassignpipeline'] = self.counter[inspect.stack()[0][3]]['varassignpipeline'] + 1 if 'varassignpipeline' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			}
			setState(125);
			rd();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfactionContext extends ParserRuleContext {
		public List<LdContext> ld() {
			return getRuleContexts(LdContext.class);
		}
		public LdContext ld(int i) {
			return getRuleContext(LdContext.class,i);
		}
		public List<TerminalNode> If() { return getTokens(count_parser.If); }
		public TerminalNode If(int i) {
			return getToken(count_parser.If, i);
		}
		public List<PipelineContext> pipeline() {
			return getRuleContexts(PipelineContext.class);
		}
		public PipelineContext pipeline(int i) {
			return getRuleContext(PipelineContext.class,i);
		}
		public List<RdContext> rd() {
			return getRuleContexts(RdContext.class);
		}
		public RdContext rd(int i) {
			return getRuleContext(RdContext.class,i);
		}
		public List<TemplateContext> template() {
			return getRuleContexts(TemplateContext.class);
		}
		public TemplateContext template(int i) {
			return getRuleContext(TemplateContext.class,i);
		}
		public EndContext end() {
			return getRuleContext(EndContext.class,0);
		}
		public TerminalNode Else() { return getToken(count_parser.Else, 0); }
		public IfactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifaction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterIfaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitIfaction(this);
		}
	}

	public final IfactionContext ifaction() throws RecognitionException {
		IfactionContext _localctx = new IfactionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_ifaction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			ld();
			setState(128);
			match(If);
			setState(129);
			pipeline();
			setState(130);
			rd();
			setState(131);
			template();
			setState(141);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(132);
				ld();
				setState(133);
				match(Else);
				setState(136);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==If) {
					{
					setState(134);
					match(If);
					setState(135);
					pipeline();
					}
				}

				setState(138);
				rd();
				setState(139);
				template();
				}
				break;
			}
			setState(143);
			end();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RangeactionContext extends ParserRuleContext {
		public List<LdContext> ld() {
			return getRuleContexts(LdContext.class);
		}
		public LdContext ld(int i) {
			return getRuleContext(LdContext.class,i);
		}
		public TerminalNode Range() { return getToken(count_parser.Range, 0); }
		public List<RdContext> rd() {
			return getRuleContexts(RdContext.class);
		}
		public RdContext rd(int i) {
			return getRuleContext(RdContext.class,i);
		}
		public List<TemplateContext> template() {
			return getRuleContexts(TemplateContext.class);
		}
		public TemplateContext template(int i) {
			return getRuleContext(TemplateContext.class,i);
		}
		public EndContext end() {
			return getRuleContext(EndContext.class,0);
		}
		public PipelineContext pipeline() {
			return getRuleContext(PipelineContext.class,0);
		}
		public VardeclarepipelineContext vardeclarepipeline() {
			return getRuleContext(VardeclarepipelineContext.class,0);
		}
		public TerminalNode Else() { return getToken(count_parser.Else, 0); }
		public RangeactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rangeaction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterRangeaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitRangeaction(this);
		}
	}

	public final RangeactionContext rangeaction() throws RecognitionException {
		RangeactionContext _localctx = new RangeactionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_rangeaction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			ld();
			setState(146);
			match(Range);
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(147);
				pipeline();
				self.counter[inspect.stack()[0][3]]['pipeline'] = self.counter[inspect.stack()[0][3]]['pipeline'] + 1 if 'pipeline' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 2:
				{
				setState(150);
				vardeclarepipeline();
				self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] = self.counter[inspect.stack()[0][3]]['vardeclarepipeline'] + 1 if 'vardeclarepipeline' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			}
			setState(155);
			rd();
			setState(156);
			template();
			setState(162);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(157);
				ld();
				setState(158);
				match(Else);
				setState(159);
				rd();
				setState(160);
				template();
				}
				break;
			}
			setState(164);
			end();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TemplateactionContext extends ParserRuleContext {
		public LdContext ld() {
			return getRuleContext(LdContext.class,0);
		}
		public TerminalNode Template() { return getToken(count_parser.Template, 0); }
		public TerminalNode StringConstant() { return getToken(count_parser.StringConstant, 0); }
		public RdContext rd() {
			return getRuleContext(RdContext.class,0);
		}
		public PipelineContext pipeline() {
			return getRuleContext(PipelineContext.class,0);
		}
		public TemplateactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_templateaction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterTemplateaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitTemplateaction(this);
		}
	}

	public final TemplateactionContext templateaction() throws RecognitionException {
		TemplateactionContext _localctx = new TemplateactionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_templateaction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			ld();
			setState(167);
			match(Template);
			setState(168);
			match(StringConstant);
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 27022697242738688L) != 0)) {
				{
				setState(169);
				pipeline();
				}
			}

			setState(172);
			rd();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefineActionContext extends ParserRuleContext {
		public LdContext ld() {
			return getRuleContext(LdContext.class,0);
		}
		public TerminalNode Define() { return getToken(count_parser.Define, 0); }
		public TerminalNode StringConstant() { return getToken(count_parser.StringConstant, 0); }
		public RdContext rd() {
			return getRuleContext(RdContext.class,0);
		}
		public DefineActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defineAction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterDefineAction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitDefineAction(this);
		}
	}

	public final DefineActionContext defineAction() throws RecognitionException {
		DefineActionContext _localctx = new DefineActionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_defineAction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			ld();
			setState(175);
			match(Define);
			setState(176);
			match(StringConstant);
			setState(177);
			rd();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockActionContext extends ParserRuleContext {
		public LdContext ld() {
			return getRuleContext(LdContext.class,0);
		}
		public TerminalNode Block() { return getToken(count_parser.Block, 0); }
		public TerminalNode Name() { return getToken(count_parser.Name, 0); }
		public RdContext rd() {
			return getRuleContext(RdContext.class,0);
		}
		public PipelineContext pipeline() {
			return getRuleContext(PipelineContext.class,0);
		}
		public BlockActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockAction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterBlockAction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitBlockAction(this);
		}
	}

	public final BlockActionContext blockAction() throws RecognitionException {
		BlockActionContext _localctx = new BlockActionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_blockAction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			ld();
			setState(180);
			match(Block);
			setState(181);
			match(Name);
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 27022697242738688L) != 0)) {
				{
				setState(182);
				pipeline();
				}
			}

			setState(185);
			rd();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WithActionContext extends ParserRuleContext {
		public List<LdContext> ld() {
			return getRuleContexts(LdContext.class);
		}
		public LdContext ld(int i) {
			return getRuleContext(LdContext.class,i);
		}
		public TerminalNode With() { return getToken(count_parser.With, 0); }
		public PipelineContext pipeline() {
			return getRuleContext(PipelineContext.class,0);
		}
		public List<RdContext> rd() {
			return getRuleContexts(RdContext.class);
		}
		public RdContext rd(int i) {
			return getRuleContext(RdContext.class,i);
		}
		public List<TemplateContext> template() {
			return getRuleContexts(TemplateContext.class);
		}
		public TemplateContext template(int i) {
			return getRuleContext(TemplateContext.class,i);
		}
		public EndContext end() {
			return getRuleContext(EndContext.class,0);
		}
		public TerminalNode Else() { return getToken(count_parser.Else, 0); }
		public WithActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_withAction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterWithAction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitWithAction(this);
		}
	}

	public final WithActionContext withAction() throws RecognitionException {
		WithActionContext _localctx = new WithActionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_withAction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			ld();
			setState(188);
			match(With);
			setState(189);
			pipeline();
			setState(190);
			rd();
			setState(191);
			template();
			setState(197);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(192);
				ld();
				setState(193);
				match(Else);
				setState(194);
				rd();
				setState(195);
				template();
				}
				break;
			}
			setState(199);
			end();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipelineContext extends ParserRuleContext {
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public List<TerminalNode> Pipe() { return getTokens(count_parser.Pipe); }
		public TerminalNode Pipe(int i) {
			return getToken(count_parser.Pipe, i);
		}
		public MethodcallContext methodcall() {
			return getRuleContext(MethodcallContext.class,0);
		}
		public FunccallContext funccall() {
			return getRuleContext(FunccallContext.class,0);
		}
		public PipelineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipeline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterPipeline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitPipeline(this);
		}
	}

	public final PipelineContext pipeline() throws RecognitionException {
		PipelineContext _localctx = new PipelineContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_pipeline);
		int _la;
		try {
			setState(217);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(201);
				argument();
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Pipe) {
					{
					{
					setState(202);
					match(Pipe);
					setState(203);
					argument();
					}
					}
					setState(208);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				self.counter[inspect.stack()[0][3]]['argument'] = self.counter[inspect.stack()[0][3]]['argument'] + 1 if 'argument' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(211);
				methodcall();
				self.counter[inspect.stack()[0][3]]['methodcall'] = self.counter[inspect.stack()[0][3]]['methodcall'] + 1 if 'methodcall' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(214);
				funccall();
				self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VardeclarepipelineContext extends ParserRuleContext {
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public TerminalNode Assignment() { return getToken(count_parser.Assignment, 0); }
		public PipelineContext pipeline() {
			return getRuleContext(PipelineContext.class,0);
		}
		public TerminalNode Comma() { return getToken(count_parser.Comma, 0); }
		public VardeclarepipelineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardeclarepipeline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterVardeclarepipeline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitVardeclarepipeline(this);
		}
	}

	public final VardeclarepipelineContext vardeclarepipeline() throws RecognitionException {
		VardeclarepipelineContext _localctx = new VardeclarepipelineContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_vardeclarepipeline);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			variable();
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Comma) {
				{
				setState(220);
				match(Comma);
				setState(221);
				variable();
				}
			}

			setState(224);
			match(Assignment);
			setState(225);
			pipeline();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarassignpipelineContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode Equal() { return getToken(count_parser.Equal, 0); }
		public PipelineContext pipeline() {
			return getRuleContext(PipelineContext.class,0);
		}
		public VarassignpipelineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varassignpipeline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterVarassignpipeline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitVarassignpipeline(this);
		}
	}

	public final VarassignpipelineContext varassignpipeline() throws RecognitionException {
		VarassignpipelineContext _localctx = new VarassignpipelineContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_varassignpipeline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			variable();
			setState(228);
			match(Equal);
			setState(229);
			pipeline();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentContext extends ParserRuleContext {
		public TerminalNode Nil() { return getToken(count_parser.Nil, 0); }
		public TerminalNode StringConstant() { return getToken(count_parser.StringConstant, 0); }
		public TerminalNode NumberConstant() { return getToken(count_parser.NumberConstant, 0); }
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public FieldsContext fields() {
			return getRuleContext(FieldsContext.class,0);
		}
		public FunccallContext funccall() {
			return getRuleContext(FunccallContext.class,0);
		}
		public TerminalNode LeftParenthesis() { return getToken(count_parser.LeftParenthesis, 0); }
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public TerminalNode RightParenthesis() { return getToken(count_parser.RightParenthesis, 0); }
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitArgument(this);
		}
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_argument);
		try {
			setState(251);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(231);
				match(Nil);
				self.counter[inspect.stack()[0][3]]['Nil'] = self.counter[inspect.stack()[0][3]]['Nil'] + 1 if 'Nil' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(233);
				match(StringConstant);
				self.counter[inspect.stack()[0][3]]['StringConstant'] = self.counter[inspect.stack()[0][3]]['StringConstant'] + 1 if 'StringConstant' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(235);
				match(NumberConstant);
				self.counter[inspect.stack()[0][3]]['NumberConstant'] = self.counter[inspect.stack()[0][3]]['NumberConstant'] + 1 if 'NumberConstant' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(237);
				variable();
				self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(240);
				fields();
				self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(243);
				funccall();
				self.counter[inspect.stack()[0][3]]['funccall'] = self.counter[inspect.stack()[0][3]]['funccall'] + 1 if 'funccall' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(246);
				match(LeftParenthesis);
				setState(247);
				argument();
				setState(248);
				match(RightParenthesis);
				self.counter[inspect.stack()[0][3]]['LeftParenthesis'] = self.counter[inspect.stack()[0][3]]['LeftParenthesis'] + 1 if 'LeftParenthesis' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VariableContext extends ParserRuleContext {
		public TerminalNode Dollar() { return getToken(count_parser.Dollar, 0); }
		public TerminalNode Name() { return getToken(count_parser.Name, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			match(Dollar);
			setState(255);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Name) {
				{
				setState(254);
				match(Name);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FieldsContext extends ParserRuleContext {
		public List<TerminalNode> Dot() { return getTokens(count_parser.Dot); }
		public TerminalNode Dot(int i) {
			return getToken(count_parser.Dot, i);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public List<TerminalNode> Name() { return getTokens(count_parser.Name); }
		public TerminalNode Name(int i) {
			return getToken(count_parser.Name, i);
		}
		public FieldsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fields; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterFields(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitFields(this);
		}
	}

	public final FieldsContext fields() throws RecognitionException {
		FieldsContext _localctx = new FieldsContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_fields);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Dollar) {
				{
				setState(257);
				variable();
				}
			}

			setState(260);
			match(Dot);
			setState(262);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Name) {
				{
				setState(261);
				match(Name);
				}
			}

			setState(268);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(264);
				match(Dot);
				setState(266);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==Name) {
					{
					setState(265);
					match(Name);
					}
				}

				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunccallContext extends ParserRuleContext {
		public GlobalfunctionsContext globalfunctions() {
			return getRuleContext(GlobalfunctionsContext.class,0);
		}
		public FunccallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funccall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterFunccall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitFunccall(this);
		}
	}

	public final FunccallContext funccall() throws RecognitionException {
		FunccallContext _localctx = new FunccallContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_funccall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			globalfunctions();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodcallContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public FieldsContext fields() {
			return getRuleContext(FieldsContext.class,0);
		}
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public MethodcallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodcall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterMethodcall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitMethodcall(this);
		}
	}

	public final MethodcallContext methodcall() throws RecognitionException {
		MethodcallContext _localctx = new MethodcallContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_methodcall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(272);
				variable();
				self.counter[inspect.stack()[0][3]]['variable'] = self.counter[inspect.stack()[0][3]]['variable'] + 1 if 'variable' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case 2:
				{
				setState(275);
				fields();
				self.counter[inspect.stack()[0][3]]['fields'] = self.counter[inspect.stack()[0][3]]['fields'] + 1 if 'fields' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			}
			setState(283);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 27022697242738688L) != 0)) {
				{
				{
				setState(280);
				argument();
				}
				}
				setState(285);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EndContext extends ParserRuleContext {
		public LdContext ld() {
			return getRuleContext(LdContext.class,0);
		}
		public TerminalNode End() { return getToken(count_parser.End, 0); }
		public RdContext rd() {
			return getRuleContext(RdContext.class,0);
		}
		public EndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterEnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitEnd(this);
		}
	}

	public final EndContext end() throws RecognitionException {
		EndContext _localctx = new EndContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_end);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			ld();
			setState(287);
			match(End);
			setState(288);
			rd();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LdContext extends ParserRuleContext {
		public TerminalNode BlockStart() { return getToken(count_parser.BlockStart, 0); }
		public TerminalNode Dash() { return getToken(count_parser.Dash, 0); }
		public LdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ld; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterLd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitLd(this);
		}
	}

	public final LdContext ld() throws RecognitionException {
		LdContext _localctx = new LdContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_ld);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			match(BlockStart);
			setState(292);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Dash) {
				{
				setState(291);
				match(Dash);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RdContext extends ParserRuleContext {
		public TerminalNode BlockEnd() { return getToken(count_parser.BlockEnd, 0); }
		public TerminalNode Dash() { return getToken(count_parser.Dash, 0); }
		public RdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterRd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitRd(this);
		}
	}

	public final RdContext rd() throws RecognitionException {
		RdContext _localctx = new RdContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_rd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Dash) {
				{
				setState(294);
				match(Dash);
				}
			}

			setState(297);
			match(BlockEnd);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GlobalfunctionsContext extends ParserRuleContext {
		public TerminalNode And() { return getToken(count_parser.And, 0); }
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public TerminalNode Index() { return getToken(count_parser.Index, 0); }
		public TerminalNode Slice() { return getToken(count_parser.Slice, 0); }
		public TerminalNode Len() { return getToken(count_parser.Len, 0); }
		public TerminalNode Not() { return getToken(count_parser.Not, 0); }
		public TerminalNode Or() { return getToken(count_parser.Or, 0); }
		public TerminalNode Printf() { return getToken(count_parser.Printf, 0); }
		public TerminalNode Eq() { return getToken(count_parser.Eq, 0); }
		public TerminalNode Ne() { return getToken(count_parser.Ne, 0); }
		public TerminalNode Lt() { return getToken(count_parser.Lt, 0); }
		public TerminalNode Le() { return getToken(count_parser.Le, 0); }
		public TerminalNode Gt() { return getToken(count_parser.Gt, 0); }
		public TerminalNode Ge() { return getToken(count_parser.Ge, 0); }
		public TerminalNode Random() { return getToken(count_parser.Random, 0); }
		public TerminalNode Myprint() { return getToken(count_parser.Myprint, 0); }
		public GlobalfunctionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globalfunctions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterGlobalfunctions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitGlobalfunctions(this);
		}
	}

	public final GlobalfunctionsContext globalfunctions() throws RecognitionException {
		GlobalfunctionsContext _localctx = new GlobalfunctionsContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_globalfunctions);
		try {
			int _alt;
			setState(385);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case And:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(299);
				match(And);
				setState(300);
				argument();
				setState(301);
				argument();
				}
				self.counter[inspect.stack()[0][3]]['And'] = self.counter[inspect.stack()[0][3]]['And'] + 1 if 'And' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Index:
				enterOuterAlt(_localctx, 2);
				{
				setState(305);
				match(Index);
				setState(306);
				argument();
				setState(310);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(307);
						argument();
						}
						} 
					}
					setState(312);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
				}
				self.counter[inspect.stack()[0][3]]['Index'] = self.counter[inspect.stack()[0][3]]['Index'] + 1 if 'Index' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Slice:
				enterOuterAlt(_localctx, 3);
				{
				setState(315);
				match(Slice);
				setState(316);
				argument();
				setState(320);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(317);
						argument();
						}
						} 
					}
					setState(322);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
				}
				self.counter[inspect.stack()[0][3]]['Slice'] = self.counter[inspect.stack()[0][3]]['Slice'] + 1 if 'Slice' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Len:
				enterOuterAlt(_localctx, 4);
				{
				setState(325);
				match(Len);
				setState(326);
				argument();
				self.counter[inspect.stack()[0][3]]['Len'] = self.counter[inspect.stack()[0][3]]['Len'] + 1 if 'Len' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Not:
				enterOuterAlt(_localctx, 5);
				{
				setState(329);
				match(Not);
				setState(330);
				argument();
				self.counter[inspect.stack()[0][3]]['Len'] = self.counter[inspect.stack()[0][3]]['Len'] + 1 if 'Len' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Or:
				enterOuterAlt(_localctx, 6);
				{
				setState(333);
				match(Or);
				setState(334);
				argument();
				setState(335);
				argument();
				self.counter[inspect.stack()[0][3]]['Or'] = self.counter[inspect.stack()[0][3]]['Or'] + 1 if 'Or' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Printf:
				enterOuterAlt(_localctx, 7);
				{
				setState(338);
				match(Printf);
				setState(339);
				argument();
				setState(343);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(340);
						argument();
						}
						} 
					}
					setState(345);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
				}
				self.counter[inspect.stack()[0][3]]['Printf'] = self.counter[inspect.stack()[0][3]]['Printf'] + 1 if 'Printf' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Eq:
				enterOuterAlt(_localctx, 8);
				{
				setState(348);
				match(Eq);
				setState(349);
				argument();
				setState(350);
				argument();
				self.counter[inspect.stack()[0][3]]['Eq'] = self.counter[inspect.stack()[0][3]]['Eq'] + 1 if 'Eq' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Ne:
				enterOuterAlt(_localctx, 9);
				{
				setState(353);
				match(Ne);
				setState(354);
				argument();
				setState(355);
				argument();
				self.counter[inspect.stack()[0][3]]['Ne'] = self.counter[inspect.stack()[0][3]]['Ne'] + 1 if 'Ne' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Lt:
				enterOuterAlt(_localctx, 10);
				{
				setState(358);
				match(Lt);
				setState(359);
				argument();
				setState(360);
				argument();
				self.counter[inspect.stack()[0][3]]['Lt'] = self.counter[inspect.stack()[0][3]]['Lt'] + 1 if 'Lt' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Le:
				enterOuterAlt(_localctx, 11);
				{
				setState(363);
				match(Le);
				setState(364);
				argument();
				setState(365);
				argument();
				self.counter[inspect.stack()[0][3]]['Le'] = self.counter[inspect.stack()[0][3]]['Le'] + 1 if 'Le' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Gt:
				enterOuterAlt(_localctx, 12);
				{
				{
				setState(368);
				match(Gt);
				setState(369);
				argument();
				setState(370);
				argument();
				}
				self.counter[inspect.stack()[0][3]]['Gt'] = self.counter[inspect.stack()[0][3]]['Gt'] + 1 if 'Gt' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Ge:
				enterOuterAlt(_localctx, 13);
				{
				setState(374);
				match(Ge);
				setState(375);
				argument();
				setState(376);
				argument();
				self.counter[inspect.stack()[0][3]]['Ge'] = self.counter[inspect.stack()[0][3]]['Ge'] + 1 if 'Ge' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Random:
				enterOuterAlt(_localctx, 14);
				{
				setState(379);
				match(Random);
				self.counter[inspect.stack()[0][3]]['random'] = self.counter[inspect.stack()[0][3]]['random'] + 1 if 'random' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case Myprint:
				enterOuterAlt(_localctx, 15);
				{
				setState(381);
				match(Myprint);
				setState(382);
				argument();
				self.counter[inspect.stack()[0][3]]['myprint'] = self.counter[inspect.stack()[0][3]]['myprint'] + 1 if 'myprint' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TextContext extends ParserRuleContext {
		public TerminalNode Text() { return getToken(count_parser.Text, 0); }
		public StyleContext style() {
			return getRuleContext(StyleContext.class,0);
		}
		public JsContext js() {
			return getRuleContext(JsContext.class,0);
		}
		public ImgContext img() {
			return getRuleContext(ImgContext.class,0);
		}
		public DefaultContext default_() {
			return getRuleContext(DefaultContext.class,0);
		}
		public HrefContext href() {
			return getRuleContext(HrefContext.class,0);
		}
		public TextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_text; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterText(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitText(this);
		}
	}

	public final TextContext text() throws RecognitionException {
		TextContext _localctx = new TextContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_text);
		try {
			setState(404);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Text:
				enterOuterAlt(_localctx, 1);
				{
				setState(387);
				match(Text);
				self.counter[inspect.stack()[0][3]]['Text'] = self.counter[inspect.stack()[0][3]]['Text'] + 1 if 'Text' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case StyleStart:
				enterOuterAlt(_localctx, 2);
				{
				setState(389);
				style();
				self.counter[inspect.stack()[0][3]]['style'] = self.counter[inspect.stack()[0][3]]['style'] + 1 if 'style' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case ScriptStart:
				enterOuterAlt(_localctx, 3);
				{
				setState(392);
				js();
				self.counter[inspect.stack()[0][3]]['js'] = self.counter[inspect.stack()[0][3]]['js'] + 1 if 'js' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case ImgStart:
				enterOuterAlt(_localctx, 4);
				{
				setState(395);
				img();
				self.counter[inspect.stack()[0][3]]['img'] = self.counter[inspect.stack()[0][3]]['img'] + 1 if 'img' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case BrStart:
				enterOuterAlt(_localctx, 5);
				{
				setState(398);
				default_();
				self.counter[inspect.stack()[0][3]]['default'] = self.counter[inspect.stack()[0][3]]['default'] + 1 if 'default' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case AStart:
			case HrefStart:
				enterOuterAlt(_localctx, 6);
				{
				setState(401);
				href();
				self.counter[inspect.stack()[0][3]]['href'] = self.counter[inspect.stack()[0][3]]['href'] + 1 if 'href' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StyleContext extends ParserRuleContext {
		public TerminalNode StyleStart() { return getToken(count_parser.StyleStart, 0); }
		public GoactionContext goaction() {
			return getRuleContext(GoactionContext.class,0);
		}
		public TerminalNode StyleEnd() { return getToken(count_parser.StyleEnd, 0); }
		public StyleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_style; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterStyle(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitStyle(this);
		}
	}

	public final StyleContext style() throws RecognitionException {
		StyleContext _localctx = new StyleContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_style);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(406);
			match(StyleStart);
			setState(407);
			goaction();
			setState(408);
			match(StyleEnd);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsContext extends ParserRuleContext {
		public TerminalNode ScriptStart() { return getToken(count_parser.ScriptStart, 0); }
		public GoactionContext goaction() {
			return getRuleContext(GoactionContext.class,0);
		}
		public TerminalNode ScriptEnd() { return getToken(count_parser.ScriptEnd, 0); }
		public JsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_js; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterJs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitJs(this);
		}
	}

	public final JsContext js() throws RecognitionException {
		JsContext _localctx = new JsContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_js);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(410);
			match(ScriptStart);
			setState(411);
			goaction();
			setState(412);
			match(ScriptEnd);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImgContext extends ParserRuleContext {
		public TerminalNode ImgStart() { return getToken(count_parser.ImgStart, 0); }
		public GoactionContext goaction() {
			return getRuleContext(GoactionContext.class,0);
		}
		public TerminalNode ImgEnd() { return getToken(count_parser.ImgEnd, 0); }
		public ImgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_img; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterImg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitImg(this);
		}
	}

	public final ImgContext img() throws RecognitionException {
		ImgContext _localctx = new ImgContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_img);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(414);
			match(ImgStart);
			setState(415);
			goaction();
			setState(416);
			match(ImgEnd);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefaultContext extends ParserRuleContext {
		public TerminalNode BrStart() { return getToken(count_parser.BrStart, 0); }
		public GoactionContext goaction() {
			return getRuleContext(GoactionContext.class,0);
		}
		public TerminalNode BrEnd() { return getToken(count_parser.BrEnd, 0); }
		public DefaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_default; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterDefault(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitDefault(this);
		}
	}

	public final DefaultContext default_() throws RecognitionException {
		DefaultContext _localctx = new DefaultContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_default);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(418);
			match(BrStart);
			setState(419);
			goaction();
			setState(420);
			match(BrEnd);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HrefContext extends ParserRuleContext {
		public TerminalNode AStart() { return getToken(count_parser.AStart, 0); }
		public GoactionContext goaction() {
			return getRuleContext(GoactionContext.class,0);
		}
		public TerminalNode AEnd() { return getToken(count_parser.AEnd, 0); }
		public TerminalNode HrefStart() { return getToken(count_parser.HrefStart, 0); }
		public TerminalNode HrefEnd() { return getToken(count_parser.HrefEnd, 0); }
		public HrefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_href; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterHref(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitHref(this);
		}
	}

	public final HrefContext href() throws RecognitionException {
		HrefContext _localctx = new HrefContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_href);
		try {
			setState(432);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AStart:
				enterOuterAlt(_localctx, 1);
				{
				setState(422);
				match(AStart);
				setState(423);
				goaction();
				setState(424);
				match(AEnd);
				self.counter[inspect.stack()[0][3]]['AStart'] = self.counter[inspect.stack()[0][3]]['AStart'] + 1 if 'AStart' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			case HrefStart:
				enterOuterAlt(_localctx, 2);
				{
				setState(427);
				match(HrefStart);
				setState(428);
				goaction();
				setState(429);
				match(HrefEnd);
				self.counter[inspect.stack()[0][3]]['HrefStart'] = self.counter[inspect.stack()[0][3]]['HrefStart'] + 1 if 'HrefStart' in self.counter[inspect.stack()[0][3]] else 1
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LocalContext extends ParserRuleContext {
		public TerminalNode Name() { return getToken(count_parser.Name, 0); }
		public LocalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_local; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).enterLocal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof count_parserListener ) ((count_parserListener)listener).exitLocal(this);
		}
	}

	public final LocalContext local() throws RecognitionException {
		LocalContext _localctx = new LocalContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_local);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(434);
			match(Name);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u00018\u01b5\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001E\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0005\u0001M\b\u0001\n\u0001\f\u0001P\t\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002j\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004|\b\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0003\u0005\u0089\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005\u008e\b\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u009a\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u00a3\b\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"\u00ab\b\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u00b8\b\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u00c6\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0005\u000b\u00cd\b\u000b\n\u000b\f\u000b\u00d0\t\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0003\u000b\u00da\b\u000b\u0001\f\u0001\f\u0001\f\u0003\f"+
		"\u00df\b\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0003\u000e\u00fc\b\u000e\u0001\u000f\u0001\u000f\u0003"+
		"\u000f\u0100\b\u000f\u0001\u0010\u0003\u0010\u0103\b\u0010\u0001\u0010"+
		"\u0001\u0010\u0003\u0010\u0107\b\u0010\u0001\u0010\u0001\u0010\u0003\u0010"+
		"\u010b\b\u0010\u0003\u0010\u010d\b\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003"+
		"\u0012\u0117\b\u0012\u0001\u0012\u0005\u0012\u011a\b\u0012\n\u0012\f\u0012"+
		"\u011d\t\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u0125\b\u0014\u0001\u0015\u0003\u0015\u0128\b"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0005"+
		"\u0016\u0135\b\u0016\n\u0016\f\u0016\u0138\t\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u013f\b\u0016\n\u0016"+
		"\f\u0016\u0142\t\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0005\u0016\u0156\b\u0016\n\u0016\f\u0016\u0159"+
		"\t\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u0182\b\u0016\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u0195"+
		"\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u01b1\b\u001c\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0000\u0000\u001e\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:\u0000"+
		"\u0000\u01d3\u0000<\u0001\u0000\u0000\u0000\u0002D\u0001\u0000\u0000\u0000"+
		"\u0004i\u0001\u0000\u0000\u0000\u0006k\u0001\u0000\u0000\u0000\bq\u0001"+
		"\u0000\u0000\u0000\n\u007f\u0001\u0000\u0000\u0000\f\u0091\u0001\u0000"+
		"\u0000\u0000\u000e\u00a6\u0001\u0000\u0000\u0000\u0010\u00ae\u0001\u0000"+
		"\u0000\u0000\u0012\u00b3\u0001\u0000\u0000\u0000\u0014\u00bb\u0001\u0000"+
		"\u0000\u0000\u0016\u00d9\u0001\u0000\u0000\u0000\u0018\u00db\u0001\u0000"+
		"\u0000\u0000\u001a\u00e3\u0001\u0000\u0000\u0000\u001c\u00fb\u0001\u0000"+
		"\u0000\u0000\u001e\u00fd\u0001\u0000\u0000\u0000 \u0102\u0001\u0000\u0000"+
		"\u0000\"\u010e\u0001\u0000\u0000\u0000$\u0116\u0001\u0000\u0000\u0000"+
		"&\u011e\u0001\u0000\u0000\u0000(\u0122\u0001\u0000\u0000\u0000*\u0127"+
		"\u0001\u0000\u0000\u0000,\u0181\u0001\u0000\u0000\u0000.\u0194\u0001\u0000"+
		"\u0000\u00000\u0196\u0001\u0000\u0000\u00002\u019a\u0001\u0000\u0000\u0000"+
		"4\u019e\u0001\u0000\u0000\u00006\u01a2\u0001\u0000\u0000\u00008\u01b0"+
		"\u0001\u0000\u0000\u0000:\u01b2\u0001\u0000\u0000\u0000<=\u0003\u0002"+
		"\u0001\u0000=\u0001\u0001\u0000\u0000\u0000>?\u0003.\u0017\u0000?@\u0006"+
		"\u0001\uffff\uffff\u0000@E\u0001\u0000\u0000\u0000AB\u0003\u0004\u0002"+
		"\u0000BC\u0006\u0001\uffff\uffff\u0000CE\u0001\u0000\u0000\u0000D>\u0001"+
		"\u0000\u0000\u0000DA\u0001\u0000\u0000\u0000EN\u0001\u0000\u0000\u0000"+
		"FG\u0003.\u0017\u0000GH\u0006\u0001\uffff\uffff\u0000HM\u0001\u0000\u0000"+
		"\u0000IJ\u0003\u0004\u0002\u0000JK\u0006\u0001\uffff\uffff\u0000KM\u0001"+
		"\u0000\u0000\u0000LF\u0001\u0000\u0000\u0000LI\u0001\u0000\u0000\u0000"+
		"MP\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000"+
		"\u0000O\u0003\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000QR\u0003"+
		"\u0006\u0003\u0000RS\u0006\u0002\uffff\uffff\u0000Sj\u0001\u0000\u0000"+
		"\u0000TU\u0003\b\u0004\u0000UV\u0006\u0002\uffff\uffff\u0000Vj\u0001\u0000"+
		"\u0000\u0000WX\u0003\n\u0005\u0000XY\u0006\u0002\uffff\uffff\u0000Yj\u0001"+
		"\u0000\u0000\u0000Z[\u0003\f\u0006\u0000[\\\u0006\u0002\uffff\uffff\u0000"+
		"\\j\u0001\u0000\u0000\u0000]^\u0003\u000e\u0007\u0000^_\u0006\u0002\uffff"+
		"\uffff\u0000_j\u0001\u0000\u0000\u0000`a\u0003\u0012\t\u0000ab\u0006\u0002"+
		"\uffff\uffff\u0000bj\u0001\u0000\u0000\u0000cd\u0003\u0014\n\u0000de\u0006"+
		"\u0002\uffff\uffff\u0000ej\u0001\u0000\u0000\u0000fg\u0003\u0010\b\u0000"+
		"gh\u0006\u0002\uffff\uffff\u0000hj\u0001\u0000\u0000\u0000iQ\u0001\u0000"+
		"\u0000\u0000iT\u0001\u0000\u0000\u0000iW\u0001\u0000\u0000\u0000iZ\u0001"+
		"\u0000\u0000\u0000i]\u0001\u0000\u0000\u0000i`\u0001\u0000\u0000\u0000"+
		"ic\u0001\u0000\u0000\u0000if\u0001\u0000\u0000\u0000j\u0005\u0001\u0000"+
		"\u0000\u0000kl\u0003(\u0014\u0000lm\u0005\u0005\u0000\u0000mn\u0005(\u0000"+
		"\u0000no\u0005\u0006\u0000\u0000op\u0003*\u0015\u0000p\u0007\u0001\u0000"+
		"\u0000\u0000q{\u0003(\u0014\u0000rs\u0003\u0016\u000b\u0000st\u0006\u0004"+
		"\uffff\uffff\u0000t|\u0001\u0000\u0000\u0000uv\u0003\u0018\f\u0000vw\u0006"+
		"\u0004\uffff\uffff\u0000w|\u0001\u0000\u0000\u0000xy\u0003\u001a\r\u0000"+
		"yz\u0006\u0004\uffff\uffff\u0000z|\u0001\u0000\u0000\u0000{r\u0001\u0000"+
		"\u0000\u0000{u\u0001\u0000\u0000\u0000{x\u0001\u0000\u0000\u0000|}\u0001"+
		"\u0000\u0000\u0000}~\u0003*\u0015\u0000~\t\u0001\u0000\u0000\u0000\u007f"+
		"\u0080\u0003(\u0014\u0000\u0080\u0081\u0005\u0007\u0000\u0000\u0081\u0082"+
		"\u0003\u0016\u000b\u0000\u0082\u0083\u0003*\u0015\u0000\u0083\u008d\u0003"+
		"\u0002\u0001\u0000\u0084\u0085\u0003(\u0014\u0000\u0085\u0088\u0005\b"+
		"\u0000\u0000\u0086\u0087\u0005\u0007\u0000\u0000\u0087\u0089\u0003\u0016"+
		"\u000b\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000"+
		"\u0000\u0000\u0089\u008a\u0001\u0000\u0000\u0000\u008a\u008b\u0003*\u0015"+
		"\u0000\u008b\u008c\u0003\u0002\u0001\u0000\u008c\u008e\u0001\u0000\u0000"+
		"\u0000\u008d\u0084\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000"+
		"\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u0090\u0003&\u0013\u0000"+
		"\u0090\u000b\u0001\u0000\u0000\u0000\u0091\u0092\u0003(\u0014\u0000\u0092"+
		"\u0099\u0005\t\u0000\u0000\u0093\u0094\u0003\u0016\u000b\u0000\u0094\u0095"+
		"\u0006\u0006\uffff\uffff\u0000\u0095\u009a\u0001\u0000\u0000\u0000\u0096"+
		"\u0097\u0003\u0018\f\u0000\u0097\u0098\u0006\u0006\uffff\uffff\u0000\u0098"+
		"\u009a\u0001\u0000\u0000\u0000\u0099\u0093\u0001\u0000\u0000\u0000\u0099"+
		"\u0096\u0001\u0000\u0000\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b"+
		"\u009c\u0003*\u0015\u0000\u009c\u00a2\u0003\u0002\u0001\u0000\u009d\u009e"+
		"\u0003(\u0014\u0000\u009e\u009f\u0005\b\u0000\u0000\u009f\u00a0\u0003"+
		"*\u0015\u0000\u00a0\u00a1\u0003\u0002\u0001\u0000\u00a1\u00a3\u0001\u0000"+
		"\u0000\u0000\u00a2\u009d\u0001\u0000\u0000\u0000\u00a2\u00a3\u0001\u0000"+
		"\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a5\u0003&\u0013"+
		"\u0000\u00a5\r\u0001\u0000\u0000\u0000\u00a6\u00a7\u0003(\u0014\u0000"+
		"\u00a7\u00a8\u0005\u0002\u0000\u0000\u00a8\u00aa\u00055\u0000\u0000\u00a9"+
		"\u00ab\u0003\u0016\u000b\u0000\u00aa\u00a9\u0001\u0000\u0000\u0000\u00aa"+
		"\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000\u00ac"+
		"\u00ad\u0003*\u0015\u0000\u00ad\u000f\u0001\u0000\u0000\u0000\u00ae\u00af"+
		"\u0003(\u0014\u0000\u00af\u00b0\u0005\u0018\u0000\u0000\u00b0\u00b1\u0005"+
		"5\u0000\u0000\u00b1\u00b2\u0003*\u0015\u0000\u00b2\u0011\u0001\u0000\u0000"+
		"\u0000\u00b3\u00b4\u0003(\u0014\u0000\u00b4\u00b5\u0005\u0003\u0000\u0000"+
		"\u00b5\u00b7\u00057\u0000\u0000\u00b6\u00b8\u0003\u0016\u000b\u0000\u00b7"+
		"\u00b6\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8"+
		"\u00b9\u0001\u0000\u0000\u0000\u00b9\u00ba\u0003*\u0015\u0000\u00ba\u0013"+
		"\u0001\u0000\u0000\u0000\u00bb\u00bc\u0003(\u0014\u0000\u00bc\u00bd\u0005"+
		"\u0004\u0000\u0000\u00bd\u00be\u0003\u0016\u000b\u0000\u00be\u00bf\u0003"+
		"*\u0015\u0000\u00bf\u00c5\u0003\u0002\u0001\u0000\u00c0\u00c1\u0003(\u0014"+
		"\u0000\u00c1\u00c2\u0005\b\u0000\u0000\u00c2\u00c3\u0003*\u0015\u0000"+
		"\u00c3\u00c4\u0003\u0002\u0001\u0000\u00c4\u00c6\u0001\u0000\u0000\u0000"+
		"\u00c5\u00c0\u0001\u0000\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000"+
		"\u00c6\u00c7\u0001\u0000\u0000\u0000\u00c7\u00c8\u0003&\u0013\u0000\u00c8"+
		"\u0015\u0001\u0000\u0000\u0000\u00c9\u00ce\u0003\u001c\u000e\u0000\u00ca"+
		"\u00cb\u0005\n\u0000\u0000\u00cb\u00cd\u0003\u001c\u000e\u0000\u00cc\u00ca"+
		"\u0001\u0000\u0000\u0000\u00cd\u00d0\u0001\u0000\u0000\u0000\u00ce\u00cc"+
		"\u0001\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf\u00d1"+
		"\u0001\u0000\u0000\u0000\u00d0\u00ce\u0001\u0000\u0000\u0000\u00d1\u00d2"+
		"\u0006\u000b\uffff\uffff\u0000\u00d2\u00da\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d4\u0003$\u0012\u0000\u00d4\u00d5\u0006\u000b\uffff\uffff\u0000\u00d5"+
		"\u00da\u0001\u0000\u0000\u0000\u00d6\u00d7\u0003\"\u0011\u0000\u00d7\u00d8"+
		"\u0006\u000b\uffff\uffff\u0000\u00d8\u00da\u0001\u0000\u0000\u0000\u00d9"+
		"\u00c9\u0001\u0000\u0000\u0000\u00d9\u00d3\u0001\u0000\u0000\u0000\u00d9"+
		"\u00d6\u0001\u0000\u0000\u0000\u00da\u0017\u0001\u0000\u0000\u0000\u00db"+
		"\u00de\u0003\u001e\u000f\u0000\u00dc\u00dd\u0005\u000b\u0000\u0000\u00dd"+
		"\u00df\u0003\u001e\u000f\u0000\u00de\u00dc\u0001\u0000\u0000\u0000\u00de"+
		"\u00df\u0001\u0000\u0000\u0000\u00df\u00e0\u0001\u0000\u0000\u0000\u00e0"+
		"\u00e1\u0005\f\u0000\u0000\u00e1\u00e2\u0003\u0016\u000b\u0000\u00e2\u0019"+
		"\u0001\u0000\u0000\u0000\u00e3\u00e4\u0003\u001e\u000f\u0000\u00e4\u00e5"+
		"\u0005\r\u0000\u0000\u00e5\u00e6\u0003\u0016\u000b\u0000\u00e6\u001b\u0001"+
		"\u0000\u0000\u0000\u00e7\u00e8\u0005\u000e\u0000\u0000\u00e8\u00fc\u0006"+
		"\u000e\uffff\uffff\u0000\u00e9\u00ea\u00055\u0000\u0000\u00ea\u00fc\u0006"+
		"\u000e\uffff\uffff\u0000\u00eb\u00ec\u00056\u0000\u0000\u00ec\u00fc\u0006"+
		"\u000e\uffff\uffff\u0000\u00ed\u00ee\u0003\u001e\u000f\u0000\u00ee\u00ef"+
		"\u0006\u000e\uffff\uffff\u0000\u00ef\u00fc\u0001\u0000\u0000\u0000\u00f0"+
		"\u00f1\u0003 \u0010\u0000\u00f1\u00f2\u0006\u000e\uffff\uffff\u0000\u00f2"+
		"\u00fc\u0001\u0000\u0000\u0000\u00f3\u00f4\u0003\"\u0011\u0000\u00f4\u00f5"+
		"\u0006\u000e\uffff\uffff\u0000\u00f5\u00fc\u0001\u0000\u0000\u0000\u00f6"+
		"\u00f7\u0005\u000f\u0000\u0000\u00f7\u00f8\u0003\u001c\u000e\u0000\u00f8"+
		"\u00f9\u0005\u0010\u0000\u0000\u00f9\u00fa\u0006\u000e\uffff\uffff\u0000"+
		"\u00fa\u00fc\u0001\u0000\u0000\u0000\u00fb\u00e7\u0001\u0000\u0000\u0000"+
		"\u00fb\u00e9\u0001\u0000\u0000\u0000\u00fb\u00eb\u0001\u0000\u0000\u0000"+
		"\u00fb\u00ed\u0001\u0000\u0000\u0000\u00fb\u00f0\u0001\u0000\u0000\u0000"+
		"\u00fb\u00f3\u0001\u0000\u0000\u0000\u00fb\u00f6\u0001\u0000\u0000\u0000"+
		"\u00fc\u001d\u0001\u0000\u0000\u0000\u00fd\u00ff\u0005\u0011\u0000\u0000"+
		"\u00fe\u0100\u00057\u0000\u0000\u00ff\u00fe\u0001\u0000\u0000\u0000\u00ff"+
		"\u0100\u0001\u0000\u0000\u0000\u0100\u001f\u0001\u0000\u0000\u0000\u0101"+
		"\u0103\u0003\u001e\u000f\u0000\u0102\u0101\u0001\u0000\u0000\u0000\u0102"+
		"\u0103\u0001\u0000\u0000\u0000\u0103\u0104\u0001\u0000\u0000\u0000\u0104"+
		"\u0106\u0005\u0012\u0000\u0000\u0105\u0107\u00057\u0000\u0000\u0106\u0105"+
		"\u0001\u0000\u0000\u0000\u0106\u0107\u0001\u0000\u0000\u0000\u0107\u010c"+
		"\u0001\u0000\u0000\u0000\u0108\u010a\u0005\u0012\u0000\u0000\u0109\u010b"+
		"\u00057\u0000\u0000\u010a\u0109\u0001\u0000\u0000\u0000\u010a\u010b\u0001"+
		"\u0000\u0000\u0000\u010b\u010d\u0001\u0000\u0000\u0000\u010c\u0108\u0001"+
		"\u0000\u0000\u0000\u010c\u010d\u0001\u0000\u0000\u0000\u010d!\u0001\u0000"+
		"\u0000\u0000\u010e\u010f\u0003,\u0016\u0000\u010f#\u0001\u0000\u0000\u0000"+
		"\u0110\u0111\u0003\u001e\u000f\u0000\u0111\u0112\u0006\u0012\uffff\uffff"+
		"\u0000\u0112\u0117\u0001\u0000\u0000\u0000\u0113\u0114\u0003 \u0010\u0000"+
		"\u0114\u0115\u0006\u0012\uffff\uffff\u0000\u0115\u0117\u0001\u0000\u0000"+
		"\u0000\u0116\u0110\u0001\u0000\u0000\u0000\u0116\u0113\u0001\u0000\u0000"+
		"\u0000\u0117\u011b\u0001\u0000\u0000\u0000\u0118\u011a\u0003\u001c\u000e"+
		"\u0000\u0119\u0118\u0001\u0000\u0000\u0000\u011a\u011d\u0001\u0000\u0000"+
		"\u0000\u011b\u0119\u0001\u0000\u0000\u0000\u011b\u011c\u0001\u0000\u0000"+
		"\u0000\u011c%\u0001\u0000\u0000\u0000\u011d\u011b\u0001\u0000\u0000\u0000"+
		"\u011e\u011f\u0003(\u0014\u0000\u011f\u0120\u0005\u0013\u0000\u0000\u0120"+
		"\u0121\u0003*\u0015\u0000\u0121\'\u0001\u0000\u0000\u0000\u0122\u0124"+
		"\u0005\u0014\u0000\u0000\u0123\u0125\u0005\u0015\u0000\u0000\u0124\u0123"+
		"\u0001\u0000\u0000\u0000\u0124\u0125\u0001\u0000\u0000\u0000\u0125)\u0001"+
		"\u0000\u0000\u0000\u0126\u0128\u0005\u0015\u0000\u0000\u0127\u0126\u0001"+
		"\u0000\u0000\u0000\u0127\u0128\u0001\u0000\u0000\u0000\u0128\u0129\u0001"+
		"\u0000\u0000\u0000\u0129\u012a\u0005\u0016\u0000\u0000\u012a+\u0001\u0000"+
		"\u0000\u0000\u012b\u012c\u0005\u0019\u0000\u0000\u012c\u012d\u0003\u001c"+
		"\u000e\u0000\u012d\u012e\u0003\u001c\u000e\u0000\u012e\u012f\u0001\u0000"+
		"\u0000\u0000\u012f\u0130\u0006\u0016\uffff\uffff\u0000\u0130\u0182\u0001"+
		"\u0000\u0000\u0000\u0131\u0132\u0005#\u0000\u0000\u0132\u0136\u0003\u001c"+
		"\u000e\u0000\u0133\u0135\u0003\u001c\u000e\u0000\u0134\u0133\u0001\u0000"+
		"\u0000\u0000\u0135\u0138\u0001\u0000\u0000\u0000\u0136\u0134\u0001\u0000"+
		"\u0000\u0000\u0136\u0137\u0001\u0000\u0000\u0000\u0137\u0139\u0001\u0000"+
		"\u0000\u0000\u0138\u0136\u0001\u0000\u0000\u0000\u0139\u013a\u0006\u0016"+
		"\uffff\uffff\u0000\u013a\u0182\u0001\u0000\u0000\u0000\u013b\u013c\u0005"+
		"$\u0000\u0000\u013c\u0140\u0003\u001c\u000e\u0000\u013d\u013f\u0003\u001c"+
		"\u000e\u0000\u013e\u013d\u0001\u0000\u0000\u0000\u013f\u0142\u0001\u0000"+
		"\u0000\u0000\u0140\u013e\u0001\u0000\u0000\u0000\u0140\u0141\u0001\u0000"+
		"\u0000\u0000\u0141\u0143\u0001\u0000\u0000\u0000\u0142\u0140\u0001\u0000"+
		"\u0000\u0000\u0143\u0144\u0006\u0016\uffff\uffff\u0000\u0144\u0182\u0001"+
		"\u0000\u0000\u0000\u0145\u0146\u0005 \u0000\u0000\u0146\u0147\u0003\u001c"+
		"\u000e\u0000\u0147\u0148\u0006\u0016\uffff\uffff\u0000\u0148\u0182\u0001"+
		"\u0000\u0000\u0000\u0149\u014a\u0005!\u0000\u0000\u014a\u014b\u0003\u001c"+
		"\u000e\u0000\u014b\u014c\u0006\u0016\uffff\uffff\u0000\u014c\u0182\u0001"+
		"\u0000\u0000\u0000\u014d\u014e\u0005\"\u0000\u0000\u014e\u014f\u0003\u001c"+
		"\u000e\u0000\u014f\u0150\u0003\u001c\u000e\u0000\u0150\u0151\u0006\u0016"+
		"\uffff\uffff\u0000\u0151\u0182\u0001\u0000\u0000\u0000\u0152\u0153\u0005"+
		"%\u0000\u0000\u0153\u0157\u0003\u001c\u000e\u0000\u0154\u0156\u0003\u001c"+
		"\u000e\u0000\u0155\u0154\u0001\u0000\u0000\u0000\u0156\u0159\u0001\u0000"+
		"\u0000\u0000\u0157\u0155\u0001\u0000\u0000\u0000\u0157\u0158\u0001\u0000"+
		"\u0000\u0000\u0158\u015a\u0001\u0000\u0000\u0000\u0159\u0157\u0001\u0000"+
		"\u0000\u0000\u015a\u015b\u0006\u0016\uffff\uffff\u0000\u015b\u0182\u0001"+
		"\u0000\u0000\u0000\u015c\u015d\u0005\u001a\u0000\u0000\u015d\u015e\u0003"+
		"\u001c\u000e\u0000\u015e\u015f\u0003\u001c\u000e\u0000\u015f\u0160\u0006"+
		"\u0016\uffff\uffff\u0000\u0160\u0182\u0001\u0000\u0000\u0000\u0161\u0162"+
		"\u0005\u001d\u0000\u0000\u0162\u0163\u0003\u001c\u000e\u0000\u0163\u0164"+
		"\u0003\u001c\u000e\u0000\u0164\u0165\u0006\u0016\uffff\uffff\u0000\u0165"+
		"\u0182\u0001\u0000\u0000\u0000\u0166\u0167\u0005\u001b\u0000\u0000\u0167"+
		"\u0168\u0003\u001c\u000e\u0000\u0168\u0169\u0003\u001c\u000e\u0000\u0169"+
		"\u016a\u0006\u0016\uffff\uffff\u0000\u016a\u0182\u0001\u0000\u0000\u0000"+
		"\u016b\u016c\u0005\u001c\u0000\u0000\u016c\u016d\u0003\u001c\u000e\u0000"+
		"\u016d\u016e\u0003\u001c\u000e\u0000\u016e\u016f\u0006\u0016\uffff\uffff"+
		"\u0000\u016f\u0182\u0001\u0000\u0000\u0000\u0170\u0171\u0005\u001e\u0000"+
		"\u0000\u0171\u0172\u0003\u001c\u000e\u0000\u0172\u0173\u0003\u001c\u000e"+
		"\u0000\u0173\u0174\u0001\u0000\u0000\u0000\u0174\u0175\u0006\u0016\uffff"+
		"\uffff\u0000\u0175\u0182\u0001\u0000\u0000\u0000\u0176\u0177\u0005\u001f"+
		"\u0000\u0000\u0177\u0178\u0003\u001c\u000e\u0000\u0178\u0179\u0003\u001c"+
		"\u000e\u0000\u0179\u017a\u0006\u0016\uffff\uffff\u0000\u017a\u0182\u0001"+
		"\u0000\u0000\u0000\u017b\u017c\u0005\'\u0000\u0000\u017c\u0182\u0006\u0016"+
		"\uffff\uffff\u0000\u017d\u017e\u0005&\u0000\u0000\u017e\u017f\u0003\u001c"+
		"\u000e\u0000\u017f\u0180\u0006\u0016\uffff\uffff\u0000\u0180\u0182\u0001"+
		"\u0000\u0000\u0000\u0181\u012b\u0001\u0000\u0000\u0000\u0181\u0131\u0001"+
		"\u0000\u0000\u0000\u0181\u013b\u0001\u0000\u0000\u0000\u0181\u0145\u0001"+
		"\u0000\u0000\u0000\u0181\u0149\u0001\u0000\u0000\u0000\u0181\u014d\u0001"+
		"\u0000\u0000\u0000\u0181\u0152\u0001\u0000\u0000\u0000\u0181\u015c\u0001"+
		"\u0000\u0000\u0000\u0181\u0161\u0001\u0000\u0000\u0000\u0181\u0166\u0001"+
		"\u0000\u0000\u0000\u0181\u016b\u0001\u0000\u0000\u0000\u0181\u0170\u0001"+
		"\u0000\u0000\u0000\u0181\u0176\u0001\u0000\u0000\u0000\u0181\u017b\u0001"+
		"\u0000\u0000\u0000\u0181\u017d\u0001\u0000\u0000\u0000\u0182-\u0001\u0000"+
		"\u0000\u0000\u0183\u0184\u0005\u0001\u0000\u0000\u0184\u0195\u0006\u0017"+
		"\uffff\uffff\u0000\u0185\u0186\u00030\u0018\u0000\u0186\u0187\u0006\u0017"+
		"\uffff\uffff\u0000\u0187\u0195\u0001\u0000\u0000\u0000\u0188\u0189\u0003"+
		"2\u0019\u0000\u0189\u018a\u0006\u0017\uffff\uffff\u0000\u018a\u0195\u0001"+
		"\u0000\u0000\u0000\u018b\u018c\u00034\u001a\u0000\u018c\u018d\u0006\u0017"+
		"\uffff\uffff\u0000\u018d\u0195\u0001\u0000\u0000\u0000\u018e\u018f\u0003"+
		"6\u001b\u0000\u018f\u0190\u0006\u0017\uffff\uffff\u0000\u0190\u0195\u0001"+
		"\u0000\u0000\u0000\u0191\u0192\u00038\u001c\u0000\u0192\u0193\u0006\u0017"+
		"\uffff\uffff\u0000\u0193\u0195\u0001\u0000\u0000\u0000\u0194\u0183\u0001"+
		"\u0000\u0000\u0000\u0194\u0185\u0001\u0000\u0000\u0000\u0194\u0188\u0001"+
		"\u0000\u0000\u0000\u0194\u018b\u0001\u0000\u0000\u0000\u0194\u018e\u0001"+
		"\u0000\u0000\u0000\u0194\u0191\u0001\u0000\u0000\u0000\u0195/\u0001\u0000"+
		"\u0000\u0000\u0196\u0197\u0005.\u0000\u0000\u0197\u0198\u0003\u0004\u0002"+
		"\u0000\u0198\u0199\u0005/\u0000\u0000\u01991\u0001\u0000\u0000\u0000\u019a"+
		"\u019b\u0005,\u0000\u0000\u019b\u019c\u0003\u0004\u0002\u0000\u019c\u019d"+
		"\u0005-\u0000\u0000\u019d3\u0001\u0000\u0000\u0000\u019e\u019f\u00052"+
		"\u0000\u0000\u019f\u01a0\u0003\u0004\u0002\u0000\u01a0\u01a1\u00054\u0000"+
		"\u0000\u01a15\u0001\u0000\u0000\u0000\u01a2\u01a3\u00050\u0000\u0000\u01a3"+
		"\u01a4\u0003\u0004\u0002\u0000\u01a4\u01a5\u00051\u0000\u0000\u01a57\u0001"+
		"\u0000\u0000\u0000\u01a6\u01a7\u0005)\u0000\u0000\u01a7\u01a8\u0003\u0004"+
		"\u0002\u0000\u01a8\u01a9\u00053\u0000\u0000\u01a9\u01aa\u0006\u001c\uffff"+
		"\uffff\u0000\u01aa\u01b1\u0001\u0000\u0000\u0000\u01ab\u01ac\u0005*\u0000"+
		"\u0000\u01ac\u01ad\u0003\u0004\u0002\u0000\u01ad\u01ae\u0005+\u0000\u0000"+
		"\u01ae\u01af\u0006\u001c\uffff\uffff\u0000\u01af\u01b1\u0001\u0000\u0000"+
		"\u0000\u01b0\u01a6\u0001\u0000\u0000\u0000\u01b0\u01ab\u0001\u0000\u0000"+
		"\u0000\u01b19\u0001\u0000\u0000\u0000\u01b2\u01b3\u00057\u0000\u0000\u01b3"+
		";\u0001\u0000\u0000\u0000\u001fDLNi{\u0088\u008d\u0099\u00a2\u00aa\u00b7"+
		"\u00c5\u00ce\u00d9\u00de\u00fb\u00ff\u0102\u0106\u010a\u010c\u0116\u011b"+
		"\u0124\u0127\u0136\u0140\u0157\u0181\u0194\u01b0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}