import numpy
class TinyStatistician:

    def __init__(self):
        pass

    def mean(self, lst):
        if len(lst) > 0:
            return float(sum(lst)/len(lst))
        return None

    def median(self, lst):
        if len(lst) > 0:
            lst.sort()
            return self.calc(lst, 0.5)
        return None

    def calc(self, lst, pos):
        index = float(len(lst) - 1) * pos
        if (index).is_integer():
            return float(lst[int(index)])
        n1 = lst[int(index)]
        n2 = lst[int(index) + 1]
        quart = n1 * (1 - pos) + n2 * pos
        return quart

    def quartile(self, lst):
        if len(lst) > 0:
            lst.sort()
            result = list()
            result.append(self.calc(lst, 0.25))
            result.append(self.calc(lst, 0.75))
            return result
        else:
            return None

    def var(self, lst):
        if len(lst) > 0:
            mean = self.mean(lst)
            var = 0.0
            for elem in lst:
                var += (elem - mean) * (elem - mean)
            var = var / len(lst) - 1
            return var
        else:
            return None

    def std(self, lst):
        if len(lst) > 0:
            mean = self.mean(lst)
            dev = 0.0
            for elem in lst:
                dev += (elem - mean) * (elem - mean)
            dev = dev / len(lst)
            dev = dev**(0.5)
            return dev
        else:
            return None

if __name__ == '__main__':
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.median(a))
    #print(numpy.median(a))
    # Expected result: 42.0
    print(tstat.quartile(a))
    #print(numpy.quantile(a, 0.25))
    #print(numpy.quantile(a, 0.75))
    # Expected result: [10.0, 59.0]
    print(tstat.var(a))
    #print(numpy.var(a))
    # Expected result: 12279.439999999999
    print(tstat.std(a))
    #print(numpy.std(a))
    # Expected result: 110.81263465868862