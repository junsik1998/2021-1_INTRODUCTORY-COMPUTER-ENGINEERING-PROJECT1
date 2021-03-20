import re

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