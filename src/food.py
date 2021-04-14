import time
import string
import os
from inputCheck import inputFoodName, checkListNum, inputFoodAmount, inputFoodExpiration, matchFoodAmount

def foodInput(path):
    while True:
        print("식품명, 식품의 양, 식품의 유통기한(YYYYMMDD)을 공백을 기준으로 입력하세요.")
        string = input("입력 > ")
        try:
            input_string = string.split()
            if inputFoodName(input_string[0]) and checkListNum(input_string,3) and inputFoodAmount(input_string[1]) and inputFoodExpiration(input_string[2]):
                while True:
                    title = time.strftime('%Y%m%d%I%M%S',time.localtime())
                    if os.path.isfile("./refrigerator/"+path+"/"+title+".txt") == True:
                        time.sleep(1)
                    else:
                        break
                f = open("./refrigerator/"+path+"/"+title+".txt", 'w',encoding='utf-8')
                f.write(string)
                f.close()
                print("식품 입고 완료")
                break
        except:
            pass

def foodOutput(path):
    file_list = os.listdir("./refrigerator/"+path)
    file_list_txt = [file for file in file_list if file.endswith(".txt")]
    expiration_date = 99999999
    food_file = ""
    while True:
        print("식품명, 양을 공백을 기준으로 입력하세요.")
        string = input("입력 > ")
        try:
            input_string = string.split()
            if inputFoodName(input_string[0]) and checkListNum(input_string,2) and inputFoodAmount(input_string[1]):
                food_name = input_string[0]
                out_food_amount = input_string[1]
                for i in file_list_txt:
                    f = open("./refrigerator/"+path+"/"+i,'r',encoding='utf-8')
                    line = f.readline()
                    buf = line.split()
                    if buf[0] == food_name and expiration_date > int(buf[2]):
                        food_file = i
                        food_amount = buf[1]
                        expiration_date = int(buf[2])
                    f.close()
                break
        except:
            pass
    if food_file == "":
        print("식품이 존재하지 않습니다.")
    else:
        if matchFoodAmount(food_amount,out_food_amount):
            amount = matchFoodAmount(food_amount,out_food_amount)
            if amount[0] > amount[1]:
                amount[0] = amount[0] - amount[1]
                new_line = food_name + " " + str(amount[0])+amount[2]+ " " + str(expiration_date)
                f = open("./refrigerator/"+path+"/"+food_file,'w',encoding='utf-8')
                f.write(new_line)
                f.close()
                print(food_name+"을(를) "+str(amount[1])+str(amount[2])+" 만큼 출고하여 "+str(amount[0])+amount[2]+" 만큼 남음")
            elif amount[0] == amount[1]:
                os.remove("./refrigerator/"+path+"/"+food_file)
                print(food_name+"을(를) 전부 출고 완료")
            else:
                print(food_name+"의 최대 출고 가능한 양은 "+str(amount[0])+amount[2]+" 입니다.")



def lessExpirationDate():
    print("유통기한 적게 남은 식품 확인을 위한 함수")
