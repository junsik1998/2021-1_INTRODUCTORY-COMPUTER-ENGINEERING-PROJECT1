import os
import re
from menu import menuSelect, SEARCH_MENU_LIST
from inputCheck import inputRecipeName, inputFoodNote

#폴더 경로들 (상수 취급하여 코딩해 주세요.)
REFRIGERATOR_PATH = "./refrigerator/"
RECIPE_PATH = "./recipe/"

def addRecipe ():
    current_recipe_list = os.listdir(RECIPE_PATH)
    while True:
        recipe = inputRecipeName()
        if recipe in current_recipe_list:
            print("이미 등록된 요리입니다.")
        else:
            break
    f = open(RECIPE_PATH+recipe+'.txt', 'w')
    print("요리에 필요한 재료들의 식품명과 메모의 쌍을 공백을 기준으로 식품명과 메모를 구분하여 한 쌍을 한 줄씩 입력해 주세요.")
    print("모든 입력이 끝났으면 엔터를 한번 더 입력하세요.")
    while True:
        food_note = inputFoodNote()
        if food_note == 0:
            f.close()
            return 0;
        else:
            f.write(food_note)



def cooking(path):     
    possible_recipe_select_menu_list = ["메인 메뉴로"]
    current_possible_recipe_list = []
    current_recipe_list = os.listdir(RECIPE_PATH) #레시피 목록 가져오기
    current_file_list_txt = [file for file in file_list if file.endswith(".txt")]
    food_file_list = os.listdir("./refrigerator/"+path)
    food_file_list_txt = [file for file in file_list if file.endswith(".txt")]
    if(len(current_recipe_list_txt)==0 or len(food_file_list_txt)==0):
        print("만들 수 있는 요리가 없습니다.")
        return
    for i in current_file_list_txt:
        f = open(RECIPE_PATH+i,'r',encoding='utf-8')
        lineList = f.readlines()
        foodList = [0 for j in range(len(lineList))]    #요리에 필요한 식재료의 이름
        amountList = [0 for j in range(len(lineList))]  #요리에 필요한 식재료의 양
        checkList = [0 for j in range(len(lineList))]   #가지고 있는 식재료의 양 
        f.close()
        for j in len(lineList):    
            buf = lineList[j].split()
            foodList[j] = buf[0]
            if re.compile('mL$').search(buf[1]): 
                amountList[j]+= int(buf[1].replace('mL',''))
            elif re.compile('kg$').search(buf[1]):  
                amountList[j]+= (int(buf[1].replace('kg','')))*1000      
            elif re.compile('g$').search(buf[1]):
                amountList[j]+= int(buf[1].replace('g',''))
            elif re.compile('L$').search(buf[1]):
                amountList[j]+= (int(buf[1].replace('L','')))*1000
            elif re.compile('인분$').search(buf[1]):
                amountList[j]+= int(buf[1].replace('인분',''))
            else :
                print("오류: 혀용되지 않은 단위")
                return False
        for j in food_file_list_txt:    #남아있는 식품 검사
            f=open(REFRIGERATOR_PATH+path+"/"+j,'r',encoding='utf-8')
            line = f.readline()
            buf = line.split()          #buf[0]은 남아있는 식품명, buf[1]은 남아있는 식품량 
            if(buf[0] in foodList):     #필요한 식품이 냉장고에 있다면
                tmp = foodList.index(buf[0])    #buf[1] 의 단위
                if re.compile('mL$').search(buf[1]): 
                    checkList[tmp]+= int(buf[1].replace('mL',''))
                elif re.compile('kg$').search(buf[1]):  
                    checkList[tmp]+= (int(buf[1].replace('kg','')))*1000      
                elif re.compile('g$').search(buf[1]):
                    checkList[tmp]+= int(buf[1].replace('g',''))
                elif re.compile('L$').search(buf[1]):
                    checkList[tmp]+= (int(buf[1].replace('L','')))*1000
                elif re.compile('인분$').search(buf[1]):
                    checkList[tmp]+= int(buf[1].replace('인분',''))
                else :
                    print("오류: 혀용되지 않은 단위")
                    return False
            f.close()
        check=1
        for(j in range(len(checkList))):
            if(checkList[j]<amountList[j]):
                check*=0
                break
        if(check==1):       #현재 가지고 있는 식품으로 만들 수 있을 경우
            recipe_name = i[:-4]
            current_possible_recipe_list.append(recipe_name)
    if(len(current_possible_recipe_list)==0):
        print("만들 수 있는 요리가 없습니다.")
        return
    possible_recipe_select_menu_list.extend(current_possible_recipe_list)
    showRecipeList("만들 수 있는 요리목록",current_possible_recipe_list)
    

def showRecipeList(menuName,recipe_list):
    menu=menuSelect(menuName,recipe_list)
    if menu==0:
        return 0
    file_list = os.listdir(RECIPE_PATH)
    file_list_txt = [file for file in file_list if file.endswith(".txt")]
    for i in file_list_txt:
        if(i==recipe_list[menu-1]+".txt"):
            f = open(RECIPE_PATH+i,'r',encoding='utf-8')
            while True:
                line=f.readline()
                if not line:break;
                print(line)
            f.close()
            menu1=menuSelect("메뉴",SEARCH_MENU_LIST)
            if menu==0:
                return 0
            elif menu==1:
                f = open(RECIPE_PATH+i,'w',encoding='utf-8')
                ##################### 문서 수정 작성
                return 0
            else:
                os.remove(RECIPE_PATH+i)
                print("레시피 삭제됨")
                return 0
                
