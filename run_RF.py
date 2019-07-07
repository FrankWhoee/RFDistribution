from ete3 import Tree
import RF

def test(newick):
    tree = Tree(newick)
    print(RF.polynomial(tree, tree.get_leaves().__len__() + 1))

# 8 tip
# newick ="(((t2:0.8727817549,(t1:0.4722830437,t3:0.5129283739):0.02436175128):0.7209995012,(t4:0.06786046806,t6:0.7481567271):0.07053013402):0.5619613971,((t7:0.1686784215,t8:0.2114313007):0.1445601732,t5:0.8294858425):0.6152706817);"
# 4 tip
newick = "(((t3:0.1943115185,t1:0.5272119145):0.009663451463,t2:0.7607416636):0.3779389253,t4:0.6556323681);"
# 7 tip
# newick = "((((t6:0.9997730749,t5:0.7224498999):0.9447174252,t7:0.2788554211):0.5613310144,t1:0.239701811):0.6714769001,((t2:0.3941503041,t4:0.9353253739):0.5277405111,t3:0.4965463369):0.5105549153);"

# phy
test("(((A,B),(C,D)),((A,B),(C,D)));")
test("((((A,B),(C,D)),((A,B),(C,D))),(((A,B),(C,D)),((A,B),(C,D))));")
test("(((((A,B),(C,D)),((A,B),(C,D))),(((A,B),(C,D)),((A,B),(C,D)))),((((A,B),(C,D)),((A,B),(C,D))),(((A,B),(C,D)),((A,B),(C,D)))));")
test("((((((A,B),(C,D)),((A,B),(C,D))),(((A,B),(C,D)),((A,B),(C,D)))),((((A,B),(C,D)),((A,B),(C,D))),(((A,B),(C,D)),((A,B),(C,D))))),(((((A,B),(C,D)),((A,B),(C,D))),(((A,B),(C,D)),((A,B),(C,D)))),((((A,B),(C,D)),((A,B),(C,D))),(((A,B),(C,D)),((A,B),(C,D))))));")

# phyCat
test("(((((((A,B),C),D),E),F),G),H);")
test("(((((((((((((((A,B),C),D),E),F),G),H),H),H),H),H),H),H),H),H);")
test("(((((((((((((((((((((((((((((((A,B),C),D),E),F),G),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H);")
test("(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((A,B),C),D),E),F),G),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H),H);")