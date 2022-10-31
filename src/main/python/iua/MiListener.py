from curses.ascii import isalpha
from traceback import print_tb
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser
from tablaValores import *


# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MiListener(ParseTreeListener):

    tabla = tablaValores();
    idList = []
    initList = []

    # Enter a parse tree produced by compiladoresParser#program.
    def enterProgram(self, ctx:compiladoresParser.ProgramContext):
        print ("ProgramContext IN -> |" + ctx.getText() + "|")


    # Exit a parse tree produced by compiladoresParser#program.
    def exitProgram(self, ctx:compiladoresParser.ProgramContext):
        print ("ProgramContext OUT -> |" + ctx.getText() + "|")
        self.tabla.del_context();


        # Enter a parse tree produced by compiladoresParser#instruction.
    def enterInstructionBlock(self, ctx:compiladoresParser.InstructionContext):
        print ("InstructionBlock IN -> {" + ctx.getText() + "}")
        self.tabla.add_context();


    # Exit a parse tree produced by compiladoresParser#Instruction.
    def exitInstructionBock(self, ctx:compiladoresParser.InstructionContext):
        print ("InstructionBlock OUT -> {" + ctx.getText() + "}")
        print("Tiene " + str(ctx.getChildCount()) + " hijos")
        self.tabla.del_context();

    def enterDoWhileInstruction(self, ctx:compiladoresParser.DoWhileInstructionContext):
        print ("DoWhileInstContext IN -> |" + ctx.getText() + "|")
        


    # Exit a parse tree produced by compiladoresParser#WhileInstructionContext.
    def exitDoWhileInstruction(self, ctx:compiladoresParser.DoWhileInstructionContext):
        print ("DoWhileInstContext OUT -> |" + ctx.getText() + "|")
        

        # Enter a parse tree produced by compiladoresParser#WhileInstruction.
    def enterWhileInstruction(self, ctx:compiladoresParser.WhileInstructionContext):
        print ("WhileInstContext IN -> |" + ctx.getText() + "|")
        


    # Exit a parse tree produced by compiladoresParser#WhileInstruction.
    def exitWhileInstruction(self, ctx:compiladoresParser.WhileInstructionContext):
        print ("WhileInstContext OUT -> |" + ctx.getText() + "|")
        

    def enterIfInstruction(self, ctx:compiladoresParser.IfInstructionContext):
        print("IfInstruction IN -> (" + ctx.getText() + ")")
    def exitIfInstruction(self, ctx:compiladoresParser.IfInstructionContext):
        print("IfInstruction OUT -> (" + ctx.getText() + ")")

    

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

    def enterDeclaration(self, ctx:compiladoresParser.DeclarationContext):
        print("Declaracion IN")
    
    def exitDeclaration(self, ctx:compiladoresParser.DeclarationContext):
        tipo = ctx.getChild(0).getChild(0)
        for temp in self.idList:
            if not self.tabla.findKey(temp):
                self.tabla.ts[-1][temp] = variable(temp, tipo)
            else:
                print("La variable " + str(temp) + " ya existe.")
        for temp in self.initList:
            if self.tabla.findKey(temp):
                self.tabla.ts[-1][temp].initialized = True
                print(temp + " esta inicializada")

        self.idList = []
        self.initList = []



    def enterAsignation(self, ctx:compiladoresParser.AsignationContext):
        print("Asignation in:")

    def exitAsignation(self, ctx:compiladoresParser.AsignationContext):
        print("Asignation out:")
        
        name = ctx.getChild(0)

        if self.tabla.findKey(str(name)):
            self.tabla.ts[-1][str(name)].initialized = True
        else:
            print("Error: La variable \"" + str(name) + "\" no esta declarada") 

    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        print("Init in")

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        name = str(ctx.getChild(0))
        self.idList.append(name)   
        self.initList.append(name)
        print("Init exit")


      # Enter a parse tree produced by compiladoresParser#declarationM.
    def enterDeclarationM(self, ctx:compiladoresParser.DeclarationMContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declarationM.
    def exitDeclarationM(self, ctx:compiladoresParser.DeclarationMContext):
        name = str(ctx.getChild(0))
        
        if name[0].isalpha() :
            self.idList.append(str(name))


        
        
        