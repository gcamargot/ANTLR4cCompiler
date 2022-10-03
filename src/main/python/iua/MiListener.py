from traceback import print_tb
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser
from tablaValores import tablaValores


# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MiListener(ParseTreeListener):

    tabla = tablaValores();

    # Enter a parse tree produced by compiladoresParser#program.
    def enterProgram(self, ctx:compiladoresParser.ProgramContext):
        print ("ProgramContext IN -> |" + ctx.getText() + "|")
        self.tabla.add_context();


    # Exit a parse tree produced by compiladoresParser#program.
    def exitProgram(self, ctx:compiladoresParser.ProgramContext):
        print ("ProgramContext OUT -> |" + ctx.getText() + "|")
        self.tabla.del_context();


        # Enter a parse tree produced by compiladoresParser#instruction.
    def enterInstruction(self, ctx:compiladoresParser.InstructionContext):
        print ("InstructionContext IN -> {" + ctx.getText() + "}")
        self.tabla.add_context();


    # Exit a parse tree produced by compiladoresParser#Instruction.
    def exitInstruction(self, ctx:compiladoresParser.InstructionContext):
        print ("InstructionContext OUT -> {" + ctx.getText() + "}")
        print("Tiene " + str(ctx.getChildCount()) + " hijos")
        self.tabla.del_context();

    def enterDoWhileInstruction(self, ctx:compiladoresParser.DoWhileInstructionContext):
        print ("DoWhileInstContext IN -> |" + ctx.getText() + "|")
        self.tabla.add_context();


    # Exit a parse tree produced by compiladoresParser#WhileInstructionContext.
    def exitDoWhileInstruction(self, ctx:compiladoresParser.DoWhileInstructionContext):
        print ("DoWhileInstContext OUT -> |" + ctx.getText() + "|")
        self.tabla.del_context();

        # Enter a parse tree produced by compiladoresParser#WhileInstruction.
    def enterWhileInstruction(self, ctx:compiladoresParser.WhileInstructionContext):
        print ("WhileInstContext IN -> |" + ctx.getText() + "|")
        self.tabla.add_context();


    # Exit a parse tree produced by compiladoresParser#WhileInstruction.
    def exitWhileInstruction(self, ctx:compiladoresParser.WhileInstructionContext):
        print ("WhileInstContext OUT -> |" + ctx.getText() + "|")
        self.tabla.del_context();

    def enterIfInstruction(self, ctx:compiladoresParser.IfInstructionContext):
        print("IfInstruction IN -> (" + ctx.getText() + ")")
        self.tabla.add_context();
    def exitIfInstruction(self, ctx:compiladoresParser.IfInstructionContext):
        print("IfInstruction OUT -> (" + ctx.getText() + ")")
        self.tabla.del_context();

    

    # Enter a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        print ("Term tiene " + str(ctx.getChildCount()) + " hijos")
        print ("Term -> text |" + ctx.getText() + "|")
    
    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        print ("Factor IN -> |" + ctx.getText() + "|")

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        print ("Factor OUT -> |" + ctx.getText() + "|")

    def enterAsignation(self, ctx:compiladoresParser.AsignationContext):
        print("hola soy una asignacion")
    
    def exitAsignation(self, ctx:compiladoresParser.AsignationContext):
        temp = str(ctx.getChild(0))
        print("text:" + temp)
        self.tabla.ts[-1][temp.name] = temp

        