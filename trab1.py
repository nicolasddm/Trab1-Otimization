#!/usr/bin/python3
import numpy as np
from scipy.optimize import linprog
import sys

A_eq = []
B_eq = []
A_ineq = []
B_ineq = []

tasksHours = []
machsInfos = []
eachMachTasks = []
machsCosts = []

numTasks, numMachines = input().split()

numTasks = int(numTasks)
numMachines = int(numMachines)

for i in range(0, numTasks):
  tasksHours.append(int(input()))

for i in range(0, numMachines):
  cost, maxUseTime = input().split()
  infos = [int(cost), int(maxUseTime)]
  machsInfos.append(infos)

for i in range(0, numMachines):
  listAux = []
  numMachTasks = int(input())
  for i in range(0, numMachTasks):
      listAux.append(int(input())) 
  listAux = sorted(set(listAux))
  eachMachTasks.append(listAux)

for i in range(0, numMachines):
  for j in range(0, len(eachMachTasks[i])):
    machsCosts.append(machsInfos[i][0])

for i in range(0, numTasks):
  vetAux = []
  for machine in eachMachTasks:
    for task in machine:
      if (task == i+1):
        vetAux.append(1)        
      else:
        vetAux.append(0)
  A_eq.append(vetAux)
  B_eq.append(tasksHours[i])

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

result = linprog(c = machsCosts, A_ub=A_ineq, b_ub=B_ineq, A_eq=A_eq, b_eq=B_eq, bounds=(0, None), method='simplex')

if result.success:
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

else: 
  print(result.message)