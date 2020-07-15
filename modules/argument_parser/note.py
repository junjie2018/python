import argparse

"""
    prog:
    usage:
    description:
    epilog:
    parents:
    formater_class:
    prefix_chars:
    fromfile_prefix_chars:
    argument_default:
    conflict_handler:
    add_help
    allow_abbbrev
"""

# 这块的description应该是对这个程序的描述
parser = argparse.ArgumentParser(
    # prog='PROG',
    # usage='USAGE',
    description='DESCRIPTION',
    epilog='thank to use, having a happy day',  # 这个地方改为我的个人介绍信息，B格很好
    parents=[],
    # formatter_class=
    # prefix_chars='*'
)
args = parser.parse_args()
# 这个metavar怎么理解呀

# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an inter for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

"""
    调用parse_args()将会返回一个拥有integers和accumulate属性的对象。integers属性将会
    是一个列表，其中包好一个或多个int值；如果命令行中含有--sum，这accumulate将会使sum()
    如果命令行中不包含该参数，则其为max方法。
    
    大多数情况下，调用parse_args()意味着一个简单的包含从命令行中解析出来的属性的Namespace
    对象将会被创建。
    
    我对Namespace对象还不熟，《Python学习手册》中貌似没有讲到这个对象
"""

# print(args.accumulate(args.integers))
