import os

from menu import menuSelect, MAIN_MENU_LIST
from inputCheck import inputRefrigerarorName
from food import foodInput, foodOutput, lessExpirationDate
from search import searchFood, searchRecipe
from showList import showALLFood
from recipe import addRecipe, cooking


refrigerator = "" #현재 선택된 냉장고 이름

#폴더 경로들 (상수 취급하여 코딩해 주세요.)
ROOT_PATH = "./"
REFRIGERATOR_PATH = "./refrigerator/"
RECIPE_PATH = "./recipe/"


def selectRefrigerator(): #냉장고 선택 함수
    refrigerator_select_menu_list = ["냉장고 추가"]
    current_refrigerator_list = os.listdir(REFRIGERATOR_PATH) #냉장고 목록 가져오기
    refrigerator_select_menu_list.extend(current_refrigerator_list)
    menu = menuSelect("냉장고 선택 및 추가 메뉴", refrigerator_select_menu_list) #냉장고 선택 및 추가 메뉴
    while menu==0:
        while True:
            refrigerator = inputRefrigerarorName()
            if refrigerator in current_refrigerator_list:
                print("중복되는 냉장고 이름이 있습니다. 다른 이름을 입력해 주세요.")
            else:
                break
        os.mkdir(REFRIGERATOR_PATH+refrigerator) #냉장고 이름의 폴더 생성
        current_refrigerator_list.append(refrigerator)
        refrigerator_select_menu_list.append(refrigerator)
        menu = menuSelect("냉장고 선택 및 추가 메뉴", refrigerator_select_menu_list) #냉장고 선택 및 추가 메뉴 다시 보여줌
    return refrigerator_select_menu_list[menu] #사용자가 선택한 냉장고


if __name__ == "__main__":
    root_path_list = os.listdir(ROOT_PATH) 
    if "recipe" not in root_path_list: #레시피 폴더가 없으면
        os.mkdir(RECIPE_PATH) #레시피 폴더 생성
    if "refrigerator" not in root_path_list: #냉장고 폴더가 없으면
        os.mkdir(REFRIGERATOR_PATH) #냉장고 폴더가 생성
    
    refrigerator = selectRefrigerator() #냉장고 선택
    print("선택한 냉장고: " + refrigerator)

    while True:
        menu = menuSelect("메인 메뉴", MAIN_MENU_LIST)
        if menu == 0:
            print("프로그램 종료")
            break
        if menu == 1:
            foodInput(refrigerator)
        if menu == 2:
            foodOutput(refrigerator)
        if menu == 3:
            searchFood(refrigerator)
        if menu == 4:
            showALLFood(refrigerator)
        if menu == 5:
            lessExpirationDate(refrigerator)
        if menu == 6:
            addRecipe()
        if menu == 7:
            searchRecipe()
        if menu == 8:
            cooking(refrigerator)
        if menu == 9:
            refrigerator = selectRefrigerator()
            print("변경된 냉장고: " + refrigerator)
