
from lexer import Lexer
from parser import Parser 
from interpreter import Interpreter
from context import Context
from SymbolTable import SymbolTable 
from values import Number


##### run #########
#################

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number(0))


##################s
### genarte tokens####

def run (fn,text):
    lexer = Lexer(fn,text)
    tokens , error = lexer.make_tokens()
    if error : return None , error

############################
## ast   ###########
    parser= Parser(tokens)
    ast = parser.parse()
    if ast.error : return None ,ast.error

###############################
# run program
    interpreter = Interpreter()
    context = Context('<program>') 
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value , result.error





