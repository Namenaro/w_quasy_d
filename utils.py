def vals_to_absolute_errors(vals, val_predicted):
    abs_errors = []
    for val in vals:
        val_err = abs(val - val_predicted)
        abs_errors.append(val_err)

    return abs_errors


def get_sigma_array_errs(errs, index):
    # перебираем левее на начиная с ближайших индексов
    err = errs[index]
    i = index
    lefts_arr = []
    current_best_err = err
    while True:
        new_index = i - 1
        if new_index < 0:
            break
        new_err = errs[new_index]
        if new_err < current_best_err:
            current_best_err = new_err
        lefts_arr.append(current_best_err)
        i = new_index
    lefts_arr = list(reversed(lefts_arr))

    # перебираем левее на начиная с ближайших индексов
    i = index
    rights_arr = []
    current_best_err = err
    while True:
        new_index = i + 1
        if new_index == len(errs):
            break
        new_err = errs[new_index]
        if new_err < current_best_err:
            current_best_err = new_err
        rights_arr.append(current_best_err)
        i = new_index

    best_errs_left_rigt = lefts_arr + [err] + rights_arr
    return best_errs_left_rigt