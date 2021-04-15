import os
from inputCheck import inputRecipeName
from recipe import showRecipeList

#폴더 경로들 (상수 취급하여 코딩해 주세요.)
REFRIGERATOR_PATH = "./refrigerator/"
RECIPE_PATH = "./recipe/"

def searchFood():
    print("식품 검색하기를 위한 함수")


def searchRecipe():
    current_recipe_list = os.listdir(RECIPE_PATH)
    search_recipe_list = []
    print("검색할 요리이름을 입력하세요")
    recipe = inputRecipeName()
    for i in current_recipe_list:
        val=i.find(recipe)
        if val!= (-1):
            search_recipe_list.append(i)
    
    if len(search_recipe_list) == 0:
        print("검색 결과가 없습니다.")
        return 0
    showRecipeList("요리 레시피 목록", search_recipe_list)
