
import random

class QuasyDistr:
    def __init__(self, errs_sample):
        self.uniq_errs = []
        self.ps = []
        self._get_ps_from_sample(errs_sample)

    def _get_ps_from_sample(self, errs):
        ps = []
        self.uniq_errs = list(set(errs))
        for element in self.uniq_errs:
            ps.append(errs.count(element))
        self.ps = list([x/len(errs) for x in ps])


    def get_p_event_lesser_errs(self, err):
        p=0
        for i in range(len(self.uniq_errs)):
            if self.uniq_errs[i] <= err:
                p += self.ps[i]
        return p

    def get_mean(self):
        mean = 0
        for i in range(len(self.uniq_errs)):
            mean += self.uniq_errs[i] * self.ps[i]
        return mean


class QGen:
    def __init__(self, errs):
        self.errs = errs
        self.SIZE_SAMPLING = 400

    def get_distr_of_minimum(self, sample_len):
        sample_min_errs = []
        for i in range(self.SIZE_SAMPLING):
            random_sample =random.sample(self.errs, sample_len)
            sample_min_errs.append(min(random_sample))
        distr_of_mins = QuasyDistr(sample_min_errs)
        return distr_of_mins



