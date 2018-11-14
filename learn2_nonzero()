np.nonzero(a)表示返回a中不为0的元素的下标，
(1)对于一维布尔值类型False即为0

```
{
    b1=np.array('True','False','True','False')
    np.nonzero(b1)
        array((0,2),)
}
```

(2)对于二维数组,nonzero（a）函数一般返回两行array（）。如果mat（）一下，就是个2*N 的矩阵
N 表示的是矩阵a中不为0的元素个数
转载自 https://blog.csdn.net/u010315668/article/details/80204973
例：

```
{   b=np.array([[1,1,1,1,0,0,1],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]])
    c=np.nonzero(b)
    print(np.mat(c))
}
```

> 输出结果如下：
[[0 0 0 0 0 1 1 1 1 2 2 2]     表示b中第几行
 [0 1 2 3 6 0 2 4 6 1 3 5]]     表示b中第几列
 表示b[0,0],b[0,1]等元素为非零元素
 
(3)机器学习实战-SVM

```
{   ec=np.mat(np.zeros((3,2)))
    print(ec,'---1--')
}
```
输出：
    [[0. 0.]
    [0. 0.]
    [0. 0.]] ---1--
 
 ```
 {  ec[1]=[1,2]
    ec[2]=[3,4]
    print(ec,'----2--')
    print(ec[:,0])
 }
 ```
 
 输出：
 [[0. 0.]
 [1. 2.]
 [3. 4.]] ----2--
 
 ```
 {  validEliast1=np.nonzero(ec[:,0])
    print(validEliast1)
 }
 ```
输出：
[[0.]
 [1.]
 [3.]]
(array([1, 2], dtype=int64), array([0, 0], dtype=int64))  >第一个元素[1,2]表示第几行，第二个元素[0,0]表示第几列，合在一起即为[1,0],[2,0]为非零元素


```
{   validEliast=np.nonzero(ec[:,0].A)[0]
    print(validEliast)
}
```

输出：
[1 2]
