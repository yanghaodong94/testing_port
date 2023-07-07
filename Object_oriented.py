"""
 项目名称:面向对象
 功能描述:类与对象的用法
 创建人:杨
 创建日期:2023.7.6
"""


# # 创建洗衣机的类
# class Washer:
#     # 创建属性
#     def __init__(self, a, b):
#         self.weith = a
#         self.height = b
#
#     def wash(self):
#         print(f'洗衣机的宽度是{self.weith},洗衣机的高度是{self.height}')
# haier = Washer(1000, 2000)
# haier.wash()

# 烤串：examination

# # 创建考试的类
# class Examination:
#
#     # 创建属性
#     def __init__(self):
#         self.cook_time = 0
#         self.status = "初步状态"
#         self.subjects = []
#
#     # 创建考试方法
#     def write(self, time):
#         self.cook_time = self.cook_time + time
#         # print(f'目前已经写了{self.cook_time}分钟')
#         # 判断写了多长时间
#         if 0 < self.cook_time < 3:
#             self.status = "不合格"
#         elif 3 <= self.cook_time <= 8:
#             self.status = "即将合格"
#         elif self.cook_time >= 8:
#             self.status = "已合格"
#         # else:
#             # print("目前还未开始")
#     # 写的科目统计
#     def add_subjects(self, subject):
#         self.subjects.append(subject)
#
#     # 结果描述
#     def __str__(self):
#         return  f"目前已经写了{self.cook_time}分钟，成绩为{self.status},写的科目有{self.subjects}"
#
#
# # 调试
# if __name__ == '__main__':
#     reExamination = Examination()
#     # 输入考生时间
#     wtime = int(input('请输入考生时间:'))
#     reExamination.write(wtime)
#     # 判断是否时间是有效
#     if wtime<0:
#         print("目前还未开始")
#     else:
#         #时间有效后才可打印结果
#         wsubject = str(input('请输入考生科目:'))
#         reExamination.add_subjects(wsubject)
#         print(reExamination)

# 将小于房子面积的家具摆放到房子中

# 家具类
class Furniture:
    # 家具的种类,数量，大小
    def __init__(self, furname, furarea):
        self.furarea = furarea
        self.furname = furname

    # 返回的结果描述
    def __str__(self):
        return f'该家具是{self.furname},并且它的面积为{self.furarea}'


# 房子类
class House():
    # 房子的总面积
    def __init__(self, gross_area):
        self.gross_area = gross_area
        # 房子的剩余面积
        self.residual_area = self.gross_area
        # 家具的列表
        self.furniture_list = []

    # 摆放家具
    # 外界给予家具种类
    def add_furniture(self, furniture_type):
        # 判断家具大小是否小于房子剩余面积
        # while True:
            if furniture_type.furarea <= self.residual_area:
                # 如果小于，则加入家具列表中
                self.furniture_list.append(furniture_type.furname)
                # 此时房子的剩余面积为
                self.residual_area -= furniture_type.furarea
            else:
                print('房子空间不足')

    # 房子的结果描述
    def __str__(self):
        return f'房子的总面积为{self.gross_area},放入了{self.furniture_list}后,剩余房子的面积为{self.residual_area}'


if __name__ == '__main__':

    housearea = int(input('请输入房子的面积:'))
    # 实例化家具类
    i = 0
    while True:
        if i <= housearea:
            furnames = str(input('请输入要放的家具:'))
            furareas = int(input('请输入家具的面积:'))
            furnitureing = Furniture(furnames, furareas)
            houseing = House(housearea)
            houseing.add_furniture(furnitureing)
            print(houseing)
            i += furareas
        else:
            print('空间不足')
