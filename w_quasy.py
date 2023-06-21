from utils import *
from quasi_distr import QGen, QuasyDistr

def w1(vals, index, predicted_val):

    abs_errs = vals_to_absolute_errors(vals, predicted_val)
    sigma_errs = get_sigma_array_errs(abs_errs, index)
    qgen = QGen(abs_errs)
    w=0
    for i in range(len(sigma_errs)):
        sigma_err = sigma_errs[i]
        distance = abs(i-index)+1

        quasy_distr = qgen.get_distr_of_minimum(distance)
        p_of_err = quasy_distr.get_p_event_lesser_errs(sigma_err)
        w+=p_of_err
    return w


def w2(vals, index, predicted_val):
    abs_errs = vals_to_absolute_errors(vals, predicted_val)
    sigma_errs = get_sigma_array_errs(abs_errs, index)
    qgen = QGen(abs_errs)
    w = 0

    for i in range(len(sigma_errs)):
        sigma_err = sigma_errs[i]
        distance = abs(i - index) + 1

        quasy_distr = qgen.get_distr_of_minimum(distance)
        mean_quasy = quasy_distr.get_mean()
        divider = sum(vals)/len(vals)
        w += (mean_quasy - sigma_err)/divider
    return w

