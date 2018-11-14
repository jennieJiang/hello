最近自学机器学习，用python实现算法，编程基础薄弱，疯狂补课中。
一直没搞明白__init__，知乎上看到几个回答比较通俗易懂，搬来给自己做个笔记，方便复习

Python中 __init__的通俗解释？ - cloudream的回答 - 知乎
https://www.zhihu.com/question/46973549/answer/293788116
Python中 __init__的通俗解释？ - 留德华叫兽的回答 - 知乎
https://www.zhihu.com/question/46973549/answer/476331606

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
class后面定义了一个类，类有各种参数(属性)和功能(方法)，比如‘人’这个类，就有名字‘name’和年龄‘age’等属性，self是一个指向对象的指针，即表示对象本身，**谁调用，就表示谁**
__init__对新创建的对象的属性进行初始化，方便实现一个类多个对象的创建
例如：
```
p1=Person('Jim',12)
print(p1.age)
```

```
>>>12
```
这里self就是p1，即Jim这个对象

```
p1=Person('Lili',20)
print(p1.age)
```

```
>>>20
```
此时self就表示Person('Lili',20)这个对象，在这个Person('Lili',20)对象的创建过程中，使用了__init__的初始化属性功能

接下来在类Person中定义一个方法，用于自我介绍，完整代码如下：

```
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def describ(self):
        print('I am %s,I am %d years old' %(self.name,self.age))

p1=Person('Lily',20)
print(p1.describ())
```

```
>>> I am Lily,I am 20 years old
```


