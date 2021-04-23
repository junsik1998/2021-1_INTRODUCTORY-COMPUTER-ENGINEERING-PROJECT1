import os
import time
from menu import menuSelect
from inputCheck import checkListNum, inputConditionName, inputFoodAmount, inputFoodExpiration

def showFoodList():
    print("식품 목록을 출력하는 함수")


def showRecipeList(menuName,recipe_list):
    menu=menuSelect(menuName,recipe_list)
    return menu



def showALLFood(path):
    food_list=[]
    index_list=[]
    real_list=[]

    print("정렬기준과 오름/내림차순을 공백을 기준으로 입력하시오.")
    while(True):
        string=input("입력> ")
        input_condition=string.split()
        if checkListNum(input_condition,2) and inputConditionName(input_condition[0],input_condition[1]):
            break

    while(True):
        food_list.clear()
        index_list.clear()
        real_list.clear()
        food_list.append("메인메뉴로 돌아가기")
        file_list = os.listdir("./refrigerator/"+path)
        file_list_txt = [file for file in file_list if file.endswith(".txt")]
        i=0
        for i in file_list_txt:
            f = open("./refrigerator/"+path+"/"+i,'r',encoding='utf-8')
            line = f.readline()
            buf = line.split()        
            real_list.append([buf[0],buf[2],i])
            f.close()

        if input_condition[0]=="식품명":
            real_list.sort()
        if input_condition[0]=="유통기한"and input_condition[1]=='오름차순':
            real_list.sort(key=lambda x : x[1])
        if input_condition[0]=="유통기한"and input_condition[1]=='내림차순':
            real_list.sort(key=lambda x : x[1], reverse=True)
        if input_condition[0]=="식품생성날짜"and input_condition[1]=='오름차순':
            real_list.sort(key=lambda x : x[2])
        if input_condition[0]=="식품생성날짜"and input_condition[1]=='내림차순':
            real_list.sort(key=lambda x : x[2], reverse=True)
        i=0
        while i<len(real_list):
            food_list.append(real_list[i][0])
            index_list.append(real_list[i][2])
            i+=1


        menu=menuSelect("식품목록",food_list)
        if(menu==0):
            break
        else:
            while(True):
                f = open("./refrigerator/"+path+"/"+index_list[menu-1],'r',encoding='utf-8')
                line=f.readline()
                print(line)
                f.close()
                submenu=menuSelect("수정 및 삭제 메뉴",['돌아가기','수정하기','삭제하기'])
                if(submenu==0):                    
                    break
                if(submenu==1):
                    while True:
                        print("수정 값(양, 유통기한)")
                        string = input("입력 > ")
                        input_string = string.split()
                        if  checkListNum(input_string,2) and inputFoodAmount(input_string[0]) and inputFoodExpiration(input_string[1]):
                            while True:
                                title = time.strftime('%Y%m%d%H%M%S',time.localtime())
                                if os.path.isfile("./refrigerator/"+path+"/"+title+".txt") == True:
                                    time.sleep(1)
                                else:
                                    break
                            f = open("./refrigerator/"+path+"/"+index_list[menu-1], 'w',encoding='utf-8')
                            f.write(food_list[menu]+' ')
                            f.write(string)
                            f.close()
                            break

                if(submenu==2):
                    os.remove("./refrigerator/"+path+"/"+index_list[menu-1])
                    food_list.pop(menu)
                    index_list.pop(menu-1)
                    print("삭제가 완료되었습니다.")
                    break
        
    

    

        
    

