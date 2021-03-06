"""
    在Python中，同时运行多个任务有两种基本做法：进程分支和线程分支。从功能上看，二者均属于操作系统
    的底层服务来并行地执行Python代码。从操作步骤上来看，二者在接口，跨平台移植性和通信方面都有很大
    差异。

    所有主流平台都能执行Python的线程，此外os.spawn函数和方法集提供了类似分支而无平台相关的方法来启
    动程序，还有我们在第2章和第3章学到的os.popen和os.system调用，以及subprocess模块也可用于跨平台
    移植使用Shell命名派生程序。新模块multiprocessing也提供了其他方法，用于在多情境下运行多个进程。

    本章会重点介绍更直接的技巧如分叉、线程、管道、信号、套接字，以及其他启动技巧；还会使用支持它们
    的Python内建工具，如os.fork调用，还有threading、queue和multiprocessing模块。
"""