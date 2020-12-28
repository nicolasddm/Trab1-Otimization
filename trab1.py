import numpy as np
from scipy.optimize import linprog
import sys

A_eq = []
B_eq = []

A_ineq = []
B_ineq = []

numTasks, numMachines = input().split()
print(numTasks, numMachines)

numTasks = int(numTasks)
numMachines = int(numMachines)

tasksHours = []

for i in range(0, numTasks):
  tasksHours.append(int(input()))
print(tasksHours)

machsInfos = []

for i in range(0, numMachines):
  cost, maxUseTime = input().split()
  infos = [int(cost), int(maxUseTime)]
  machsInfos.append(infos)
print(machsInfos)

numOfVariables = 0
eachMachTasks = []

for i in range(0, numMachines):
  listAux = []
  numMachTasks = int(input())
  for i in range(0, numMachTasks):
      listAux.append(int(input())) 
      numOfVariables += 1
  listAux = sorted(set(listAux))
  eachMachTasks.append(listAux)
print(eachMachTasks)

machsCosts = []

for i in range(0, numMachines):
  for j in range(0, len(eachMachTasks[i])):
    machsCosts.append(machsInfos[i][0])
print(machsCosts)

for i in range(0, numTasks):
  vet_aux_l1 = []
  for machine in eachMachTasks:
    for task in machine:
      if (task == i+1):
        vet_aux_l1.append(1)        
      else:
        vet_aux_l1.append(0)
  A_eq.append(vet_aux_l1)
  B_eq.append(tasksHours[i])
print(A_eq, B_eq)

for i in range(0, numMachines):
  vetAux = []
  z = 0
  for machine in eachMachTasks:
      if i == z:
          for task in machine:
              vetAux.append(1)
      else:
          for task in machine:
              vetAux.append(0)
      z += 1
  A_ineq.append(vetAux)
  B_ineq.append(machsInfos[i][1])
print(A_ineq, B_ineq)

result = linprog(c = machsCosts, A_ub=A_ineq, b_ub=B_ineq, A_eq=A_eq, b_eq=B_eq, bounds=(0, None), method='simplex')

print(result.x)
print(result.fun)

y=0
for machine in eachMachTasks:
  for task in range(0, numTasks):
    if task+1 in machine:
      print(float(result.x[y]), end=" ")
      y += 1
    else:
      print(float(0), end=" ")
  print('')
print(float(result.fun))
