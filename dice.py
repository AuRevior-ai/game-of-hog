"""Functions that simulate dice rolls.

A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

Types of dice:

 -  Dice can be fair, meaning that they produce each possible outcome with equal
    probability. Examples: four_sided, six_sided骰子可以是四面的也可以是六面的,但是骰子丢出来的各个值必须是等可能的

 -  For testing functions that use dice, deterministic test dice always cycle
    through a fixed sequence of values that are passed as arguments to the
    make_test_dice function.
"""

from random import randint#引用随机数头文件

def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'#保证值是整数并且大于等于一（我居然看懂了，抽象）
    def dice():
        return randint(1,sides)#dice函数可以返回1到sides之间的所有值,包括端点值
    return dice#返回的是一整个函数,也就是说,整个make_fair_dice函数的意思是,传进去一个数,然后等可能的生成端点之间的所有数值

four_sided = make_fair_dice(4)#意思即是print(four_sided)可能生成1到4之间的任何整数,并且它们是等可能的
six_sided = make_fair_dice(6)#同理,这样子就实现了一个表达式,但是它可能是不同的值

def make_test_dice(*outcomes):#python加*指的是可变数量的参数,不是解引用或者指针或者首地址,他妈的
    """Return a die that cycles deterministically through OUTCOMES.保证调用函数的时候可以循环输出输入的参数

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'#确保输入了参数
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'#对于所有的值,确保是整数,并且是正数
    index = len(outcomes) - 1#定义序号是长度减一
    def dice():
        nonlocal index#nonlocal前缀是告诉编译器:当前这个变量不是当前作用域下的变量,而是外部作用域中的变量
        #也就是说这个时候的index还是len(outcomes) - 1
        index = (index + 1) % len(outcomes)#然后就是一个很正常的循环输入
        return outcomes[index]#返回值
    return dice#返回函数,也就是说,这里实际上是实现了循环
#python ok -q 00 -u --local
#python ok -q 00 --local
#python -i hog.py
