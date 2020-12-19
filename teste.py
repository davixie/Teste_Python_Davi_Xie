## Teste de Python - Navi
## Candidato: Davi Xie

import math

# ------------------------------------
# ------------------------------------
# Questão 1

def questao1():
    mult1 = 49
    mult2 = 37
    mult3 = 2

    start = 1
    end = 5000000

    cont = 0

    for i in range(start, end + 1):
        if(i%mult1 == 0):
            if(i%mult2 == 0):
                if(i%mult3 == 0):
                    cont = cont + 1
    
    print(cont)

questao1()

# -------------------------------------
# -------------------------------------

# Questão 2

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat = fat * i
    return fat

def position_par(i):
    return 3**i + 7*(fatorial(i))

def position_impar(i):
    return 2**i + 4*math.log(i)

def questao2():
    X = []
    positon_big = 0
    summer = 0
    lenght_lista = 10
    
    for i in range(0, lenght_lista):
        if(i%2 == 0):
            X.append(position_par(i))
        else:
            X.append(position_impar(i))
        if(X[i] > X[positon_big]):
            positon_big = i
        summer = summer + X[i]
    
    media = summer/lenght_lista
    print("Posicao do maior elemento: ", positon_big)
    print("Media: ", round(media, 2))

questao2()

# -----------------------------------
# -----------------------------------
# Questão 3

number_of_students = 5

def dictionary():
    dictionary_grades = []
    
    for i in range(0, number_of_students):
        name = input("Qual o nome do " + str((i+1)) + "° aluno?\n")
        grade = float(input("Qual a nota desse aluno?\n"))
        tupla = (name, grade)
        dictionary_grades.append(tupla)
        print("")
    
    return dictionary_grades

def questao3():
    dictionary_grades = dictionary()
    biggest_grade = 0
    best_student = ""
    for tupla in dictionary_grades:
        if(tupla[1] >= biggest_grade):
            best_student = tupla[0]
            biggest_grade = tupla[1]
    
    print("Aluno com maior nota: ", best_student)
    print("Maior nota: ", biggest_grade)

questao3()

# --------------------------------------------
# --------------------------------------------