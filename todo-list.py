import csv

TODO_FILE = "todos.csv"


def load_todos():
   try:
      with open(TODO_FILE, newline="", encoding="utf-8") as file:
         return [row[0] for row in csv.reader(file) if row]
   except FileNotFoundError:
      return []


tasks = load_todos()


##Add title to list
def add_one_task(title):
   tasks.append(title)
   save_todos()
    
    

def delete_task(number_to_delete):
   tasks.pop(number_to_delete)
   save_todos()

##Print tasks on list along with list index position    
## 1 Hacer loop en lista
## 2 Acceder valor de la lista
## 3 Imprir el valor de la lista con su indice numerico
def print_list(tasks):
      ##Enumerate asigns by pairs  index and value of element in the list
      ##loop through all
    for index, item in enumerate(tasks):
        
      print(index,item)

def save_todos():
   with open(TODO_FILE, "w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerows([task] for task in tasks)

#add_one_task("cantar")
#delete_task(2)

while True:
   
   title = input("Tarea (Enter para terminar):").strip()
   ##If title was not entered
   if not title:
      ##finish loop
      break
   add_one_task(title)
   
print_list(tasks)

