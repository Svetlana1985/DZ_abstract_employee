from abc import ABC, abstractmethod
from typing import List
class Employee(ABC):
    def __init__(self, name: str, post: str):
        self.name = name
        self.post = post
        self.completed_tasks = 0
        pass
    @abstractmethod
    def work(self, task):
        pass
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.completed_tasks == other.completed_tasks
        return False
    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.completed_tasks < other.completed_tasks
        return False
    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.completed_tasks > other.completed_tasks
        return False

class Developer(Employee):
    def work(self, task):
        print(f'Разработчик {self.name} работает над {task.description}')
        task.mark_complete()
        self.completed_tasks +=1

class Tester(Employee):
    def work(self, task):
        print(f'Тестировщик {self.name} тестирует {task.description}')
        task.mark_complete()
        self.completed_tasks += 1

class Manager(Employee):
    def work(self, task):
        print(f'Управляющий {self.name} управляет {task.description}')
        task.mark_complete()
        self.completed_tasks += 1

class Task:
    def __init__(self, description: str, employee: Employee):
        self.description = description
        self.employee = employee
        self.is_complete = False
    def mark_complete(self):
        self.is_complete = True

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks:List[Task] = []
        self.employees:List[Employee] = []
    def add_task(self, task: Task):
        self.tasks.append(task)
    def add_employee(self, employee: Employee):
        self.employees.append(employee)
    def assing_tasks(self):
        for task in self.tasks:
            task.employee.work(task)
class LeadDeveloper(Developer, Manager):
    def __init__(self, name):
        super().__init__(name, 'Ведущий разработчик')

project = Project('Верстка веб-сайта')
developer = Developer('Аленушка Прелестница', 'Разработчик')
tester = Tester('Алеша Попович', 'Тестировщик')
manager = Manager('Тугарин Змей', 'Управляющий')
lead_developer = LeadDeveloper('Соловей Разбойник')

project.add_employee(developer)
project.add_employee(tester)
project.add_employee(manager)
project.add_employee(lead_developer)

task1 = Task('Дизайн пользовательского интерфейса', developer)
task2 = Task('Написание кода', developer)
task3 = Task('Тест UI', tester)
task4 = Task('Тест API', tester)
task5 = Task('Планирование проекта', manager)
task6 = Task('Проверка кода', lead_developer)

project.add_task(task1)
project.add_task(task2)
project.add_task(task3)
project.add_task(task4)
project.add_task(task5)
project.add_task(task6)

project.assing_tasks()
print(f'Сравнение')
print(f'{developer > tester}')
print(f'{developer == tester}')
print(f'{manager < developer}')


        

