from loser_tree import LoserTree, debug


def test_case_1():
    """
    用例说明：
    首先有一棵这样的树：
                [0]
              /     \
            [0]    [0]
            /
          [0]
    方括号为loser_tree_node。初始化值为0。0号元素为-∞（这里为-65535）。

    1.添加 值为 12 的node5。根据公式，它的父节点为ls4，开始竞赛。

               ls1[0]
              /     \
         ls2[0]    ls3[0]
            /
          ls4[0]
            \
            (12,index=5)
    ls4中保存的为node0(val= -∞)。12 > -∞。所以 12 败。将 12 的index记录在ls4中。
                ls1[0]
              /     \
         ls2[0]    ls3[0]
            /
          ls4[5]
            \
            (12,index=5)
    此时的胜者为node0(val=-∞),node 0 再次与ls2中的值竞赛，ls2中保存的也是node0。 -∞ ！< -∞。不修改ls2。
    同理，此时的胜者为node0。与ls1比较，也不会修改ls1值。

    2.添加 值为 6 的Node。根据公式，它的父为ls4。
                ls1[0]
              /     \
         ls2[0]    ls3[0]
            /
          ls4[5]
         /       \
    (6,index=4) (12,index=5)
    ls4中保存的现在是node5（val=12）。node4与ls4中node5竞赛。6 ！〉 12，所以不修改ls4的值，胜者仍然为
    node4(val=6)。
    然后node4(val=6)再与ls2中的Node0(val=-∞)竞赛。6 〉-∞。node4败，所以更新ls2的值为node4。

                       ls1[0]
                      /     \
    更新ls2的值-->ls2[4]    ls3[0]
                    /
                  ls4[5]
                 /       \
            (6,index=4) (12,index=5)

    此时在ls2上竞赛后的胜者为node0(val=-∞)。node0将会与ls1上的node0进行竞赛。显然不用更新ls1的值。

    依照上面的规则，不断的更新。
    在更新的过程中同时将每轮最后的胜利者保存在ls[0]上，最后会生成败者树。
    最终结果如下：
                           ls0[4]
                              /
                            ls1[2]
                      /                    \
                 ls2[1]                    ls3[3]
                /     \                   /       \
            ls4[5]   (10,index=1)  (9,index=2) (20,index=3)
          /       \
    (6,index=4) (12,index=5)

    我们得到了本轮最终竞赛的最小值，node4(val=6)。
    """
    debug("test_case_1 start")
    test_arr = [10, 9, 20, 6, 12]
    ls_tree = LoserTree(5)
    ls_tree.build(test_arr)
    debug("ls_tree.leaves {}".format(ls_tree.leaves))
    debug("ls_tree.loser_tree_node {}".format(ls_tree.loser_tree_node))
    winner_index = ls_tree.loser_tree_node[0]
    winner_val = ls_tree.leaves[winner_index]
    debug("ls_tree winner(minimum) index is {} value is {}".format(winner_index, winner_val))
    assert winner_index == 4
    assert winner_val == 6


test_cases = [
    test_case_1,
]

for item in test_cases:
    item()
