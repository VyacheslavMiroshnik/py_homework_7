documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "10006"},
        {"type": "insurance", "number": "1003"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }       
def search_by_people_name(doc_number="", some_data=False):
  if not doc_number:
    doc_number=input("Введите номер документа ")
    find_doc  = False 
  try:
    for element_document in documents:
        if doc_number == element_document["number"]:
            find_doc = True
            if not some_data:
                print (element_document["name"])
            else:
                return documents.index(element_document)   
  except KeyError:
      print('Такого документа нет ')

def full_info():
  for element_document in documents:
    for scroll in element_document.values():
      print(str(scroll), end=" ")
    print()

def search_shelf_number(doc_number="", some_data=False):
  if not doc_number:
   doc_number=input("Введите номер документа ")
  find_doc  = False  
  for number_shelf, list_doc in directories.items():
    if doc_number in list_doc : 
      if not some_data:
        print(f"документы находятся на {number_shelf} полке ")
      else:
        return {number_shelf:list_doc.index(doc_number) }  
  if not find_doc:
    print("Такого документа нет в списке")     


def add_new_card():
  temp_dict={
    "type" : input("Введите тип документа "),
    "number": input("Введите номер документа "),
    "name": input("Введите имя  ")
  }
  documents.append(temp_dict)
  number_shelf = input("Введите номер полки ")
  if number_shelf not in directories.keys():
    directories[number_shelf]=[]
  directories[number_shelf].append(temp_dict["number"])

def delete_card():
  doc_number = input("Введите номер докумена который нужно удалить ")
  p = search_by_people_name
  s = search_shelf_number
  if p(doc_number,True):
    del(documents[p(doc_number, True)])
    temp_dict=s(doc_number, True)
    for shelf_number,index_of_list in temp_dict.items():
      del(directories[shelf_number][index_of_list])

def move_document():
  doc_number = input("Введите номер документа ")
  s = search_shelf_number
  temp_dict = s(doc_number, True)
  if temp_dict:
    new_number_shelf = input("Введите номер полки куда необходимо переместить ")
    if new_number_shelf not in directories.keys():
      directories[new_number_shelf]=[]
    for number_shelf, index_of_list in temp_dict.items():
      directories[new_number_shelf].append((directories[number_shelf][index_of_list]))
    del(directories[number_shelf][index_of_list]) 

def add_shelf():
  new_number_shelf = input('Введите новый номер полки')
  if new_number_shelf not in directories.keys():
    directories[new_number_shelf]=[]
  else:
    print("Такая полка уже есть ")

def print_dict(dict):
  if type(dict) == list:
    for key in dict:
      print(key)
  else:
    for key, values in dict.items():
      print(key, " ", values)  

def print_all_name():
        for element_document in documents:
            try:
        
                print(element_document["name"])
            except KeyError:
                print(f"у документа {element_document['number']} нет поля name")
init_dict = {
  "p": search_by_people_name,
  "l": full_info ,
  "s": search_shelf_number,
  "a": add_new_card,
  "d": delete_card,
  "md": move_document,
  "as": add_shelf,
  "na": print_all_name
}
print_dict(documents)
print_dict(directories)
user_init= input("Введите \n p - для поиска имени \n l - получить всю информацию в строку  \n s - поиск полки \n a - добавить новый документ  \n d - удалить документ \n md - переместить документ \n as - добавить полку \n na - имена всех владельцев \n ").lower()
if  init_dict.get(user_init):
    init_dict[user_init]()
    print_dict(documents)
    print_dict(directories)
else:
  print("Нет такой команды")   