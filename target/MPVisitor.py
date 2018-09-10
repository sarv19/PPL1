# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#manydeclares.
    def visitManydeclares(self, ctx:MPParser.ManydeclaresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primtype.
    def visitPrimtype(self, ctx:MPParser.PrimtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrtype.
    def visitArrtype(self, ctx:MPParser.ArrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr1.
    def visitExpr1(self, ctx:MPParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr2.
    def visitExpr2(self, ctx:MPParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr3.
    def visitExpr3(self, ctx:MPParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr4.
    def visitExpr4(self, ctx:MPParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr5.
    def visitExpr5(self, ctx:MPParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr6.
    def visitExpr6(self, ctx:MPParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr7.
    def visitExpr7(self, ctx:MPParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varde.
    def visitVarde(self, ctx:MPParser.VardeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vartype.
    def visitVartype(self, ctx:MPParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#idlist.
    def visitIdlist(self, ctx:MPParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcde.
    def visitFuncde(self, ctx:MPParser.FuncdeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcde1.
    def visitFuncde1(self, ctx:MPParser.Funcde1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paralist.
    def visitParalist(self, ctx:MPParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parade.
    def visitParade(self, ctx:MPParser.ParadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compostate.
    def visitCompostate(self, ctx:MPParser.CompostateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statelist.
    def visitStatelist(self, ctx:MPParser.StatelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procede.
    def visitProcede(self, ctx:MPParser.ProcedeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procede1.
    def visitProcede1(self, ctx:MPParser.Procede1Context):
        return self.visitChildren(ctx)



del MPParser