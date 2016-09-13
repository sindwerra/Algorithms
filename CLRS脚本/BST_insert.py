# coding=utf-8

def insert(head, x):
    """
    :二分搜索树插入函数的实现
    :type head: 二分搜索树头节点
    :type x: 需要插入的树的节点
    """
    fir, sec = head, None

    # 搜索确定x应该安放的具体位置, fir最后指向的None
    # 即为最后的应安放的位置

    while fir != None:
        sec = fir
        if x.val < fir.val:
            fir = fir.left
        else: fir = fir.right

    # 第一种判定是否树本身为空
    # 第二种判定x值小于sec
    # 第三种判定x值大于sec

    if sec == None:
        head = x
    elif sec.val > x.val:
        sec.left = x
    else:
        sec.right = x

    return head         # 返回头节点
