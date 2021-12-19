#Task 1
#def numbers(bin_list):
 #   bin_str = "".join(str(x) for x in bin_list)
  #  return int(bin_str, 2)
#
#if __name__ == "__main__":
#    print(numbers([0, 1, 1, 0]))

#Task 2
# def capitalization(my_str):
#     for i in range(len(my_str)):
#         up_char = my_str[i].upper()
#         print(f"{my_str[:i]}{up_char}{my_str[i+1:]}")
#
# if __name__ == "__main__":
#     print(capitalization("bbbbbbb"))

# Task 4
# if __name__ == "__main__":
#     word_list = "мама мыла раму".split(" ")
#     list_of_numbers = []
#     for word in word_list:
#         a = 0
#         for i in word:
#             a += int(ord(i)-1071)
#         list_of_numbers.append(a)
#     print(word_list[list_of_numbers.index(max(list_of_numbers))])


# Task 5
# if __name__ == "__main__":
#     word = "mosertQ"
#     middle = int(len(word)//2)
#     if middle % 2 == 0:
#         print(f'{word[(middle-1)::-1]}{word[middle]}{word[:middle:-1]}')
#     else:
#         print(f'{word[(middle-1)::-1]}{word[:middle:-1]}{word[middle]}')

# Task 7
# import datetime
# import random
# from faker import Faker
# import string
#
# import json
# Faker.seed(random)
# fake = Faker()
#
# Alph_ = {
#     'а': 'a',
#     'е': 'e',
#     'ж': 'zh',
#     'н': 'n',
#     'с': 's',
#     'ш': 'sh',
#     'я': 'ya',
#     'Ж': 'Zh',
#     'С': 'S'
#
# }
# """в алфавит вынесены только буквы используемые в списке имен (при вводе новых имен в список - словарь дополнить)"""
# names = ("Саша", "Женя")
# surnames = ("Степаненко", "Иващенко", "Ким")

# def generate_person(n):
#     dict_for_all = []
#     for counter in range(1, n+1):
#         name = random.choice(names)
# """выбор имени"""
#         len_name = len(name)
#
#         def gen_login():
# """транслитерация логина из имени по словарю"""
#             login_ = str("")
#             for i in range(0, len_name):
#                 letter = Alph_[name[i]]
#                 login_ = login_ + letter
#             return login_
#         def password():
#             pass_ = string.digits + string.ascii_letters
#             return "".join(random.choice(pass_) for _ in range(6))
#         dict_ = {"Number in system": counter,
#             "name": name, "surname": random.choice(surnames),
#             "login": "@" + gen_login(), "password": password(),
#             "email": gen_login() + "@" + gen_login() + ".com",
#             "phone": "+7" + fake.phone_number(),
#             "register_time": str(datetime.datetime.now())
#             }
#         dict_for_all.append(dict_)
#         counter += 1
#     return dict_for_all
#
# def write_it_in_json(n):
#     with open('package.json', 'w') as f:
#         return json.dump(generate_person(n), f, indent=4, ensure_ascii=False)
#
#
# if __name__ == "__main__":
#     write_it_in_json(10)
#     print(generate_person(10))

# Task 8
import datetime

if __name__ == "__main__":
    print(datetime.datetime.today().strftime('%Y-%m-%d'))








