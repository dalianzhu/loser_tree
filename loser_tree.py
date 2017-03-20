isdebug = True


def debug(str):
    if isdebug:
        print(str)


class LoserTree(object):
    """
    参考资料：http://www.cnblogs.com/qianye/archive/2012/11/25/2787923.html

    实现一个败者树，关键在于不断更新父节点（不是叶子节点）的值。
    在一个固定的多路输入中，父节点的数量是固定的，等于输入路数。
    比如，5路输入，它们的树结构如下所示：
                    ※ -- ls[0]
                     \
                    ※ --ls[1]
                   /  \
           ls[2]--※  ※ --ls[3]
                 /
    ls[5]--    ※

    ls节点下可以挂叶子。ls[5]节点是 第4,5路输入的父节点
    它们的关系为 parent = (index + input_counts - 1) / 2，index 可以等于5
    每次败者竞赛之后，ls[0]保存最终胜利者
    具体的一个例子，见testcase。
    """
    def __init__(self, input_counts):
        self.loser_tree_node = [0 for x in range(input_counts)]


    def build(self, input_arr):
        self.leaves = [-65535] + input_arr
        self.nodes_count = len(input_arr)

        for i in range(self.nodes_count, 0, -1):
            self.adjust(i);

    def adjust(self, index):
        k = self.nodes_count
        parent = (k - 1 + index) // 2
        while parent > 0:
            if self.leaves[index] > self.leaves[self.loser_tree_node[parent]]:
                # 值大者败
                # 进入此条件，说明leaves[index]是败者。所以对它的父节点进行赋值。
                self.loser_tree_node[parent], index = index, self.loser_tree_node[parent]
                # 交换后，index变成了优胜者
                # 求出parent的parent，进入下一轮循环。
            parent = parent // 2

        # 循环结束后，index一定是最后的优胜者，把最后的优胜者保存在ls[0]中。
        self.loser_tree_node[0] = index