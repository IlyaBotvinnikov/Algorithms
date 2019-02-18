# -------------------------------------------------------------------------------------
# 5. Пользователь вводит две буквы.
#    Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
#   https://drive.google.com/file/d/1LYEf6pEtSpiaU618FHoaVHJIcEiO9hj8/view?usp=sharing
# -------------------------------------------------------------------------------------
import string
alphabet_string = string.ascii_uppercase
print(alphabet_string)

alphabet_list = []
i = 0                                       
for i in range( len(alphabet_string) ):              # преобразуем строку в список
	alphabet_list.append(alphabet_string[i])

print(alphabet_list)                                 # получили алфавит в виде списка, то есть знаем индексы букв

print("Введите одну букву алфавита: ")               
A_str = str(input("A_str= ")).upper()                # приводим введенную букву к uppercase 
print(A_str)

print("Введите еще одну букву алфавита: ")        
B_str = str(input("B_str= ")).upper()                # приводим введенную букву к uppercase 

A_str_index = alphabet_list.index(A_str)             # получаем индексы введенных букв     
B_str_index = alphabet_list.index(B_str)

print(" индекс первой введенной буквы = ", A_str_index)
print(" индекс второй введенной буквы = ", B_str_index)


diff_str = abs(B_str_index - A_str_index -1)

print("букв между", A_str, "и", B_str, " - ", diff_str)
