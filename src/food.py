import time
import string
import os
import glob
from inputCheck import inputFoodName, checkListNum, inputFoodAmount, inputFoodExpiration, matchFoodAmount
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def foodInput(path):
    print("식품명, 식품의 양, 식품의 유통기한(YYYYMMDD)을 공백을 기준으로 입력하세요.")
    while True:
        string = input("입력 > ")
        try:
            input_string = string.split()
            if inputFoodName(input_string[0]) and checkListNum(input_string,3) and inputFoodAmount(input_string[1]) and inputFoodExpiration(input_string[2]):
                while True:
                    title = time.strftime('%Y%m%d%H%M%S',time.localtime())
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
            print("공백을 기준으로 조건에 맞게 3가지 요소만 입력하세요.")

def foodOutput(path):
    file_list = os.listdir("./refrigerator/"+path)
    file_list_txt = [file for file in file_list if file.endswith(".txt")]
    expiration_date = 99999999
    food_file = ""
    print("식품명, 양을 공백을 기준으로 입력하세요.")
    while True:
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
        except:
            print("공백을 기준으로 조건에 맞게 2가지 요소만 입력하세요.")
        if food_file == "":
            print("식품이 존재하지 않습니다.")
            break
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
                    break
                elif amount[0] == amount[1]:
                    os.remove("./refrigerator/"+path+"/"+food_file)
                    print(food_name+"을(를) 전부 출고 완료")
                    break
                else:
                    print(food_name+"의 최대 출고 가능한 양은 "+str(amount[0])+amount[2]+" 입니다.")
                    break



def lessExpirationDate():
    #print("유통기한 적게 남은 식품 확인을 위한 함수")
    now = datetime.now()
    ex_date = get_date(now)
    now_date = int(now.strftime('%Y%m%d'))
    if ex_date >= now_date:
        takingExpiration(ex_date)
    else:
        print("이미 유통기한이 지난 식품은 확인할 수 없습니다")
        
        
#유통기한 입력받는 함수        
def get_date(now):
    while(True):
        print("================")
        date = input("유통기한이 입력하신 날짜 또는 기간 이내로 남은 식품 목록을 출력해 드리기 위해서,YYYYMMDD형식의 날짜 또는 양의 정수와 기간의 단위(일, 월, 년)의 결합으로 이루어진 기간을 입력해주세요.\n\n입력 >")
        if isinstance(date, int):
            if len(date == 8):
                return date
            else:
                print("입력형식에 맞지 않습니다.")
                continue
        elif isinstance(date, string):
            n = len(date)
            num = int(date[0:n-1])
            kind = date[n-1:n]
            if kind == "일":
                wanted_date = now + timedelta(days=num)
            elif kind == "월":
                wanted_date = now + relativedelta(months=num)
            elif kind == "년":
                wanted_date = now + relativedelta(years=num)
            else:
                print("입력형식에 맞지 않습니다.")
                continue
            wanted_date.strftime('%Y%m%d')
            return int(wanted_date)
        
        
#유통기한 검사해서 가져오는 함수        
def takingExpiration(ex_date):
    count = 0
    food_dic ={}
    file_list = glob.glob(ROOT_PATH)
    file_list_txt = [file for file in file_list if file.endswith(".txt")]
    for i in range(0, len(file_list_txt)):
        f = open.(file_list_txt[i], 'r', encoding='utf-8') #위에서 텍스트 파일 경로들을 리스트 받아와서, 인덱스로 해당 텍스트파일들 출력하려는 의도인데, 문법적으로 틀린 것 같은데 어떻게 수정할 지 모르겠습니다.
        string_list = f.split(' ')
        if int(string_list[2]) > ex_date:
            food_dic[string_list[0]] = int(string_list[2])
            count+=1
        f.close()
    if count == 0:
        print("해당되는 식품이 없습니다.")
    else:
        dic = sorted(food_dic.items(), key=lambda x:x[1])
    print("식품명 / 유통기한 / 남은 일수\n")
     for i in dic:
            print("\n")#
