from pymongo import MongoClient
from pygments.lexers import JavascriptLexer
from pygments import lex
from pygments.token import Token
from pygments.token import String, string_to_tokentype

#MONGOOOO
client = MongoClient('database:27017')
db = client['crawler']

#INICIO
print("********** JAVASCRIPT SOURCE CODE CRAWLER **********")
#CAMBIAR EL VALOR AL NOMBRE DEL ARCHIVO INICIAL DEL SOURCE CODE
archivoyes = "require"
#EL ROLLO DE LEXING ARCHIVO BASE
filepath = './src/'+ archivoyes +'.js'
fp = open(filepath).read()
#CODE INSERTION
lexer = JavascriptLexer()
tokens = lex(fp, lexer)
code = []
for x in tokens:
    code.append(x)

def indexing(code, colleccion, filepath):
        cont = 0
        # a iterar sobre el codigo para ver que es una variable. 
        for i in code:
            #DECLARACIONES DE VARIABLES Y FUNCIONES CON function
            if i[0] == string_to_tokentype('Token.Keyword.Declaration'):
                if i[1] == 'var':
                    document = {
                        "file":filepath,
                        "type":"var",
                        "name":str(code[cont + 2][1]),
                        "value":str(code[cont + 6][1])
                    }
                    colleccion.insert_one(document)
                elif i[1] == 'let':
                    document = {
                        "file":filepath,
                        "type":"let",
                        "name":str(code[cont + 2][1]),
                        "value":str(code[cont + 6][1])
                    }
                    colleccion.insert_one(document)
                elif i[1] == 'const':
                    document = {
                        "file":filepath,
                        "type":"const",
                        "name":code[cont + 2][1],
                        "value":code[cont + 6][1]
                    }
                    colleccion.insert_one(document)
                elif i[1] == 'function':
                    #REVISA SI TIENE NOMBRE PARA GUARDARLO. 
                    if code[cont + 1][1] != '(':
                        valor = code[cont + 2][1]
                        contador_aux = 2
                        params = []
                        #VERIFICAR PARAMETROS
                        while valor != ")":
                            if(contador_aux > 3 and contador_aux % 2 == 0):
                                params.append(valor)
                            contador_aux += 1
                            valor = code[cont + contador_aux][1]
                        document = {
                        "file":filepath,
                        "type":"function",
                        "name":str(code[cont + 2][1]),
                        "params":str(params)
                        }
                        colleccion.insert_one(document)
                    #PARA FUNCIONES SIN NOMBRE O DECLARADAS HOLA: FUNCTION()
                    else:
                        '''if code[cont - 2][1] == ":":
                            print("Name", code[cont - 3][1])
                        else:
                            print("No tiene nombre.")'''
                        valor = code[cont + 1][1]
                        contador_aux = 1
                        params = []
                        #VERIFICAR PARAMETROS
                        while valor != ")":
                            if(contador_aux > 1 and contador_aux % 2 == 0):
                                params.append(valor)
                            contador_aux += 1
                            valor = code[cont + contador_aux][1]
                        document = {
                        "file":filepath,
                        "type":"function",
                        "name":"No Name",
                        "params":str(params)
                        }
                        colleccion.insert_one(document)
        
            #CLASES y MODULOS
            elif i[0] == string_to_tokentype('Token.Keyword.Reserved'):
                if i[1] == 'class':
                    #VERIFICAR SI TIENE CONSTRUCTOR PARA LOS PARAMETROS
                    if code[cont + 6][1] == 'constructor':
                        add = 8
                        valortemp = code[cont + add][1]
                        params = []
                        while valortemp != ')':
                            if(add % 2 == 0):
                                params.append(valortemp)
                            valortemp = code[cont + add][1]
                            add += 1
                        document = {
                        "file":filepath,
                        "type":"class",
                        "name":str(code[cont + 2][1]),
                        "constructor": "true",
                        "parameters": str(params)
                        }
                        colleccion.insert_one(document)
                    elif code[cont + 10][1] == 'constructor':
                        add = 12
                        valortemp = code[cont + add][1]
                        params2 = []
                        while valortemp != ')':
                            valortemp = code[cont + add][1]
                            if(add % 2 == 0):
                                params2.append(valortemp)
                            add += 1
                        document = {
                        "file":filepath,
                        "type":"class child",
                        "name":str(code[cont + 2][1]),
                        "parent":str(code[cont + 4][1]),
                        "constructor": "true",
                        "parameters": str(params2)
                        }
                        colleccion.insert_one(document)
                elif i[1] == 'export':
                        document = {
                        "file":filepath,
                        "type":"export",
                        "name":str(code[cont + 4][1])
                        }
                        colleccion.insert_one(document)
                elif i[1] == 'import':
                    document = {
                        "file":filepath,
                        "type":"import",
                        "name":str(code[cont + 4][1])
                    }
                    colleccion.insert_one(document)
                
            #FUNCIONES DE TIPO () => {} NO VERIFICA NOMBRE
            elif i[0] == string_to_tokentype('Token.Punctuation'):
                if i[1] == '=>':
                    valor = code[cont][1]
                    contador_aux2 = 1
                    params = []
                    while valor != "(":
                        if(contador_aux2 > 1 and contador_aux2 % 2 != 0):
                            params.append(valor)
                        contador_aux2 += 1
                        valor = code[cont - contador_aux2][1]
                    document = {
                        "file":filepath,
                        "type":"arrow function",
                        "name":str(code[cont + 2][1]),
                        "params":str(params)
                    }
                    colleccion.insert_one(document)
          
            cont += 1

#VARIABLE GLOBAL PARA USO EN RECORRER
global recorrido, total
recorrido = []
total = []
#CREACION DEL SPANNING TREE DE ARCHIVOS
def recorrer(codigo):
    nombres = []
    contador = 0
    for i in codigo:
                if i[1] == 'require':
                        total.append(codigo[contador + 2][1])
                        path_modificado = codigo[contador + 2][1][1:-1]
                        nombres.append('./src/' + path_modificado + '.js')
                contador += 1
                for x in nombres:
                    filepath2 = x
                    fp2 = open(filepath2).read()
                    tokens2 = lex(fp2, lexer)
                    code2 = []
                    for y in tokens2:
                        code2.append(y)
                    
                    if x not in recorrido:
                        recorrer(code2)
                    recorrido.append(x)         

def indexado_general(coleccion):
    print("CAMINO EN EL ÁRBOL")
    for e in total:
        print(e[3:-1].upper(), "->")
        filepath = './src/'+ e[3:-1] + '.js'
        archivo = open(filepath).read()
        tokens = lex(archivo, lexer)
        source = []
        for x in tokens:
            source.append(x)
        indexing(source, coleccion, str(e[3:-1]))


#MAIN
colleccion_inicio = db['general']
#print(code)
recorrer(code)
indexing(code, colleccion_inicio, filepath)
indexado_general(colleccion_inicio)