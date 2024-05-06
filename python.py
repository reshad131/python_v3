# task1

# list = [-4,16,0,1,4,5,9,16,25,36,49,64,81,100]

# sonuc = []

# for number in list:
#     x = number ** 0.5
#     sonuc.append(x)

# print(sonuc)





#task2

# def funksiya (list):
#     tekrarsiz = []
#     for num in list:
#         if list.count(num) == 1:
#             tekrarsiz.append(num)
#     return tekrarsiz

# liste = [-1,1,2,2,6,7,7,'say']
# result = funksiya(liste)
# print(result)




#task3

# def hasil(inputList):
#     sonuc = 1
#     for i in inputList:
#         sonuc *= int(i)
#     return sonuc

# inputList = input("Enter a number:  ")
# result = hasil(inputList)
# print(result)


#task4

# num=int(input("Bolenlerini tapmaq istediyiniz ededi daxil edin: "))
# bolenler = [x for x in range(1, num+1) if num % x ==0]
# print(bolenler)


#task5

# aylar = ["Yanvar" , "Fevral" , "Mart" , 
#          "Aprel" , "May" , "Iyun" , 
#          "Iyul" , "Iyun" , "Avqust" ,
#            "Sentyabr" , "Noyabr" , "Dekabr"]
           

# x = {ay: len(ay) for ay in aylar}
# print(x)


# task6

# names = ["Rick Sanchez" , "Morty Smith" , "Summer Smith" , "Jerry Smith" , "Beth Smith"]
# x = [name.split()[0].lower() for name in names]
# print(x)

#task7

# num1 = [1 , 2 , 3]
# num2 = [4 , 5 , 6]

# x = [(num1[i] + num2[i]) / 2 for i in range(len(num1))]
# print(x)