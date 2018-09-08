// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MPParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, INTTYPE=2, VOIDTYPE=3, REALTYPE=4, BOOLEANTYPE=5, STRINGTYPE=6, 
		ARRAYTYPE=7, LB=8, RB=9, LP=10, RP=11, LQ=12, RQ=13, SEMI=14, CM=15, EQ=16, 
		COL=17, DD=18, ADD=19, MUL=20, NOTEQ=21, LESSTN=22, LESSEQ=23, SUBNE=24, 
		DIVSI=25, GRETN=26, GREEQ=27, WS=28, BREAK=29, CONTINUE=30, FOR=31, TO=32, 
		DOWNTO=33, DO=34, AND=35, ID=36, INTLIT=37, REALLIT=38, BOOLLIT=39, ERROR_CHAR=40, 
		UNCLOSE_STRING=41, ILLEGAL_ESCAPE=42;
	public static final int
		RULE_program = 0, RULE_mptype = 1, RULE_body = 2, RULE_exp = 3, RULE_funcall = 4;
	public static final String[] ruleNames = {
		"program", "mptype", "body", "exp", "funcall"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'main'", "'int'", "'void'", "'real'", "'boolean'", "'string'", 
		"'array'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'='", 
		"':'", "'..'", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'>'", 
		"'>='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, "INTTYPE", "VOIDTYPE", "REALTYPE", "BOOLEANTYPE", "STRINGTYPE", 
		"ARRAYTYPE", "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", 
		"DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", "GRETN", 
		"GREEQ", "WS", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "AND", 
		"ID", "INTLIT", "REALLIT", "BOOLLIT", "ERROR_CHAR", "UNCLOSE_STRING", 
		"ILLEGAL_ESCAPE"
	};
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
	public String getGrammarFileName() { return "MP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MPParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public MptypeContext mptype() {
			return getRuleContext(MptypeContext.class,0);
		}
		public TerminalNode LB() { return getToken(MPParser.LB, 0); }
		public TerminalNode RB() { return getToken(MPParser.RB, 0); }
		public TerminalNode LP() { return getToken(MPParser.LP, 0); }
		public TerminalNode RP() { return getToken(MPParser.RP, 0); }
		public TerminalNode EOF() { return getToken(MPParser.EOF, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			mptype();
			setState(11);
			match(T__0);
			setState(12);
			match(LB);
			setState(13);
			match(RB);
			setState(14);
			match(LP);
			setState(16);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(15);
				body();
				}
			}

			setState(18);
			match(RP);
			setState(19);
			match(EOF);
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

	public static class MptypeContext extends ParserRuleContext {
		public TerminalNode INTTYPE() { return getToken(MPParser.INTTYPE, 0); }
		public TerminalNode VOIDTYPE() { return getToken(MPParser.VOIDTYPE, 0); }
		public MptypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mptype; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitMptype(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MptypeContext mptype() throws RecognitionException {
		MptypeContext _localctx = new MptypeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_mptype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(21);
			match(INTTYPE);
			setState(22);
			match(VOIDTYPE);
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

	public static class BodyContext extends ParserRuleContext {
		public FuncallContext funcall() {
			return getRuleContext(FuncallContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MPParser.SEMI, 0); }
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitBody(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			funcall();
			setState(25);
			match(SEMI);
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

	public static class ExpContext extends ParserRuleContext {
		public FuncallContext funcall() {
			return getRuleContext(FuncallContext.class,0);
		}
		public TerminalNode INTLIT() { return getToken(MPParser.INTLIT, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitExp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			funcall();
			setState(28);
			match(INTLIT);
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

	public static class FuncallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MPParser.ID, 0); }
		public TerminalNode LB() { return getToken(MPParser.LB, 0); }
		public TerminalNode RB() { return getToken(MPParser.RB, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public FuncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcall; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitFuncall(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FuncallContext funcall() throws RecognitionException {
		FuncallContext _localctx = new FuncallContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_funcall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(ID);
			setState(31);
			match(LB);
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(32);
				exp();
				}
			}

			setState(35);
			match(RB);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,(\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6$\n\6\3\6\3\6\3"+
		"\6\2\2\7\2\4\6\b\n\2\2\2$\2\f\3\2\2\2\4\27\3\2\2\2\6\32\3\2\2\2\b\35\3"+
		"\2\2\2\n \3\2\2\2\f\r\5\4\3\2\r\16\7\3\2\2\16\17\7\n\2\2\17\20\7\13\2"+
		"\2\20\22\7\f\2\2\21\23\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2"+
		"\2\24\25\7\r\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\7\4\2\2\30\31\7\5\2"+
		"\2\31\5\3\2\2\2\32\33\5\n\6\2\33\34\7\20\2\2\34\7\3\2\2\2\35\36\5\n\6"+
		"\2\36\37\7\'\2\2\37\t\3\2\2\2 !\7&\2\2!#\7\n\2\2\"$\5\b\5\2#\"\3\2\2\2"+
		"#$\3\2\2\2$%\3\2\2\2%&\7\13\2\2&\13\3\2\2\2\4\22#";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}