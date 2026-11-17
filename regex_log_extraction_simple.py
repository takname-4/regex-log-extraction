
import re

# 로그 파일 읽기
file = open("07-02. 전주대 대동제 및 해커톤 통합운영 데이터 로그.txt", "r", encoding="utf-8")
data = file.read()
file.close()

# 1. 이메일 주소 추출
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+', data)

# 2. 휴대폰 번호 추출
phones = re.findall(r'010[-. ]\d{4}[-. ]\d{4}', data)

# 3. 학번과 학과 추출
students = re.findall(r'\[(202\d{6})\s*/\s*([가-힣]+)\]', data)

# 4. GitHub 주소와 쿠폰 코드 추출
github = re.findall(r'https?://github\.com/[A-Za-z0-9-]+/[A-Za-z0-9_-]+(?:\.git)?', data)
coupons = re.findall(r'FEST-2026-[A-Z0-9]{4}', data)

# 5. 부스별 매출 추출
sales = re.findall(r'- (.*?) 매출: ([\d,]+)원', data)

# 결과 출력
print("1. 이메일 주소")
for email in emails:
    print(email)

print("\n2. 휴대폰 번호")
for phone in phones:
    print(phone)

print("\n3. 학번과 학과")
for student in students:
    print(student)

print("\n4. GitHub 주소")
for url in github:
    print(url)

print("\n2026년 쿠폰 코드")
for coupon in coupons:
    print(coupon)

print("\n5. 부스별 매출")
total = 0

for booth, money in sales:
    print(booth, ":", money, "원")
    total = total + int(money.replace(",", ""))

print("\n전체 매출 합계:", format(total, ",") + "원")
