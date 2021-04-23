import os
import re
from menu import menuSelect, SEARCH_MENU_LIST
from showList import showRecipeList
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
            return 0
        else:
            f.write(food_note)


def cooking(path):     
    possible_recipe_select_menu_list = ["메인 메뉴로 돌아가기"]
    possible_recipe_list = []
    recipe_list = os.listdir(RECIPE_PATH) #레시피 목록 가져오기
    recipe_list_txt = [file for file in recipe_list if file.endswith(".txt")]
    food_file_list = os.listdir("./refrigerator/"+path) #식재로 목록 가져오기
    food_file_list_txt = [file for file in food_file_list if file.endswith(".txt")]
    if(len(recipe_list_txt)==0 or len(food_file_list_txt)==0):
        print("만들 수 있는 요리가 없습니다.")
        return
    for i in recipe_list_txt:
        f = open(RECIPE_PATH+i,'r',encoding='utf-8')
        lineList = f.readlines()
        foodList = [0 for j in range(len(lineList))]    #요리에 필요한 식재료의 이름 , 줄 수 만큼 0으로 초기화
        checkList = [False for j in range(len(lineList))]   #식재료 체크 , 줄 수 만큼 false로 초기화
        f.close()
        for j in len(lineList):    
            buf = lineList[j].split()
            foodList[j] = buf[0]                        #식재료 이름

        for j in food_file_list_txt:    #남아있는 식품 검사
            f=open(REFRIGERATOR_PATH+path+"/"+j,'r',encoding='utf-8')
            line = f.readline()
            buf = line.split()          #buf[0]은 남아있는 식품명
            if(buf[0] in foodList):     #필요한 식품이 냉장고에 있다면
                tmp = foodList.index(buf[0])    #buf[1] 의 단위
                checkList[tmp]=True
            f.close()
        check=1
        for j in range(len(checkList)):
            if(checkList[j]==False):
                check*=0
                break
        if(check==1):       #현재 가지고 있는 식품으로 만들 수 있을 경우
            recipe_name = i[:-4]
            possible_recipe_list.append(recipe_name)

    if(len(possible_recipe_list)==0):
        print("만들 수 있는 요리가 없습니다.")
        return
    possible_recipe_select_menu_list.extend(possible_recipe_list)

    while True:
        recipeMenuNum = showRecipeList("만들 수 있는 요리목록",possible_recipe_select_menu_list)
        if not recipeMenuNum:   # 0이면 메인메뉴로
            break
        while True:
            recipeName_txt = showRecipeDetail(recipeMenuNum,possible_recipe_select_menu_list)    #상세정보 출력
            menu1=menuSelect("수정 및 삭제 메뉴",SEARCH_MENU_LIST)
            if menu1 == 0:
                break
            elif menu1 == 1:
                editRecipe(recipeName_txt)
            else:
                removeRecipe(recipeName_txt)
                tmp = recipeName_txt[:-4]               
                possible_recipe_select_menu_list.remove(tmp)        #리스트에 반영
                break
                
        
        
        

def showRecipeDetail(menu,recipe_list): #상세정보출력 함수
    file_list = os.listdir(RECIPE_PATH)
    file_list_txt = [file for file in file_list if file.endswith(".txt")]
    for i in file_list_txt:
        if(i==recipe_list[menu]+".txt"):
            f = open(RECIPE_PATH+i,'r',encoding='utf-8')
            lineList = f.readlines()
            for line in lineList:
                print(line)
            f.close()
            return i      

    
def removeRecipe(i):
    os.remove(RECIPE_PATH+i)
    print("레시피 삭제됨")

def editRecipe(i):#작성필요
    pass
    #f = open(RECIPE_PATH+recipeName_txt,'w',encoding='utf-8')   recipeName_txt라는 변수가 정의되지 않았습니다.
