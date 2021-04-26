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
    find_text = re.findall(r'[가-힣A-z0-9_()]+', input_text)
    for temp in find_text:
        check_text += temp
    if input_text == check_text and len(input_text) >= 1 and len(input_text) <= 20:
        return True
    else:
        if len(input_text) < 1 or len(input_text) > 20:
            print("식품명은 1글자 이상 20글자 이하로 입력해주세요.")
            return False
        else:
            print("식품명은 한글, 영문 대소문자, 숫자, 밑줄 문자(_), 괄호 문자 ')','(' 만 입력 가능합니다.")
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
            print(text+f"{start}이상 {end}이하의 정수로 입력해 주세요.")
            return False
    except ValueError:
        print(text+"정수로 입력해 주세요.")
        return False

def inputFoodAmount(input_text):
    try:
        if re.compile('mL$').search(input_text):
            amount_num = int(input_text.replace('mL','',1))
            if inputInt2(amount_num,1,10000,"식품의 양은 단위가 있는 "):
                return True
            else:
                return False
        elif re.compile('kg$').search(input_text):
            amount_num = int(input_text.replace('kg','',1))
            if inputInt2(amount_num,1,10000,"식품의 양은 단위가 있는 "):
                return True
            else:
                return False
        elif re.compile('g$').search(input_text):
            amount_num = int(input_text.replace('g','',1))
            if inputInt2(amount_num,1,10000,"식품의 양은 단위가 있는 "):
                return True
            else:
                return False
        elif re.compile('L$').search(input_text):
            amount_num = int(input_text.replace('L','',1))
            if inputInt2(amount_num,1,10000,"식품의 양은 단위가 있는 "):
                return True
            else:
                return False
        elif re.compile('인분$').search(input_text):
            amount_num = int(input_text.replace('인분','',1))
            if inputInt2(amount_num,1,10000,"식품의 양은 단위가 있는 "):
                return True
            else:
                return False
        else:
            print("식품의 양은 단위(mL,L,g,kg,인분)가 있는 정수로 입력해주세요.")
    except:
        print("식품의 양은 단위(mL,L,g,kg,인분)가 있는 정수로 입력해주세요.")

def inputFoodExpiration(num):
    res = re.search('[^0-9]', num)
    if res == None and len(num) == 8:
        now = time.strftime('%Y%m%d',time.localtime())
        year = int(num[:4])
        month = int(num[4:6])
        day = int(num[6:])
        try:
            datetime(year, month, day)
            if int(now) <= int(num):
                return True
            else:
                 print("식품의 유통기한은 오늘 날짜 기준 오늘 또는 다음 날짜를 입력해주세요.")
        except:
            print("해당 날짜는 유효하지 않는 날짜 입니다. 확인 후 다시 입력해주세요.")
            return False
    else:
        print("식품의 유통기한은 8자리 정수로만 입력해주세요.")
        return False


def isYYYYMMDD(input_string):
    if len(input_string) == 8:
        find_text = re.search('[^0-9]', input_string)
        if find_text == None:
            now = time.strftime('%Y%m%d',time.localtime())
            year = int(input_string[:4])
            month = int(input_string[4:6])
            day = int(input_string[6:])
            try:
                datetime(year, month, day)
                if int(now) <= int(input_string):
                    return True
                else:
                    print("오늘 날짜 기준 오늘 또는 다음 날짜를 입력해주세요.")
                    return False
            except:
                print("해당 날짜는 유효하지 않는 날짜 입니다. 확인 후 다시 입력해주세요.")
                return False
        else:
            return False
    else:
        return False

def isAllInt(input_string):
    find_text = re.search('[^0-9]', input_string)
    if len(input_string) > 0 and find_text == None:
        return True
    else:
        return False


def matchFoodAmount(foodIn,foodOut):
    try:
        if re.compile('mL$').search(foodIn) and re.compile('mL$').search(foodOut):
            foodIn = int(foodIn.replace('mL',''))
            foodOut = int(foodOut.replace('mL',''))
            return [foodIn,foodOut,"mL"]
        elif re.compile('kg$').search(foodIn) and re.compile('kg$').search(foodOut):
            foodIn = int(foodIn.replace('kg',''))
            foodOut = int(foodOut.replace('kg',''))
            return [foodIn,foodOut,"kg"]
        elif re.compile('kg$').search(foodIn) and re.compile('g$').search(foodOut):
            foodIn = int(foodIn.replace('kg',''))*1000
            foodOut = int(foodOut.replace('g',''))
            return [foodIn,foodOut,"g"]
        elif re.compile('g$').search(foodIn) and  re.compile('g$').search(foodOut):
            foodIn = int(foodIn.replace('g',''))
            foodOut = int(foodOut.replace('g',''))
            return [foodIn,foodOut,"g"]
        elif re.compile('L$').search(foodIn) and re.compile('mL$').search(foodOut):
            foodIn = int(foodIn.replace('L',''))*1000
            foodOut = int(foodOut.replace('mL',''))
            return [foodIn,foodOut,"mL"]
        elif re.compile('L$').search(foodIn) and re.compile('L$').search(foodOut):
            foodIn = int(foodIn.replace('L',''))
            foodOut = int(foodOut.replace('L',''))
            return [foodIn,foodOut,"L"]
        elif re.compile('인분$').search(foodIn) and re.compile('인분$').search(foodOut):
            foodIn = int(foodIn.replace('인분',''))
            foodOut = int(foodOut.replace('인분',''))
            return [foodIn,foodOut,"인분"]
        else:
            print("식품의 양은 출고될 양과 같은 단위(mL,L,g,kg,인분)가 있는 정수로 입력해주세요.")
            return False
    except:
        print("식품의 양은 출고될 양과 같은 단위(mL,L,g,kg,인분)가 있는 정수로 입력해주세요.")
        return False
    
    
def inputRecipeName():
    while True:
        input_text = input("요리 이름 > ")
        check_text = ''
        find_text = re.findall(r'[가-힣A-z0-9_]+', input_text)
        for temp in find_text:
            check_text += temp
        if input_text == check_text and len(input_text) >= 1 and len(input_text) <= 30:
            return check_text
        else:
            if len(input_text) < 1 or len(input_text) > 30:
                print("1글자 이상 30글자 이하로 입력해주세요.")
            else:
                print("한글, 영문 대소문자, 숫자, 밑줄 문자(_)만 입력 가능합니다.")
    
def inputFoodNote():
    while True:
        input_text = input("식품명, 메모 > ")
        try:
            if input_text == '':
                return 0
            input_string = input_text.split()
            food_name = input_string[0]
            note = input_string[1]
            check_text1 = ''
            check_text2 = ''
            find_text1 = re.findall(r'[가-힣A-z0-9_()]+', food_name)
            find_text2 = re.findall(r'[가-힣A-z0-9_()]+', note)
            for temp1 in find_text1:
                check_text1 += temp1
            if food_name == check_text1 and len(food_name) >= 1 and len(food_name) <= 20:
                for temp2 in find_text2:
                    check_text2 += temp2
                if note == check_text2 and len(note) >= 1 and len(note) <= 10:
                    return (check_text1+' '+check_text2)
                else:
                    print("입력하신 값이 문법 형식에 맞지 않습니다.")
    
            else:
                print("입력하신 값이 문법 형식에 맞지 않습니다.")
                
        except: 
            print("입력하신 값이 문법 형식에 맞지 않습니다.")
        
def inputConditionName(input_text1, input_text2):
    if input_text1=='식품명' or input_text1=='식품생성날짜' or input_text1=='유통기한':
        if input_text2=='오름차순' or input_text2=='내림차순':
            return True
        else:
            print("정렬기준은 ‘식품명’, ‘식품생성날짜’, ‘유통기한’만 입력가능하고, 오름/내림차순 은 ‘오름차순’, ‘내림차순’만 입력 가능합니다.")
            return False
    else:
        print("정렬기준은 ‘식품명’, ‘식품생성날짜’, ‘유통기한’만 입력가능하고, 오름/내림차순 은 ‘오름차순’, ‘내림차순’만 입력 가능합니다.")
        return False
   

def stringCompare(str1,str2):
    s1=''
    s2=''
    s1=str1.lower()
    s2=str2.lower()
    if s1==s2:
        return True
    else:
        if s1 in s2:
            return True
        else:
            return False
