from inputCheck import inputInt

MAIN_MENU_LIST = ["종료", "식품 입고", "식품 출고", "식품 검색", "전체 식품 목록 출력", "유통기한 적게 남은 식품 확인", "요리 레시피 등록", "요리 레시피 검색", "보관중인 식품으로 만들 수 있는 요리 확인", "냉장고 변경"]
SEARCH_MENU_LIST = ["돌아가기", "수정", "삭제"]

def menuSelect(menuName, menuList):
    print("[" + menuName + "]")
    for i in range(len(menuList)):
        print(i, ".", menuList[i])
    return inputInt(0, len(menuList) - 1)
