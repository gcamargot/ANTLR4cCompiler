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
    idList = dict()
    initList = []
    paramList = dict()
    contador = 0


    # Enter a parse tree produced by compiladoresParser#program.
    def enterProgram(self, ctx:compiladoresParser.ProgramContext):
        self.f = open("./output/tablaSimbolos.txt", "w")

    # Exit a parse tree produced by compiladoresParser#program.
    def exitProgram(self, ctx:compiladoresParser.ProgramContext):
        if(self.contador >= 0):
            self.f.write("Contexto: ")
            self.f.write(str(self.contador))
            self.f.write("\n")
            for each in self.tabla.ts[-1]:
                self.f.write(str(self.tabla.ts[-1][each].getType()) + " ")
                self.f.write(str(each))
                self.f.write("("+ self.tabla.ts[-1][each].getKind() + "), ")
                
            self.f.write("\n")
            self.f.write("\n")
        self.f.close()
        self.tabla.del_context()


        # Enter a parse tree produced by compiladoresParser#instruction.
    def enterInstructionBlock(self, ctx:compiladoresParser.InstructionContext):
        self.tabla.add_context()
        self.contador+=1

        if self.paramList:
            for temp in self.paramList.keys():
                if not self.tabla.findKey(temp):
                    self.tabla.ts[-1][temp] = variable(temp, self.paramList[temp])
                    
                else:
                    print("La variable \"" + temp + "\" ya existe en este contexto")
        self.paramList.clear()


    # Exit a parse tree produced by compiladoresParser#Instruction.
    def exitInstructionBlock(self, ctx:compiladoresParser.InstructionContext):
        if(self.tabla.ts[-1]):
            self.f.write("Contexto: ")
            self.f.write(str(self.contador))
            self.f.write("\n")
            for each in self.tabla.ts[-1]:
                self.f.write(str(self.tabla.ts[-1][each].getType()) + " ")
                self.f.write(str(each))
                self.f.write("("+ self.tabla.ts[-1][each].getKind() + "), ")
                
            self.f.write("\n")
        else:
            self.f.write("Contexto: ")
            self.f.write(str(self.contador))
            self.f.write("\n")
            self.f.write("Vacio")
            self.f.write("\n")
        self.contador-=1
    
        self.tabla.del_context()
        

    def enterDoWhileInstruction(self, ctx:compiladoresParser.DoWhileInstructionContext):
        pass
    def enterForInstruction(self, ctx:compiladoresParser.ForInstructionContext):
        pass
    def exitForInstruction(self, ctx:compiladoresParser.ForInstructionContext):
        pass
        
    # Exit a parse tree produced by compiladoresParser#WhileInstructionContext.
    def exitDoWhileInstruction(self, ctx:compiladoresParser.DoWhileInstructionContext):
        pass
        
        # Enter a parse tree produced by compiladoresParser#WhileInstruction.
    def enterWhileInstruction(self, ctx:compiladoresParser.WhileInstructionContext):
        pass
        
    # Exit a parse tree produced by compiladoresParser#WhileInstruction.
    def exitWhileInstruction(self, ctx:compiladoresParser.WhileInstructionContext):
        pass
        
    def enterIfInstruction(self, ctx:compiladoresParser.IfInstructionContext):
        pass
    def exitIfInstruction(self, ctx:compiladoresParser.IfInstructionContext):
        pass

    # Enter a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass
    
    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass
    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    def enterDeclaration(self, ctx:compiladoresParser.DeclarationContext):
        pass
    
    def exitDeclaration(self, ctx:compiladoresParser.DeclarationContext):
        tipo = str(ctx.getChild(0).getChild(0))
     
        for temp in self.idList.keys():
            if not self.tabla.findKey(temp):
                if self.idList[temp] == "variable":
                    self.tabla.ts[-1][temp] = variable(temp, tipo)
                if self.idList[temp] == "function":
                    self.tabla.ts[0][temp] = funcion(temp, tipo, self.paramList)
                
            else:
                print("WARNING: La variable " + str(temp) + " ya existe.")
        
        for temp in self.initList:
            if self.tabla.findKey(temp):

                for context in self.tabla.ts:
                    if(temp in context):
                        if(not context[temp].initialized):
                            context[temp].initialized = True

        
            

        self.idList.clear()
        self.initList = []
        self.struct = 0


    def enterAsignation(self, ctx:compiladoresParser.AsignationContext):
        pass

    def exitAsignation(self, ctx:compiladoresParser.AsignationContext):
        
        name = ctx.getChild(0)

        if self.tabla.findKey(str(name)):
            self.initList.append(str(name))
        else:
            print("ERROR: La variable \"" + str(name) + "\" no esta declarada") 

    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        name = str(ctx.getChild(0))
        self.idList[name] = "variable"
        self.initList.append(name)


      # Enter a parse tree produced by compiladoresParser#declarationM.
    def enterDeclarationM(self, ctx:compiladoresParser.DeclarationMContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declarationM.
    def exitDeclarationM(self, ctx:compiladoresParser.DeclarationMContext):
        name = str(ctx.getChild(0))
        if name[0].isalpha() :
            self.idList[str(name)] = "variable"


    # Enter a parse tree produced by compiladoresParser#declaracionF.
    def enterDeclaracionF(self, ctx:compiladoresParser.DeclaracionFContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracionF.
    def exitDeclaracionF(self, ctx:compiladoresParser.DeclaracionFContext):
        name = str(ctx.getChild(0))
        self.idList[name] = "function"

    # Enter a parse tree produced by compiladoresParser#parameter.
    def enterParameter(self, ctx:compiladoresParser.ParameterContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parameter.
    def exitParameter(self, ctx:compiladoresParser.ParameterContext):
        name = str(ctx.getChild(1))
        type = str(ctx.getChild(0).getChild(0))
        if not self.tabla.findKey(name):
            self.paramList[name] = type  

    
        