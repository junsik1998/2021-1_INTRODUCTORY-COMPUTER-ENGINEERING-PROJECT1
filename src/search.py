import os
import time
from inputCheck import inputRecipeName, inputFoodName, checkListNum, inputFoodAmount, inputFoodExpiration, stringCompare
from recipe import showRecipeDetail, removeRecipe, editRecipe
from menu import menuSelect, SEARCH_MENU_LIST
from showList import showRecipeList

#폴더 경로들 (상수 취급하여 코딩해 주세요.)
REFRIGERATOR_PATH = "./refrigerator/"
RECIPE_PATH = "./recipe/"

def searchFood(path):
    food_list=["메인메뉴로 돌아가기"]
    index_list=[]
    print("검색할 식품명을 입력하세요.")
    while True:
        food_name=(input("입력> "))
        if inputFoodName(food_name)==True:
            break
    file_list = os.listdir("./refrigerator/"+path)
    file_list_txt = [file for file in file_list if file.endswith(".txt")]
    for i in file_list_txt:
        f = open("./refrigerator/"+path+"/"+i,'r',encoding='utf-8')
        line = f.readline()
        buf = line.split()
        if stringCompare(food_name,buf[0])==True:
            food_list.append(buf[0])
            index_list.append(i)
        f.close()
    if len(food_list)==1:
        print("검색 결과가 없습니다.")         
        return

    while(True):
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




def searchRecipe():
    current_recipe_list = os.listdir(RECIPE_PATH)
    search_recipe_list = ["메인 메뉴로 돌아가기"]
    print("검색할 요리이름을 입력하세요")
    recipe = inputRecipeName()
    for i in current_recipe_list:
        val=i.find(recipe)
        if val!= (-1):
            search_recipe_list.append(i)
    
    if len(search_recipe_list) == 0:
        print("검색 결과가 없습니다.")
        return 0
    
    while True:
        recipeMenuNum = showRecipeList("요리 레시피 목록",search_recipe_list)
        if not recipeMenuNum:   # 0이면 메인메뉴로
            break
        while True:
            recipeName_txt = showRecipeDetail(recipeMenuNum,search_recipe_list)    #상세정보 출력
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
