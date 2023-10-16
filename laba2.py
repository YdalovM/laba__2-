# задача 4
# функция проверяет введенные данные и в соответствии с ними возвращает котегорию
# def temp_cat(temp):
#     if temp < - 20:
#         return(0)
#     elif temp >= -20 and temp < 0:
#         return(1)
#     elif temp >= 0 and temp < 15:
#         return(2)
#     elif temp >= 15 and temp < 25:
#         return(3)
#     else:
#         return(4)

# пользователь вводит данные
# temp= int(input())

# вывод результата функции
# print(temp_cat(temp))

# # задача 5
# def check_phone(phone):
#     rez = []
#     for i in phone:
#         l = len(i)
#         flag = True
#         if '+' in i[0]:
#             if '+' == i[0]:
#                 if i[1] == '7':
#                     flag = True
#                 elif i [1] == '8':
#                     flag = True
#                 else:
#                     flag = False
#                 l -= 1
#             else:
#                 flag = False
#         if '-' in i:
#             if '-' != i[0]:
#                 l -= 1
#             else:
#                 flag = False
#         if '(' in i and ')' in i:
#             if '(' != i[0]:
#                 l -= 1
#             if ')' != i[0]:
#                 l -= 1
#             else:
#                 flag = False
#         if l != 11:
#             flag = False
        
#         if flag == True:
#             rez.append(i)
#         else:
#             rez.append(-1)
#     return rez
# phone = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '-123 456 ++7890']
# print(check_phone(phone))
    
    
    
    
    
    
    
    

