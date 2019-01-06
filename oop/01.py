'''
定义一个学生的类,用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类,pass代表直接跳过
    # 此处必须有pass
    pass
# 定义一个具体的学生(对象)
feifei = Student()

# 再定义一个类,描述学Python的学生
class PythonStudent():
    # 用None给不确定的属性赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1.def doHomework缩进层级
    # 2.系统默认一个self参数
    def doHomework(self):
        print("我在做作业")
        # 推荐在函数末尾使用return语句
        return None
# 实例化一个叫ff的学生,一个具体的人
ff = PythonStudent()
print(ff.name)
# 成员函数的调用没有传递参数,默认参数self
ff.doHomework()
print(ff.age)
ff.course