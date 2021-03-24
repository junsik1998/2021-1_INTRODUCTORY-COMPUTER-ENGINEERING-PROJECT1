import re
import time
from datetime import datetime

def inputInt(start, end):
    while True:
        try:
            number = int(input('입력 > '))
            if start <= number <= end:
                return number
            else:
                print(f"{start}이상 {end}이하의 정수로 입력해 주세요.")
        except ValueError:
            print("정수만 입력해 주세요.")


def inputRefrigerarorName():
    while True:
        input_text = input("냉장고 이름 > ")
        check_text = ''
        find_text = re.findall(r'[가-힣a-z0-9_]+', input_text)
        for temp in find_text:
            check_text += temp
        if input_text == check_text and len(input_text) >= 1 and len(input_text) <= 20:
            return check_text
        else:
            if len(input_text) < 1 or len(input_text) > 20:
                print("1글자 이상 20글자 이하로 입력해주세요.")
            else:
                print("한글, 영문 소문자, 숫자, 밑줄 문자(_)만 입력 가능합니다.")

def inputFoodName(input_text):
    check_text = ''
    find_text = re.findall(r'[가-힣a-z0-9_()]+', input_text)
    for temp in find_text:
        check_text += temp
    if input_text == check_text and len(input_text) >= 1 and len(input_text) <= 20:
        return True
    else:
        if len(input_text) < 1 or len(input_text) > 20:
            print("1글자 이상 20글자 이하로 입력해주세요.")
            return False
        else:
            print("한글, 영문 소문자, 숫자, 밑줄 문자(_), 괄호 문자만 입력 가능합니다.")
            return False

def checkListNum(list,num):
    if len(list) == num:
        return True
    else:
        print("공백을 기준으로 조건에 맞게 "+str(num)+"가지 요소만 입력하세요.")
        return False

def inputInt2(number,start,end,text):
    try:
        if start <= number <= end:
            return True
        else:
            print(f"{start}이상 {end}이하의 "+text+"정수로 입력해 주세요.")
            return False
    except ValueError:
        print(text+"정수만 입력해 주세요.")
        return False

def inputFoodAmount(input_text):
    try:
        if re.compile('mL$').search(input_text):
            amount_num = int(input_text.replace('mL','',1))
            if inputInt2(amount_num,1,9999999999,"단위가 있는 "):
                return True
            else:
                return False
        elif re.compile('kg$').search(input_text):
            amount_num = int(input_text.replace('kg','',1))
            if inputInt2(amount_num,1,9999999999,"단위가 있는 "):
                return True
            else:
                return False
        elif re.compile('g$').search(input_text):
            amount_num = int(input_text.replace('g','',1))
            if inputInt2(amount_num,1,9999999999,"단위가 있는 "):
                return True
            else:
                return False
        elif re.compile('L$').search(input_text):
            amount_num = int(input_text.replace('L','',1))
            if inputInt2(amount_num,1,9999999999,"단위가 있는 "):
                return True
            else:
                return False
        elif re.compile('인분$').search(input_text):
            amount_num = int(input_text.replace('인분','',1))
            if inputInt2(amount_num,1,9999999999,"단위가 있는 "):
                return True
            else:
                return False
        else:
            print("양 입력시 단위(mL,L,g,kg,인분)가 있는 정수로 입력해주세요.")
    except:
        print("양 입력시 단위(mL,L,g,kg,인분)가 있는 정수로 입력해주세요.")

def inputFoodExpiration(num):
    res = re.search('[^0-9]', num)
    if res == None and len(num) == 8:
        now = time.strftime('%Y%m%d',time.localtime())
        if int(now) <= int(num):
            year = int(num[:4])
            month = int(num[4:6])
            day = int(num[6:])
            try:
                datetime(year, month, day)
                return True
            except:
                print("해당 날짜는 유효하지 않는 날짜 입니다. 확인 후 다시 입력해주세요.")
                return False
        else:
            print("유통기한은 오늘 날짜 기준 오늘 또는 다음 날짜를 입력해주세요.")
            return False
    else:
        print("유통기한은 8자리 정수로만 입력해주세요.")
        return False

def matchFoodAmount(foodIn,foodOut):
    if re.compile('mL$').search(foodIn) and re.compile('mL$').search(foodOut):
        foodIn = int(foodIn.replace('mL',''))
        foodOut = int(foodOut.replace('mL',''))
        return [foodIn,foodOut,"mL"]
    elif re.compile('kg$').search(foodIn) and re.compile('kg$').search(foodOut):
        foodIn = int(foodIn.replace('kg',''))
        foodOut = int(foodOut.replace('kg',''))
        return [foodIn,foodOut,"kg"]
    elif re.compile('g$').search(foodIn) and  re.compile('g$').search(foodOut):
        foodIn = int(foodIn.replace('g',''))
        foodOut = int(foodOut.replace('g',''))
        return [foodIn,foodOut,"g"]
    elif re.compile('L$').search(foodIn) and re.compile('L$').search(foodOut):
        foodIn = int(foodIn.replace('L',''))
        foodOut = int(foodOut.replace('L',''))
        return [foodIn,foodOut,"L"]
    elif re.compile('인분$').search(foodIn) and re.compile('인분$').search(foodOut):
        foodIn = int(foodIn.replace('인분',''))
        foodOut = int(foodOut.replace('인분',''))
        return [foodIn,foodOut,"인분"]
    else:
        print("양 입력시 출고될 양과 같은 단위(mL,L,g,kg,인분)가 있는 정수로 입력해주세요.")
        return False
