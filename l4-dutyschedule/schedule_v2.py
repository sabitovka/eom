# -*- coding: utf-8 -*-
"""schedule_v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fKxXHEXjlTlcbXopJnyddK9UvQP0eT3Q
"""

import numpy as np

class DutyScheduleProblem:
  def __init__(self):
    # initialize instance variables:
    self.items = []

    # Максимальное количество смен, которое может работать работник в неделю
    self.maxShiftsPerWeek = 10

    # Минимальное значение квалификации в смене
    self.minQualificationNumber = 50

    # Количество смен в день
    self.shiftsPerDay = 3

    # Количество смен в неделю
    self.shiftsPerWeek = 7 * self.shiftsPerDay

    # initialize the data:
    self.__initData()

  def __initData(self):
    self.items = [
      ("Инженер А", 40),
      ("Техник B", 20),
      ("Техник C", 20),
      ("Техник D", 20),
      ("Рабочий E", 10),
      ("Рабочий F", 10),
      ("Рабочий G", 10),
      ("Рабочий H", 10),
    ]

  def __len__(self):
    return len(self.items) * self.shiftsPerWeek

  def getValue(self, zeroOneList):
    # Преобразуем в двоичную матрицу
    schedule = np.reshape(zeroOneList, (len(self.items), self.shiftsPerWeek))

    numberOfShiftsPerWeekViolations = self.countNumberOfShiftsPerWeekViolation(schedule)[1]
    qualificationPerShiftViolations = self.countQualificationPerShiftViolation(schedule)[1]

    return numberOfShiftsPerWeekViolations + qualificationPerShiftViolations

  def countNumberOfShiftsPerWeekViolation(self, schedule):
    violations = 0
    shiftPerWeek = []
    for laborShifts in schedule:
      shiftsCount = sum(laborShifts)
      shiftPerWeek.append(shiftsCount)
      if (shiftsCount > self.maxShiftsPerWeek):
        violations += shiftsCount - self.maxShiftsPerWeek
    return shiftPerWeek, violations

  def countQualificationPerShiftViolation(self, schedule):
    violations = 0
    qualsPerShift = []
    for i in range(len(schedule[0])):
      qual = 0
      for j in range(len(schedule)):
        qual += self.items[j][1] * schedule[j][i]
      qualsPerShift.append(qual)
      if qual < self.minQualificationNumber:
        violations += self.minQualificationNumber - qual

    return qualsPerShift, violations


  def printItems(self, zeroOneList):
    schedule = np.reshape(zeroOneList, (len(self.items), self.shiftsPerWeek))

    laborCosts = np.sum(schedule, axis=1)
    numberOfShiftsPerWeekViolations = self.countNumberOfShiftsPerWeekViolation(schedule)
    qualificationPerShiftViolations = self.countQualificationPerShiftViolation(schedule)

    print('\tСмена\t', np.asarray([(i % self.shiftsPerDay)+1 for i in range(self.shiftsPerWeek)]), '| ТЗ')
    print('Сотрудники')
    print('-' * 115)
    for i in range(len(self.items)):
      print(self.items[i][0], '\t', schedule[i], '|', laborCosts[i])
  
    print()
    print('Кол-во смен в неделю для каждого сотрудника', numberOfShiftsPerWeekViolations[0])
    print('Нарушений кол-ва смен в неделю: ', numberOfShiftsPerWeekViolations[1])

    print()
    print('Значение квалификации в каждой смене', qualificationPerShiftViolations[0])
    print('Нарушений значения квалификации в каждой смене', qualificationPerShiftViolations[1])

    print()
    print('Фитнесс: ', numberOfShiftsPerWeekViolations[1] + qualificationPerShiftViolations[1])

# testing the class:
def main():
  # create a problem instance:
  schedule = DutyScheduleProblem()
  # creaete a random solution and evaluate it:
  randomSolution = np.random.randint(2, size=len(schedule))
  #print("Random Solution = ")
  #print(randomSolution)
  schedule.printItems(randomSolution)

if __name__ == "__main__":
  main()