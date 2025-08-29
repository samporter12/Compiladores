# Generated from SwitchLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,3,0,17,8,0,4,0,19,8,0,11,0,12,0,20,1,0,1,0,1,1,1,1,1,1,
        3,1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,5,2,39,8,2,10,
        2,12,2,42,9,2,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,5,2,51,8,2,10,2,12,
        2,54,9,2,1,2,3,2,57,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,66,8,3,5,
        3,68,8,3,10,3,12,3,71,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,90,8,6,1,6,1,6,1,6,1,6,1,6,1,6,
        5,6,98,8,6,10,6,12,6,101,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,3,1,
        0,13,16,1,0,11,12,1,0,9,10,110,0,18,1,0,0,0,2,27,1,0,0,0,4,29,1,
        0,0,0,6,58,1,0,0,0,8,74,1,0,0,0,10,78,1,0,0,0,12,89,1,0,0,0,14,16,
        3,2,1,0,15,17,5,17,0,0,16,15,1,0,0,0,16,17,1,0,0,0,17,19,1,0,0,0,
        18,14,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,22,1,
        0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,28,3,4,2,0,25,28,3,6,3,0,26,
        28,3,10,5,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,
        0,29,30,5,1,0,0,30,31,5,4,0,0,31,32,3,8,4,0,32,33,5,5,0,0,33,40,
        5,6,0,0,34,36,3,2,1,0,35,37,5,17,0,0,36,35,1,0,0,0,36,37,1,0,0,0,
        37,39,1,0,0,0,38,34,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,
        0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,56,5,7,0,0,44,45,5,3,0,0,45,
        52,5,6,0,0,46,48,3,2,1,0,47,49,5,17,0,0,48,47,1,0,0,0,48,49,1,0,
        0,0,49,51,1,0,0,0,50,46,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,
        1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,57,5,7,0,0,56,44,1,0,0,0,
        56,57,1,0,0,0,57,5,1,0,0,0,58,59,5,2,0,0,59,60,5,4,0,0,60,61,3,12,
        6,0,61,62,5,5,0,0,62,69,5,6,0,0,63,65,3,2,1,0,64,66,5,17,0,0,65,
        64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,63,1,0,0,0,68,71,1,0,0,
        0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,
        5,7,0,0,73,7,1,0,0,0,74,75,5,18,0,0,75,76,7,0,0,0,76,77,5,19,0,0,
        77,9,1,0,0,0,78,79,5,18,0,0,79,80,5,8,0,0,80,81,3,12,6,0,81,11,1,
        0,0,0,82,83,6,6,-1,0,83,90,5,19,0,0,84,90,5,18,0,0,85,86,5,4,0,0,
        86,87,3,12,6,0,87,88,5,5,0,0,88,90,1,0,0,0,89,82,1,0,0,0,89,84,1,
        0,0,0,89,85,1,0,0,0,90,99,1,0,0,0,91,92,10,5,0,0,92,93,7,1,0,0,93,
        98,3,12,6,6,94,95,10,4,0,0,95,96,7,2,0,0,96,98,3,12,6,5,97,91,1,
        0,0,0,97,94,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,
        100,13,1,0,0,0,101,99,1,0,0,0,13,16,20,27,36,40,48,52,56,65,69,89,
        97,99
    ]

class SwitchLangParser ( Parser ):

    grammarFileName = "SwitchLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'switch'", "'else'", "'('", "')'", 
                     "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'>'", 
                     "'<'", "'=='", "'!='", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "SWITCH", "ELSE", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "ASSIGN", "PLUS", "MINUS", "MUL", 
                      "DIV", "GT", "LT", "EQ", "NEQ", "SEMI", "ID", "INT", 
                      "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_ifElseStmt = 2
    RULE_switchStmt = 3
    RULE_condicion = 4
    RULE_asignacion = 5
    RULE_expresion = 6

    ruleNames =  [ "programa", "sentencia", "ifElseStmt", "switchStmt", 
                   "condicion", "asignacion", "expresion" ]

    EOF = Token.EOF
    IF=1
    SWITCH=2
    ELSE=3
    LPAREN=4
    RPAREN=5
    LBRACE=6
    RBRACE=7
    ASSIGN=8
    PLUS=9
    MINUS=10
    MUL=11
    DIV=12
    GT=13
    LT=14
    EQ=15
    NEQ=16
    SEMI=17
    ID=18
    INT=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SwitchLangParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SEMI)
            else:
                return self.getToken(SwitchLangParser.SEMI, i)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = SwitchLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.sentencia()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 15
                    self.match(SwitchLangParser.SEMI)


                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 262150) != 0)):
                    break

            self.state = 22
            self.match(SwitchLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifElseStmt(self):
            return self.getTypedRuleContext(SwitchLangParser.IfElseStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(SwitchLangParser.SwitchStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(SwitchLangParser.AsignacionContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = SwitchLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.ifElseStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.switchStmt()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.asignacion()
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


    class IfElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SwitchLangParser.RULE_ifElseStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseContext(IfElseStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.IfElseStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(SwitchLangParser.IF, 0)
        def LPAREN(self):
            return self.getToken(SwitchLangParser.LPAREN, 0)
        def condicion(self):
            return self.getTypedRuleContext(SwitchLangParser.CondicionContext,0)

        def RPAREN(self):
            return self.getToken(SwitchLangParser.RPAREN, 0)
        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.LBRACE)
            else:
                return self.getToken(SwitchLangParser.LBRACE, i)
        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.RBRACE)
            else:
                return self.getToken(SwitchLangParser.RBRACE, i)
        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.SentenciaContext,i)

        def ELSE(self):
            return self.getToken(SwitchLangParser.ELSE, 0)
        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SEMI)
            else:
                return self.getToken(SwitchLangParser.SEMI, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)



    def ifElseStmt(self):

        localctx = SwitchLangParser.IfElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifElseStmt)
        self._la = 0 # Token type
        try:
            localctx = SwitchLangParser.IfElseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(SwitchLangParser.IF)
            self.state = 30
            self.match(SwitchLangParser.LPAREN)
            self.state = 31
            self.condicion()
            self.state = 32
            self.match(SwitchLangParser.RPAREN)
            self.state = 33
            self.match(SwitchLangParser.LBRACE)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262150) != 0):
                self.state = 34
                self.sentencia()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 35
                    self.match(SwitchLangParser.SEMI)


                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(SwitchLangParser.RBRACE)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 44
                self.match(SwitchLangParser.ELSE)
                self.state = 45
                self.match(SwitchLangParser.LBRACE)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262150) != 0):
                    self.state = 46
                    self.sentencia()
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 47
                        self.match(SwitchLangParser.SEMI)


                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 55
                self.match(SwitchLangParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(SwitchLangParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(SwitchLangParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(SwitchLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(SwitchLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SwitchLangParser.RBRACE, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SEMI)
            else:
                return self.getToken(SwitchLangParser.SEMI, i)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)




    def switchStmt(self):

        localctx = SwitchLangParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(SwitchLangParser.SWITCH)
            self.state = 59
            self.match(SwitchLangParser.LPAREN)
            self.state = 60
            self.expresion(0)
            self.state = 61
            self.match(SwitchLangParser.RPAREN)
            self.state = 62
            self.match(SwitchLangParser.LBRACE)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262150) != 0):
                self.state = 63
                self.sentencia()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 64
                    self.match(SwitchLangParser.SEMI)


                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(SwitchLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SwitchLangParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionSimpleContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.CondicionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)
        def INT(self):
            return self.getToken(SwitchLangParser.INT, 0)
        def GT(self):
            return self.getToken(SwitchLangParser.GT, 0)
        def LT(self):
            return self.getToken(SwitchLangParser.LT, 0)
        def EQ(self):
            return self.getToken(SwitchLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(SwitchLangParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionSimple" ):
                listener.enterCondicionSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionSimple" ):
                listener.exitCondicionSimple(self)



    def condicion(self):

        localctx = SwitchLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            localctx = SwitchLangParser.CondicionSimpleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(SwitchLangParser.ID)
            self.state = 75
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 76
            self.match(SwitchLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SwitchLangParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(SwitchLangParser.ASSIGN, 0)
        def expresion(self):
            return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def asignacion(self):

        localctx = SwitchLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            localctx = SwitchLangParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(SwitchLangParser.ID)
            self.state = 79
            self.match(SwitchLangParser.ASSIGN)
            self.state = 80
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SwitchLangParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,i)

        def MUL(self):
            return self.getToken(SwitchLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(SwitchLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,i)

        def PLUS(self):
            return self.getToken(SwitchLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SwitchLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(SwitchLangParser.LPAREN, 0)
        def expresion(self):
            return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,0)

        def RPAREN(self):
            return self.getToken(SwitchLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SwitchLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SwitchLangParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = SwitchLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 83
                self.match(SwitchLangParser.INT)
                pass
            elif token in [18]:
                localctx = SwitchLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(SwitchLangParser.ID)
                pass
            elif token in [4]:
                localctx = SwitchLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(SwitchLangParser.LPAREN)
                self.state = 86
                self.expresion(0)
                self.state = 87
                self.match(SwitchLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 97
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = SwitchLangParser.MulDivContext(self, SwitchLangParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 91
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 92
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 93
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = SwitchLangParser.AddSubContext(self, SwitchLangParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 94
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 95
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 96
                        self.expresion(5)
                        pass

             
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




