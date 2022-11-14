# Generated from /home/gaston/Desktop/2022/2do cuatrimestre/DHS/DHS2022/src/main/python/iua/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#program.
    def visitProgram(self, ctx:compiladoresParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instructions.
    def visitInstructions(self, ctx:compiladoresParser.InstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruction.
    def visitInstruction(self, ctx:compiladoresParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#doWhileInstruction.
    def visitDoWhileInstruction(self, ctx:compiladoresParser.DoWhileInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#whileInstruction.
    def visitWhileInstruction(self, ctx:compiladoresParser.WhileInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ifInstruction.
    def visitIfInstruction(self, ctx:compiladoresParser.IfInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#forInstruction.
    def visitForInstruction(self, ctx:compiladoresParser.ForInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instructionBlock.
    def visitInstructionBlock(self, ctx:compiladoresParser.InstructionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comparison.
    def visitComparison(self, ctx:compiladoresParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#compare.
    def visitCompare(self, ctx:compiladoresParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#itop.
    def visitItop(self, ctx:compiladoresParser.ItopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#operation.
    def visitOperation(self, ctx:compiladoresParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expression.
    def visitExpression(self, ctx:compiladoresParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logicOr.
    def visitLogicOr(self, ctx:compiladoresParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lor.
    def visitLor(self, ctx:compiladoresParser.LorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logicAnd.
    def visitLogicAnd(self, ctx:compiladoresParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#land.
    def visitLand(self, ctx:compiladoresParser.LandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#t.
    def visitT(self, ctx:compiladoresParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#f.
    def visitF(self, ctx:compiladoresParser.FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaration.
    def visitDeclaration(self, ctx:compiladoresParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracionF.
    def visitDeclaracionF(self, ctx:compiladoresParser.DeclaracionFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declarationM.
    def visitDeclarationM(self, ctx:compiladoresParser.DeclarationMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignation.
    def visitAsignation(self, ctx:compiladoresParser.AsignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parameter.
    def visitParameter(self, ctx:compiladoresParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parameters.
    def visitParameters(self, ctx:compiladoresParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#init.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tipo.
    def visitTipo(self, ctx:compiladoresParser.TipoContext):
        return self.visitChildren(ctx)



del compiladoresParser