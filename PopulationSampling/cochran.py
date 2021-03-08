class Cochran:
    @staticmethod
    def cochran(data, seeds, nums):
        ZScore = Zsc.zsc(seeds,data)
        pp = PopulationProportion.populationPorportion(seeds, nums, data)
        MarOfError = MarginOfError.marginOfError(seeds, data)
        sub = Subtraction.difference(1, pp)
        cochran = (Exponent.power(ZScore, 2) * pp * sub) / Exponent.power(MarOfError, 2)
        return 
