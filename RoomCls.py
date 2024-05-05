import math
from random import *
import numpy as np



class Gen:
    def __init__(self, info_arr):
        self.genes = list() #유전자들을 담는 공간
        self.info = info_arr #학생 정보를 담는 공간
        self.n = len(self.info) #학생 수
        self.gen_num = 0 #현재 세대 수        
        self.score_dict = dict() #유전자 별 점수를 담은 공간
        
        self.num_of_genes = 100 #한 세대의 유전자 수
        self.selection_ratio = 0.4 #선택 비율
        self.crossover_a, self.crossover_b = 0.001, 5000 #교차 변수1, 2
        self.mutant_a = 0

        #self.mutant_ratio = 0.1  #변이율
        self.set_first_gen() #첫번째 세대 생성 (초기화)
    
    #단순 시그모이드 함수
    @staticmethod
    def sigmoid(x):
        return 1/(1+np.exp(-x))
    #교차율 함수
    def crossover_ratio(self):
        return self.sigmoid(self.crossover_a*(self.gen_num-self.crossover_b))*0.6 + 0.4
    def mutant_ratio(self):
        return min(0.0001 * self.gen_num, 1)

    #첫번째 세대를 초기화하는 과정
    def set_first_gen(self):
        for _ in range(self.num_of_genes):
            arrl = list(range(self.n))
            shuffle(arrl)
            ars = Gene(self.info, arrl)
            self.genes.append(ars)
        self.gen_num = 1
    
    def set_score(self): #유전자 별 적합도 함수 값 계산하기
        self.score_dict = dict()
        for _ in self.genes:
            self.score_dict[_] = _.total_score()
        d2 = dict(sorted(self.score_dict.items(), key=lambda x: x[1]))
        self.score_dict = d2
    def show_score(self):
        self.set_score()
        print("GEN"+str(self.gen_num))
        print(list(self.score_dict.values()))
    def show_avg_gen(self):
        self.set_score()
        print("Average score of GEN "+str(self.gen_num)+" : %.3f" %(sum(list(self.score_dict.values()))))
    def show_result(self, num):
        print()
        print("<%dst result RESULT> -> %.5f"%(num, self.score_dict[self.genes[num]]))

        arrl1 = self.genes[num].seq
        go2 = (3-len(arrl1)%3)%3
        go3 = int((len(arrl1) - 2*go2)/3)
        for i in range(go2 + go3):
            if i < go3:
                a, b, c = self.info[arrl1[3*i]], self.info[arrl1[3*i + 1]], self.info[arrl1[3*i + 2]]
                print("Room %-3d : [ %-4s, %d, %d, %d ] [ %-4s, %d, %d, %d ] [ %-4s, %d, %d, %d ]"
                %(i, a.name, a.time, a.temp, a.noise, b.name, b.time, b.temp, b.noise, c.name, c.time, c.temp, c.noise), end='   ')
                print("호실 점수 : %.5f" %Student.score(a, b, c))
            else:
                a, b = self.info[arrl1[go3 + 2*i]], self.info[arrl1[go3 + 2*i + 1]]
                print("Room %-3d : [ %-4s, %d, %d, %d ] [ %-4s, %d, %d, %d ]                         "
                %(i, a.name, a.time, a.temp, a.noise, b.name, b.time, b.temp, b.noise), end='   ')
                print("호실 점수 : %.5f" %Student.score(a, b))
        
    def generation(self):
        self.selection()
        self.crossover()
        self.mutation()
        self.replacement()
        self.gen_num += 1
    def selection(self):
        self.set_score()
        score = list(self.score_dict.items())
        self.selected_gene = list()
        for _ in range(int(self.num_of_genes * self.selection_ratio)):
            self.selected_gene.append(score[_])
    def crossover(self):
        shuffle(self.selected_gene)
        self.new_gen = list()
        for _ in range(len(self.selected_gene)//2):
            gene1, gene2 = self.selected_gene[2*_][0], self.selected_gene[2*_+1][0]
            gene1_roominfo, gene2_roominfo = gene1.sort_room(), gene2.sort_room()
            new_arr = list()
            cnt_two = 0
            cnt_max = (3 - self.n % 3) % 3
            num1, num2 = 0, 0
            while 3*len(new_arr) < self.num_of_genes * self.crossover_ratio():
                if(num1 < len(gene1_roominfo) and num2 < len(gene2_roominfo)):
                    if Student.score(*list(map(lambda y: self.info[y], gene1_roominfo[num1]))) < Student.score(*list(map(lambda y: self.info[y], gene2_roominfo[num2]))):
                        arr = gene1_roominfo[num1]
                        num1 += 1
                        poss = True
                        for _ in arr: 
                            for k in new_arr:
                                 if _ in k: poss = False
                        if poss and (cnt_two < cnt_max or len(arr) != 2):
                            new_arr.append(arr)
                    else:
                        arr = gene2_roominfo[num2]
                        num2 += 1
                        poss = True
                        for _ in arr: 
                            for k in new_arr:
                                 if _ in k: poss = False
                        if poss and (cnt_two < cnt_max or len(arr) != 2):
                            new_arr.append(arr)
                elif num1 < len(gene1_roominfo):
                    arr = gene1_roominfo[num1]
                    num1 += 1
                    poss = True
                    for _ in arr: 
                            for k in new_arr:
                                 if _ in k: poss = False
                    if poss and (cnt_two < cnt_max or len(arr) != 2):
                        new_arr.append(arr)
                elif num2 < len(gene2_roominfo):
                    arr = gene2_roominfo[num2]
                    num2 += 1
                    poss = True
                    for _ in arr: 
                            for k in new_arr:
                                 if _ in k: poss = False
                    if poss and (cnt_two < cnt_max or len(arr) != 2):
                        new_arr.append(arr)
                else:
                    break   
            arr_now = list()
            for _ in new_arr: arr_now.extend(_)
            check_arr = list(range(0,self.n))
            
            for _ in arr_now: check_arr.remove(_)
            shuffle(check_arr)

            new_arr = sorted(new_arr, key= lambda x: len(x), reverse=True)
            new_arr2 = list()
            for _ in new_arr:
                for __ in _: new_arr2.append(__)
            for _ in check_arr:
                new_arr2.append(_)
            self.new_gen.append(new_arr2)
    def mutation(self):
        for _ in self.new_gen:
            rand_num = random()
            if rand_num < self.mutant_ratio():
                k = int(self.n*self.crossover_ratio())
                a1, a2 = randint(0, k), randint(0, k)
                while a1 == a2: a2 = randint(0, k)
                tmp = _[a1]
                _[a1] = _[a2]
                _[a2] = tmp
        for seq in self.new_gen:
            a = Gene(self.info, seq)
            self.genes.append(a)
    def replacement(self):
        #새롭게 생겨난 자손들의 seq 배열 len이 82가 아닌 경우가 존재한다. 개같은 버그
        while len(self.genes) > self.num_of_genes:
            self.set_score()
            arr = list(self.score_dict.items())
            self.genes.remove(arr[-1][0])

class Gene:
    def __init__(self, arr, seq):
        self.room_score = list()
        self.info = arr #학생 정보 배열
        self.seq = seq #학생 호실 배정 배열
        self.size = len(arr)
        if self.size % 3 == 0: self.go2 = 0
        elif self.size % 3 == 1: self.go2 = 2
        elif self.size % 3 == 2: self.go2 = 1
        self.go3 = (self.size - 2*self.go2)//3
    def score_list(self):
        self.room_score = list()    
        for i in range(self.go2+self.go3):
            if i < self.go3:
                self.room_score.append(Student.score(self.info[self.seq[3*i]], self.info[self.seq[3*i+1]], self.info[self.seq[3*i+2]]))
            else:
                self.room_score.append(Student.score(self.info[self.seq[self.go3 + 2*i]], self.info[self.seq[self.go3 + 2*i + 1]]))
        return self.room_score
    def total_score(self):
        if len(self.room_score) == 0:
            self.score_list()
        return sum(self.room_score)/self.size
    def create_room_list(self):
        self.room_list = list()
        for i in range(self.go2+self.go3):
            if i < self.go3:
                self.room_list.append([self.seq[3*i], self.seq[3*i+1], self.seq[3*i+2]])
            else:
                self.room_list.append([self.seq[3*self.go3 + 2*(i-self.go3)], self.seq[3*self.go3 + 2*(i-self.go3) + 1]])
    def sort_room(self):
        self.create_room_list()
        array2 = sorted(self.room_list, key = lambda i : Student.score(*list(map(lambda y: self.info[y], i))))
        self.room_list = array2
        return self.room_list
        # 방 별로 리스트에 넣고 점수 높은 순으로 나열하는 기능을 구현해야 함.

class Student: #학생 한 명에 대한 객체를 나타내는 클래스
    def __init__(self, name, time, temp, noise):
        self.name = name
        self.time = time
        self.temp = temp
        self.noise = noise
            
    @staticmethod
    def score(*data):
        if len(data) == 3:
            return Student.scorefor3(data[0], data[1], data[2])
        elif len(data) == 2:
            return Student.scorefor2(data[1], data[0])    
    def scorefor3(st1, st2, st3):
        return (Student.f1(st1, st2, st3)*(1/3)*63 + Student.f2(st1, st2, st3)*(3/(4*math.sqrt(2)))*57 + Student.f3(st1, st2, st3)*51)/171
    def scorefor2(st1, st2):
        return (Student.ff1(st1, st2)*(1/2)*63 + Student.ff2(st1, st2)*(1/4)*57 + Student.ff3(st1, st2)*51)/171
    
    def f1(st1, st2, st3):
        l = [st1.time, st2.time, st3.time]
        if len(set(l)) == 1: return 0
        elif len(set(l)) == 2:
            if l.count(min(l)) == 2: return 2
            else: return 1
        else: return 3
    def f2(st1, st2, st3):
        return math.sqrt((st1.temp**2 + st2.temp**2 + st3.temp**2)/3
                         - ((st1.temp + st2.temp + st3.temp)/3)**2)
    def f3(st1, st2, st3):
        return int(not(st1.noise == st2.noise and st2.noise == st3.noise))

    def ff1(st1, st2):
        if(st1.time == st2.time): return 0
        else: return 1
    def ff2(st1, st2):
        return math.sqrt((st1.temp**2 + st2.temp**2)/2 - ((st1.temp + st2.temp)/2)**2)
    def ff3(st1, st2):
        return int(not(st1.noise == st2.noise))