# 목표 : 호실 배정 2개 중에서 겹치지 않는 방향으로 가장 우수한 형질(호실)부터 하나씩
# 가져와서 최대한 많은 호실들을 가져온 뒤에, 남은 인원들만을 바탕으로 랜덤으로 호실을 배정한다.
# 하나의 유전자는 호실 배정 해를 가지고 있어야 함
# 각 세대를 저장해놓을 수 있으면 굉장히 좋을 듯
# 1) 호실 배정 방법을 표시할 수 있는 자료 구조를 만든다.
# 2) 배정 해들을 담고 있는 세대 자료 구조를 만든다.
# 3) 한 세대 안에서 유전 알고리즘의 단계를 구현한다. (선택, 교차, 변이, 대치 총 4 단계를 반복하는 것이 하나의 새로운 세대를 만드는 것이 될 것이다.)


from RoomCls import *
from random import *
import csv
import time

info = list()
n = 62

# 파일로 저장된 학생 정보 데이터 배열로 불러오기
def load_info(num):
    data = list()
    f = open("real_std.csv",'r')
    rea = csv.reader(f)
    for row in rea:
        data.append(row)
    f.close
    for _ in range(num):
        exec("%s = Student('%s', %d, %d, %d)" % ('stdex'+str(_), data[_][0],
                                int(data[_][1]), int(data[_][2]), int(data[_][3])))
        exec("info.append(%s)" %('stdex'+str(_)))

# 학생 정보 리스트 출력
def show_info():
    for _ in info: print("{0:^4} [ {1:>4}, {2}, {3}, {4} ]".format('<'+str(info.index(_))+'>', _.name, _.time, _.temp, _.noise))

load_info(n) 
kl, kl2, kl3, kl4, kl5 = Gen(info), Gen(info), Gen(info), Gen(info), Gen(info)

for i in range(10000):
    kl.generation()
    kl2.generation()
    kl3.generation()
    if i-1 % 100 == 0:
        print('[')
        print("kl1 : ", end=''); kl.show_avg_gen()
        print("kl2 : ", end=''); kl2.show_avg_gen()
        print("kl3 : ", end=''); kl3.show_avg_gen()
        print(']')
for i in range(10):
    kl.show_result(i)
