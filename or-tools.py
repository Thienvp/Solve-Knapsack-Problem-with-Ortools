from ortools.algorithms import pywrapknapsack_solver
import os 
from time import time

current_path ="./sampledata/"
folders = sorted(os.listdir(current_path))[1:13]
subfolders =['n00050', 'n00100', 'n00200', 'n00500', 'n01000']
def Solver (input_url):
  input = open(input_url,"r").read().splitlines()
  capacities = [int(input[2])]
  size = input[1]
  values=[]
  weights = [[]]
  for i in input[4:]:
    values.append(int(i.split()[0]))
    weights[0].append(int(i.split()[1]))
  print("+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------")
  print("| The number of items: |", size)
  # print("| Weights:             |", weights)
  # print("| Values:              |", values)
  print("| Capacities:          | ", capacities[0])
  solver = pywrapknapsack_solver.KnapsackSolver(
    pywrapknapsack_solver.KnapsackSolver.
    KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample') 
  solver.set_time_limit(120)
  solver.Init(values, weights, capacities)
  start_time = time()
  computed_value = solver.Solve()
  packed_items = []
  packed_weights = []
  total_weight = 0
  print("+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------")
  print('| Total value:         |', computed_value)
  for i in range(len(values)):
      if solver.BestSolutionContains(i):
          packed_items.append(i)
          packed_weights.append(weights[0][i])
          total_weight += weights[0][i]
  end_time = time()
  runtime = end_time - start_time
  print('| Total weight:        |', total_weight)
  # print('| Packed items:        |', packed_items)
  # print('| Packed_weights:      |', packed_weights)
  print('| Run time :           |', round(runtime,4))
  print("+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------")
  
def run(folder_name):
  for subfolder in subfolders :
    url = current_path + folder_name + "/" +subfolder + "/R01000/s000.kp"
    print("| "+url)
    Solver(url)
