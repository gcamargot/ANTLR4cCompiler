# Generated from /home/gaston/Desktop/2022/2do cuatrimestre/DHS/DHS2022/src/main/python/iua/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class MiVisitor(ParseTreeVisitor):

    contador = 0
    lastLabel = [0]
    temporal = 0
    rollback = False


    # Visit a parse tree produced by compiladoresParser#program.
    def visitProgram(self, ctx:compiladoresParser.ProgramContext):
        self.f = open("CodigoIntermedio.txt", "w")
        self.f.write("jump main \n")
        
        self.visitChildren(ctx)

        self.f.write("label back" + str(self.contador))
        self.f.close()



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
        
        self.contador = self.contador + 1
        self.lastLabel.append(self.contador)
        
        self.f.write("ifnot " + ctx.getChild(2).getText() + " jump else" + str(self.contador) + "\n")
        self.visitChildren(ctx.getChild(4))
        self.f.write("jump endif" + str(self.lastLabel[-1]) + "\n")
        self.f.write("label else" + str(self.lastLabel[-1]) + "\n")
        if(ctx.getChild(5)):
            self.visitChildren(ctx.getChild(5))
        self.f.write("label endif" + str(self.lastLabel[-1]) + "\n")
        self.lastLabel.pop()

    

    def visitElseInstruction(self, ctx:compiladoresParser.ElseInstructionContext):
        self.visitChildren(ctx)
        self.f.write("label endif" + str(self.lastLabel[-1]) + "\n")


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
        self.visitChildren(ctx)
        if(ctx.getChildCount()):
            self.f.write("t" + str(self.temporal) + "=" + ctx.getChild(0).getText() + "\n")
        self.rollback = True
        self.temporal = 0
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
        self.visitChildren(ctx)
        if(ctx.getChildCount() and not self.rollback):
            self.f.write("t" + str(self.temporal) + "=" + ctx.getChild(1).getText() + "\n")
            self.temporal = self.temporal + 1
        if(self.rollback):
            if(ctx.getChildCount()):
                self.f.write("t" + str(self.temporal+1) + "=" + "t" + str(self.temporal+1))
                self.f.write(ctx.getChild(0).getText() + "t" + str(self.temporal) + "\n")
                self.temporal = self.temporal +1
        


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
        self.f.write("Label " + str(ctx.getChild(0)) + "\n")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declarationM.
    def visitDeclarationM(self, ctx:compiladoresParser.DeclarationMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignation.
    def visitAsignation(self, ctx:compiladoresParser.AsignationContext):
        self.visitChildren(ctx)
        self.f.write(str(ctx.getChild(0)) + "= t" + str(self.temporal) + "\n")
        self.temporal = 0
        


    # Visit a parse tree produced by compiladoresParser#parameter.
    def visitParameter(self, ctx:compiladoresParser.ParameterContext):
        self.f.write("pop " + str(ctx.getChild(1)) + "\n")
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parameters.
    def visitParameters(self, ctx:compiladoresParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        self.visitChildren(ctx)
        self.f.write(ctx.getChild(0).getText() + ctx.getChild(1).getText() + "t" + str(self.temporal) +  "\n")
        self.rollback = False
        self.temporal = 0
        


    # Visit a parse tree produced by compiladoresParser#tipo.
    def visitTipo(self, ctx:compiladoresParser.TipoContext):
        return self.visitChildren(ctx)

    def visitAsignationF(self, ctx:compiladoresParser.AsignationFContext):
        self.visitChildren(ctx)
        label = str(0)
        if(self.lastLabel):
            label = str(self.lastLabel[-1])
            self.lastLabel.pop()
        
        
        self.f.write("jump " + str(ctx.getChild(2))+ "\n")
        self.f.write("label back" + label + "\n")
        self.f.write("pop " + str(ctx.getChild(0))+ "\n")
        
    
    def visitParametrosF(self, ctx:compiladoresParser.ParametrosFContext):
        self.f.write("push " + str(ctx.getChild(0))+ "\n")
        return self.visitChildren(ctx)

    def visitReturnInstruction(self, ctx:compiladoresParser.ReturnInstructionContext):
        self.f.write("push " + ctx.getChild(1).getChild(0).getText() + "\n")
        self.f.write("jump back" + str(self.contador) + "\n")

del compiladoresParser