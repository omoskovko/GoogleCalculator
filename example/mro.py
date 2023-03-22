# <mro.py>

"""C3 algorithm by Samuele Pedroni."""


class str_meta(type):
    "All classes are metamagically modified to be nicely printed"

    def __repr__(self):
        return self.__name__


class ex_2:
    "Serious order disagreement"  # From Guido

    class O(metaclass=str_meta):
        pass

    class X(O):
        pass

    class Y(O):
        pass

    class A(X, Y):
        pass

    class B(Y, X):
        pass

    try:

        class Z(A, B):
            pass  # creates Z(A,B) in Python 2.2

    except TypeError:
        pass  # Z(A,B) cannot be created in Python 2.3


class ex_5:
    "My first example"

    class O(metaclass=str_meta):
        pass

    class F(O):
        pass

    class E(O):
        pass

    class D(O):
        pass

    class C(D, F):
        pass

    class B(D, E):
        pass

    class A(B, C):
        pass


class ex_6:
    "My second example"

    class O(metaclass=str_meta):
        pass

    class F(O):
        pass

    class E(O):
        pass

    class D(O):
        pass

    class C(D, F):
        pass

    class B(E, D):
        pass

    class A(B, C):
        pass


class ex_9:
    "Difference between Python 2.2 MRO and C3"  # From Samuele

    class O(metaclass=str_meta):
        pass

    class A(O):
        pass

    class B(O):
        pass

    class C(O):
        pass

    class D(O):
        pass

    class E(O):
        pass

    class K1(A, B, C):
        pass

    class K2(D, B, E):
        pass

    class K3(D, A):
        pass

    class Z(K1, K2, K3):
        pass


def merge(seqs):
    print("-------------")
    print("CPL[{0}]={1}".format(seqs[0][0], seqs))
    print("-------------")
    res = []
    i = 0
    cand = seqs[0][0]
    while 1:
        nonemptyseqs = [seq for seq in seqs if seq]

        if not nonemptyseqs:
            return res
        print("{1}+=merge({0})".format(nonemptyseqs, res))

        i += 1
        # print(i,'round: candidates...')
        for seq in nonemptyseqs:  # find merge candidates among seq heads
            cand = seq[0]
            print(i, "round: ", cand)
            nothead = [s for s in nonemptyseqs if cand in s[1:]]
            if nothead:
                print(i, "round: ", cand, "in", nothead, "not candidate")
                cand = None  # reject candidate
            else:
                break
        if not cand:
            raise Exception("Inconsistent hierarchy")
        res.append(cand)
        for seq in nonemptyseqs:  # remove cand
            if seq[0] == cand:
                del seq[0]


def mro(C):
    "Compute the class precedence list (mro) according to C3"
    return merge([[C]] + list(map(mro, C.__bases__)) + [list(C.__bases__)])


def print_mro(C):
    print("\nMRO[%s]=%s" % (C, mro(C)))


print_mro(ex_5.A)

# </mro.py>
