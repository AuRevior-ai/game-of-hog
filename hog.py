"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice#引用模块,分别是1到6内的随机数,1到4内的随机数,还有那个循环返回参数数量的函数
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

######################
# Phase 1: Simulator #任务一,模拟
######################


def roll_dice(num_rolls, dice=six_sided):#输入两个参数,一个是骰子的数量,一个是dice,它是零到六之间的随机数
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.
    试着模拟丢骰子的情况,并且骰子的数量大于一,在正常情况下返回骰子的点数之和,但是如果骰子里面出现了一个1,那么就返回一
    注意实际上的操作是将骰子一起丢出去的,所以这里一定要全部丢完,不能提前终止
    num_rolls:  The number of dice rolls that will be made.这个是骰子的数量
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'#保证骰子的数量是整数
    assert num_rolls > 0, 'Must roll at least once.'#保证骰子的数量为正
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"#孩子们,我要开始写代码了
    sum_score = 0
    pig_out_occurred = False

    for _ in range(num_rolls):
        outcome = dice()  # 调用 dice() 获取单次掷骰子的结果
        if outcome == 1:
            pig_out_occurred = True  # 如果掷出1，标记 Pig Out 发生
        sum_score += outcome  # 累加得分

    return 1 if pig_out_occurred else sum_score
    # END PROBLEM 1
#python ok -q 01 -u --local
#python ok -q 01 --local
#python -i hog.py


def free_bacon(score):#这是那个不丢骰子直接拿分的规则，传入的值是对方此时的分数
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'#保证值小于100，不然游戏就结束了
    pi = FIRST_101_DIGITS_OF_PI#前一百零一位，也是十分甚至九分的抽象

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    if score==0:
        return 6#当对手的分数是0的时候，直接返回6
    # END PROBLEM 2
    m=pow(10,100-score)
    pi=pi//m#假设score=1,那么这里就需要留下的就是31
    return pi % 10 + 3
#python ok -q 02 -u --local
#python ok -q 02 --local
#python -i hog.py

def take_turn(num_rolls, opponent_score, dice=six_sided):#传入三个参数，骰子的数量，对手的得分，以及骰子，默认是六面
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.
    返回当前玩家的本轮得分
    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    #首先还是确保我们输入的数据是有效的
    assert type(num_rolls) == int, 'num_rolls must be an integer.'#丢的骰子数量需要是整数
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'#保证丢的骰子数量是0到10
    assert opponent_score < 100, 'The game should be over.'#确保游戏还没有结束
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls==0:
        score=free_bacon(opponent_score)#要是丢骰子的数量是0，那么调用那个规则
        return score
    else:#要是不为零的话
        score=roll_dice(num_rolls, dice)#要是不为零就直接丢吧，注意只要有一个1得分就是1
        return score
    # END PROBLEM 3
#python ok -q 03 -u --local
#python ok -q 03 --local
#python -i hog.py


def extra_turn(player_score, opponent_score):
    """Return whether the player gets an extra turn."""
    return (pig_pass(player_score, opponent_score) or
            swine_align(player_score, opponent_score))



def swine_align(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Swine Align.
    如果刚刚行动完的那个玩家所得到的总分和他对手的得分的最大公约数刚好大于等于十,那么刚刚结束行动的那个玩家会获得一次额外的行动机会
    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> swine_align(30, 45)  # The GCD is 15.
    True
    >>> swine_align(35, 45)  # The GCD is 5.
    False
    """
    # BEGIN PROBLEM 4a
    "*** YOUR CODE HERE ***"
    import math
    if player_score == 0 or opponent_score == 0:
        return False
    gcd = math.gcd(player_score, opponent_score)#用math模块里面的方法，直接求出最大公约数
    
    return gcd >= 10
    # END PROBLEM 4a
#python ok -q 04a -u --local
#python ok -q 04a --local
#python -i hog.py

def pig_pass(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Pig Pass.
    如果当前行动的玩家的得分小于对手,并且两人相差的分值小于3,那么刚刚行动的人会获得一次额外机会
    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> pig_pass(9, 12)
    False
    >>> pig_pass(10, 12)
    True
    >>> pig_pass(11, 12)
    True
    >>> pig_pass(12, 12)
    False
    >>> pig_pass(13, 12)
    False
    """
    # BEGIN PROBLEM 4b
    "*** YOUR CODE HERE ***"
    return player_score < opponent_score and (opponent_score - player_score) < 3#两个条件同时满足就可以，这个好理解
    # END PROBLEM 4b
#python ok -q 04b -u --local
#python ok -q 04b --local
#python -i hog.py

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.策略0,玩家0的策略函数
    strategy1:  The strategy function for Player 1, who plays second.策略1,玩家1的策略函数
    score0:     Starting score for Player 0  玩家0的初始得分
    score1:     Starting score for Player 1  玩家1的初始得分
    dice:       A function of zero arguments that simulates a dice roll. 一个没有参数的函数,用于模拟骰子
    goal:       The game ends and someone wins when this score is reached. 游戏结束并且其中一个人胜利
    say:        The commentary function to call at the end of the first turn. 暂时可以忽略,不用管他,这是一个评论函数
    """
    who = 0  # 这个是我们的当前玩家，0代表player0，1代表player1
    # BEGIN PROBLEM 5
    """
    别忘了我们的原型函数
    def roll_dice(num_rolls, dice=six_sided):#输入两个参数,一个是骰子的数量,一个是dice,它是零到六之间的随机数
    def free_bacon(score):#这是那个不丢骰子直接拿分的规则，传入的值是对方此时的分数
    def take_turn(num_rolls, opponent_score, dice=six_sided):#传入三个参数，骰子的数量，对手的得分，以及骰子，默认是六面
    def swine_align(player_score, opponent_score): 这是那个最大公约数大于等于十就返回true的函数
    def pig_pass(player_score, opponent_score):  这是那个差的分值小于3就返回true的函数
    """
    "*** YOUR CODE HERE ***"
    while True:
        if who == 0:
            nam_roils = strategy0(score0, score1)#现决定要丢几个，注意这个策略函数是给出了的，在下面有，它的作用就是给出当前回合最好丢出几个骰子
            score0 += take_turn(nam_roils, score1, dice)#然后加上当前回合得到的分数
            say = say(score0, score1)#这是一个评论报分函数，不过这里还不用管它
            if score0 >= goal or score1 >= goal:#要是这个玩家玩玩之后，游戏结束了，就直接跳出循环
                break
                # 之前上面是return，但底下有一个return，只能用break了
            if not extra_turn(score0, score1):#要是没有触发额外回合，那么就要交换我们所关注的那个玩家了
                who = other(who)
        if who == 1:#换人，然后重复上述步骤
            nam_roils = strategy1(score1, score0)
            score1 += take_turn(nam_roils, score0, dice)
            say = say(score0, score1)
            if score0 >= goal or score1 >= goal:
                break
            if not extra_turn(score1, score0):
                who = other(who)
#python ok -q 05 -u --local
#python ok -q 05 --local
#python -i hog.py
#python ok -q 05 --suite 2 --case 3 --local
#python ok --submit --local
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    
    # END PROBLEM 6
    return score0, score1
#python ok -q 06 -u --local
#python ok -q 06 --local
#python -i hog.py

#######################
# Phase 2: Commentary #评论
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores
"""
让我们举个例子
# 初始调用
update = say_scores(10, 20)

# 后续调用，使用上一次调用返回的函数
update = update(15, 25)
Player 0 now has 10 and Player 1 now has 20
Player 0 now has 15 and Player 1 now has 25
"""

def announce_lead_changes(last_leader=None):#非常重要的点就是闭包函数可以记住上一次调用的参数，并且内部函数可以直接调用外部函数的参数
    """Return a commentary function that announces lead changes.
    其实这里的相互调用闭包关系可以再理解一下
    >>> f0 = announce_lead_changes()  这里可以理解为函数赋值，由于外部函数announce_lead_changes返回的是内部函数say，于是
    >>> f1 = f0(5, 0)  实际上就是say(5,0),然后再进行调用实际上就是返回了一个新的闭包环境
    Player 0 takes the lead by 5  
    >>> f2 = f1(5, 12)  这就是说，每一次的调用实际上都是调用say函数，并不是外部函数
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):#这就是我们需要编写的评论函数了
        if score0 > score1:#要是玩家0的分数高，那么我们就先关注玩家0
            leader = 0#将领先者设置为0
        elif score1 > score0:
            leader = 1#反之，就设置为玩家1
        else:
            leader = None#要是相等的话，就没人领先
        if leader != None and leader != last_leader:#要是存在领先者并且领先者和上一次不一样
            print('Player', leader, 'takes the lead by', abs(score0 - score1))#那么我们就要发表评论
        return announce_lead_changes(leader)#返回
    return say
"""
再来举个例子
f0 = announce_lead_changes()

# 模拟比赛过程中的分数变化
f1 = f0(5, 0)  # Player 0 takes the lead by 5
f2 = f1(5, 12) # Player 1 takes the lead by 7
f3 = f2(8, 12) # 无输出，因为领先者没有改变
f4 = f3(8, 13) # 无输出，因为领先者没有改变
f5 = f4(15, 13) # Player 0 takes the lead by 2
"""

def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


 
def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.
    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest
    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 11)
    11 point(s)! That's the biggest gain yet for Player 1
    >>> f3 = f2(20, 11)
    >>> f4 = f3(13, 20)
    >>> f5 = f4(20, 35)
    15 point(s)! That's the biggest gain yet for Player 1
    >>> f6 = f5(20, 47) # Player 1 gets 12 points; not enough for a new high
    >>> f7 = f6(21, 47)
    >>> f8 = f7(21, 77)
    30 point(s)! That's the biggest gain yet for Player 1
    >>> f9 = f8(77, 22) # Swap!
    >>> f10 = f9(33, 77) # Swap!
    55 point(s)! That's the biggest gain yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    def commentary(score0, score1, last_score=last_score, running_high=running_high):#评论函数，传入参数是玩家0的分数，玩家1的分数，对应玩家上一次的分数以及目前的最高增长分数
        if who ==0:#首先选择玩家
            if score0-last_score>running_high:#要是当前得分减去上次得分大于目前的最大增长值，
                print("{0} point(s)! The most yet for Player {1}".format(score0-last_score, who))#就输出相应语句，这里用的是占位符的方法
                running_high=score0-last_score#然后我们就可以更新一下目前的增长最大值
            return announce_highest(who, last_score=score0, running_high=running_high)#返回一个新的闭包环境，它记住了上一个闭包环境的各种参数
        elif who ==1:#换人，重复上述步骤
            if score1-last_score>running_high:
                print("{0} point(s)! The most yet for Player {1}".format(score1-last_score, who))
                running_high=score1-last_score
            return announce_highest(who, last_score=score1, running_high=running_high)
    return commentary#哎呀，这个闭包环境实在是不太好理解，我加油
    # END PROBLEM 7
#python ok -q 07 -u --local
#python ok -q 07 --local
#python -i hog.py
#python ok -q 07 --suite 2 --case 2 --local

#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.
    返回一个函数,被返回的那个函数返回了初始函数的平均值
    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)#丢一千个这么个骰子,输出的期望值是3.0
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    from statistics import mean

    def averaged_function(*args):#多参数的函数啦
        results = [original_function(*args) for _ in range(trials_count)]#创建一个列表，里面的内容是，对trials_count这么多的数据
        #对这些数据一个一个用original_fuunctional函数进行操作,然后放到这个列表里面
        return sum(results) / len(results) if results else 0#然后就可以求出列表的平均值,要是不是零的话

    return averaged_function#闭包环境,该死的闭包环境!!!!知道我理解这个需要花多长时间吗?????!!!!!
    # END PROBLEM 8
#python ok -q 08 -u --local
#python ok -q 08 --local
#python -i hog.py

def max_scoring_num_rolls(dice=six_sided, trials_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.
    返回投掷骰子的次数(一轮中),使得这一轮的平均得分达到最高,要是有多个平均得分相同的,那么返回骰子次数最少的
    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    averaged_roll_dice = make_averaged(roll_dice, trials_count)#这个是丢骰子的得分均值函数
    best_num_rolls = 0#最高分的骰子数量
    max_average_score = 0#最高的期望得分,初始化为0

    for num_rolls in range(1, 11):#骰子的数量限制
        average_score = averaged_roll_dice(num_rolls, dice)#将均值得分赋值为得分均值
        if average_score > max_average_score:#要是这个期望比目前的最大值高
            max_average_score = average_score#那么就要重新赋值
            best_num_rolls = num_rolls#这个参数当然也要变化啦

    return best_num_rolls#然后返回
    # END PROBLEM 9
#python ok -q 09 -u --local
#python ok -q 09 --local
#python -i hog.py

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test extra_turn_strategy
        print('extra_turn_strategy win rate:', average_win_rate(extra_turn_strategy))

    if False:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"



def bacon_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    当使用 Free Bacon 规则可以获得至少 cutoff 分时,bacon_strategy 应该返回 0:否则，它应该返回 num_rolls,即按照常规掷骰子。
    """
    # BEGIN PROBLEM 10
    # Calculate the score from using Free Bacon
    bacon_score = free_bacon(opponent_score)
    # 决定是否要使用freebacon函数
    if bacon_score >= cutoff:
        return 0
    else:
        return num_rolls#这个太简单了傻子都会,主要还是前面的几个闭包函数比较抽象
    # END PROBLEM 10
#python ok -q 10 -u --local
#python ok -q 10 --local
#python -i hog.py
import math
def extra_turn_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers an extra turn. It also
    rolls 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it rolls NUM_ROLLS.
    优先触发额外轮次：如果掷 0 个骰子可以触发额外轮次（通过 Pig Pass 或 Swine Align 规则），则返回 0。
    使用 Free Bacon:如果掷 0 个骰子可以获得至少 cutoff 分，则返回 0。
    默认行为：否则，返回 num_rolls,即按照常规掷骰子。
    """
    # BEGIN PROBLEM 11
    bacon_score = free_bacon(opponent_score)
    new_score = score + bacon_score

    # 看看有没有额外回合的触发,其实这两个函数在前面就定义过了,写在这里只是提醒自己别忘了规则
    """def pig_pass(new_score, opponent_score):
        return new_score < opponent_score and (opponent_score - new_score) < 3

    def swine_align(new_score, opponent_score):
        return math.gcd(new_score, opponent_score) >= 10"""

    if pig_pass(new_score, opponent_score) or swine_align(new_score, opponent_score):
        return 0
    else:
        return bacon_strategy(score, opponent_score, cutoff, num_rolls)
    # END PROBLEM 11
#python ok -q 11 -u --local
#python ok -q 11 --local
#python -i hog.py

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Replace this statement
    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()

# 好了,终于写完了,主要还是闭包函数的逻辑比较难以理解,其它的部分还是非常简单的