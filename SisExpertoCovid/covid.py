import termcolor
from logic import *

prueba = Symbol("Prueba")
fiebre = Symbol("Fiebre")
tos = Symbol("Tos")
disnea = Symbol("Disnea")
estornudos = Symbol("Estornudos") #Variante Delta
p_olfato_gusto = Symbol("Perdida de olfato y gusto") #Variante Delta
dolor_cabeza = Symbol("Dolor de cabeza")#Variante Ómicron
sec_nasal = Symbol("Secreción nasal")#Variante Ómicron
sud_nocturnos = Symbol("Sudores nocturnos")#Variante Ómicron
sintomas = [prueba, fiebre, tos, disnea, estornudos, p_olfato_gusto, dolor_cabeza, sec_nasal, sud_nocturnos]

covid19 = Symbol("Covid")
covid_asintomatico = Symbol("Asintomatico")
delta = Symbol("Covid - Variante Delta")
omicron = Symbol("Covid - Variante Ómicron")
enfRespiratoria = Symbol("Enfermedad Respiratoria")
sano = Symbol("Sano")
enfermedad = Symbol("Enfermedad desconocida")
estado_Salud = [covid19, covid_asintomatico, delta, omicron, enfRespiratoria, sano, enfermedad]

symbols = sintomas + estado_Salud

def check_knowledge(knowledge):
    i = 0;
    for symbol in symbols:
    
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: SI", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: NO")

knowledge = And(
    Implication(And(Or(fiebre, tos, disnea), (prueba)), covid19),
    Implication(And(Not(fiebre), Not(tos), Not(disnea), Not(estornudos), Not(p_olfato_gusto), Not(dolor_cabeza), Not(sec_nasal), Not(sud_nocturnos), prueba), covid_asintomatico),
    Implication(And(fiebre, tos, estornudos, p_olfato_gusto, prueba), delta),
    Implication(And(fiebre, dolor_cabeza,sec_nasal, sud_nocturnos, prueba), omicron),
    Implication(And(Or(tos, disnea), Not(prueba)), enfRespiratoria),
    Implication(And(Not(fiebre), Not(tos), Not(disnea), Not(estornudos), Not(p_olfato_gusto), Not(dolor_cabeza), Not(sec_nasal), Not(sud_nocturnos), Not(prueba)), sano),
    Implication(And(Not(prueba), Or(fiebre, sec_nasal, sud_nocturnos, dolor_cabeza, estornudos)), enfermedad),
    Not(And(covid19, covid_asintomatico, delta, omicron, enfRespiratoria, sano, enfermedad))
)
"""
#Covid19-Original
knowledge.add(And(
    (fiebre), Not(tos), Not(disnea), (prueba)
))
"""

#Covid Asintomático
knowledge.add(And(
    Not(fiebre), Not(tos), Not(disnea), Not(estornudos), Not(p_olfato_gusto), Not(dolor_cabeza), Not(sec_nasal), Not(sud_nocturnos), prueba
))


"""
#Variante Delta
knowledge.add(And(
    fiebre, tos, estornudos, p_olfato_gusto, prueba
))
"""
"""
#Variante Ómicron
knowledge.add(And(
    fiebre, dolor_cabeza,sec_nasal, sud_nocturnos, prueba
))
"""
"""
#Enfermedad Respiratoria
knowledge.add(And(
    tos, Not(prueba)
))
"""
"""
#Sano
knowledge.add(And(
    Not(fiebre), Not(tos), Not(disnea), Not(estornudos), Not(p_olfato_gusto), Not(dolor_cabeza), Not(sec_nasal), Not(sud_nocturnos), Not(prueba)
))
"""
"""
#Enfermedad desconocida
knowledge.add(And(
    (fiebre), Not(tos), Not(disnea), Not(prueba)
))
"""
check_knowledge(knowledge)