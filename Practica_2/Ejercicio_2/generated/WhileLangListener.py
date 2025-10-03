# Generated from WhileLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete listener for a parse tree produced by WhileLangParser.
class WhileLangListener(ParseTreeListener):

    # Enter a parse tree produced by WhileLangParser#program.
    def enterProgram(self, ctx:WhileLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by WhileLangParser#program.
    def exitProgram(self, ctx:WhileLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by WhileLangParser#statement.
    def enterStatement(self, ctx:WhileLangParser.StatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#statement.
    def exitStatement(self, ctx:WhileLangParser.StatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#assignment.
    def enterAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by WhileLangParser#assignment.
    def exitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by WhileLangParser#whileStatement.
    def enterWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#whileStatement.
    def exitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ifStatement.
    def enterIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ifStatement.
    def exitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#breakStatement.
    def enterBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#breakStatement.
    def exitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#continueStatement.
    def enterContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#continueStatement.
    def exitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#condition.
    def enterCondition(self, ctx:WhileLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by WhileLangParser#condition.
    def exitCondition(self, ctx:WhileLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by WhileLangParser#stringExpr.
    def enterStringExpr(self, ctx:WhileLangParser.StringExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#stringExpr.
    def exitStringExpr(self, ctx:WhileLangParser.StringExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#numberExpr.
    def enterNumberExpr(self, ctx:WhileLangParser.NumberExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#numberExpr.
    def exitNumberExpr(self, ctx:WhileLangParser.NumberExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:WhileLangParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:WhileLangParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#arithmeticExpr.
    def enterArithmeticExpr(self, ctx:WhileLangParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#arithmeticExpr.
    def exitArithmeticExpr(self, ctx:WhileLangParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#parenExpr.
    def enterParenExpr(self, ctx:WhileLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#parenExpr.
    def exitParenExpr(self, ctx:WhileLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#idExpr.
    def enterIdExpr(self, ctx:WhileLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#idExpr.
    def exitIdExpr(self, ctx:WhileLangParser.IdExprContext):
        pass



del WhileLangParser