import sys
from scipy import stats
import yaml

trial_amount = int(sys.argv[1])
num_diff_sizes = 6

sort_cpu_data = [0] * num_diff_sizes
sort_mem_data = [0] * num_diff_sizes
sort_max_data = [0] * num_diff_sizes

hash_cpu_data = [0] * num_diff_sizes
hash_mem_data = [0] * num_diff_sizes
hash_max_data = [0] * num_diff_sizes

selection_cpu_data = [0] * num_diff_sizes
selection_mem_data = [0] * num_diff_sizes
selection_max_data = [0] * num_diff_sizes

projection_cpu_data = [0] * num_diff_sizes
projection_mem_data = [0] * num_diff_sizes
projection_max_data = [0] * num_diff_sizes

join_cpu_data = [0] * num_diff_sizes
join_mem_data = [0] * num_diff_sizes
join_max_data = [0] * num_diff_sizes

i = 1
linesPerSecond = 20_000
numberOfCores = 12
divisor = linesPerSecond * numberOfCores

#add variables for all other sizes
while i <= trial_amount:
    ## SORT ##
    sort_cpu_max_100 = open("sort_cpu_100_" + str(i) + ".txt", "r")
    sort_cpu_data[0] += float(sort_cpu_max_100.readline().rstrip("\n"))/divisor
    sort_max_data[0] += float(sort_cpu_max_100.readline().rstrip("\n"))/numberOfCores

    sort_cpu_max_1000 = open("sort_cpu_1000_" + str(i) + ".txt", "r")
    sort_cpu_data[1] += float(sort_cpu_max_1000.readline().rstrip("\n"))/divisor
    sort_max_data[1] += float(sort_cpu_max_1000.readline().rstrip("\n"))/numberOfCores

    sort_cpu_max_10000 = open("sort_cpu_10000_" + str(i) + ".txt", "r")
    sort_cpu_data[2] += float(sort_cpu_max_10000.readline().rstrip("\n"))/divisor
    sort_max_data[2] += float(sort_cpu_max_10000.readline().rstrip("\n"))/numberOfCores

    sort_cpu_max_30000 = open("sort_cpu_30000_" + str(i) + ".txt", "r")
    sort_cpu_data[3] += float(sort_cpu_max_30000.readline().rstrip("\n"))/divisor
    sort_max_data[3] += float(sort_cpu_max_30000.readline().rstrip("\n"))/numberOfCores

    sort_cpu_max_60000 = open("sort_cpu_60000_" + str(i) + ".txt", "r")
    sort_cpu_data[4] += float(sort_cpu_max_60000.readline().rstrip("\n"))/divisor
    sort_max_data[4] += float(sort_cpu_max_60000.readline().rstrip("\n"))/numberOfCores

    sort_cpu_max_100000 = open("sort_cpu_100000_" + str(i) + ".txt", "r")
    sort_cpu_data[5] += float(sort_cpu_max_100000.readline().rstrip("\n"))/divisor
    sort_max_data[5] += float(sort_cpu_max_100000.readline().rstrip("\n"))/numberOfCores

    sort_mem_100 = open("sort_mem_100_" + str(i) + ".txt", "r")
    sort_mem_data[0] += float(sort_mem_100.readline().rstrip("\n"))

    sort_mem_1000 = open("sort_mem_1000_" + str(i) + ".txt", "r")
    sort_mem_data[1] += float(sort_mem_1000.readline().rstrip("\n"))

    sort_mem_10000 = open("sort_mem_10000_" + str(i) + ".txt", "r")
    sort_mem_data[2] += float(sort_mem_10000.readline().rstrip("\n"))

    sort_mem_30000 = open("sort_mem_30000_" + str(i) + ".txt", "r")
    sort_mem_data[3] += float(sort_mem_30000.readline().rstrip("\n"))

    sort_mem_60000 = open("sort_mem_60000_" + str(i) + ".txt", "r")
    sort_mem_data[4] += float(sort_mem_60000.readline().rstrip("\n"))

    sort_mem_100000 = open("sort_mem_100000_" + str(i) + ".txt", "r")
    sort_mem_data[5] += float(sort_mem_100000.readline().rstrip("\n"))

    ## HASH ##
    hash_cpu_max_100 = open("hash_cpu_100_" + str(i) + ".txt", "r")
    hash_cpu_data[0] += float(hash_cpu_max_100.readline().rstrip("\n"))/divisor
    hash_max_data[0] += float(hash_cpu_max_100.readline().rstrip("\n"))/numberOfCores

    hash_cpu_max_1000 = open("hash_cpu_1000_" + str(i) + ".txt", "r")
    hash_cpu_data[1] += float(hash_cpu_max_1000.readline().rstrip("\n"))/divisor
    hash_max_data[1] += float(hash_cpu_max_1000.readline().rstrip("\n"))/numberOfCores

    hash_cpu_max_10000 = open("hash_cpu_10000_" + str(i) + ".txt", "r")
    hash_cpu_data[2] += float(hash_cpu_max_10000.readline().rstrip("\n"))/divisor
    hash_max_data[2] += float(hash_cpu_max_10000.readline().rstrip("\n"))/numberOfCores

    hash_cpu_max_30000 = open("hash_cpu_30000_" + str(i) + ".txt", "r")
    hash_cpu_data[3] += float(hash_cpu_max_30000.readline().rstrip("\n"))/divisor
    hash_max_data[3] += float(hash_cpu_max_30000.readline().rstrip("\n"))/numberOfCores

    hash_cpu_max_60000 = open("hash_cpu_60000_" + str(i) + ".txt", "r")
    hash_cpu_data[4] += float(hash_cpu_max_60000.readline().rstrip("\n"))/divisor
    hash_max_data[4] += float(hash_cpu_max_60000.readline().rstrip("\n"))/numberOfCores

    hash_cpu_max_100000 = open("hash_cpu_100000_" + str(i) + ".txt", "r")
    hash_cpu_data[5] += float(hash_cpu_max_100000.readline().rstrip("\n"))/divisor
    hash_max_data[5] += float(hash_cpu_max_100000.readline().rstrip("\n"))/numberOfCores

    hash_mem_100 = open("hash_mem_100_" + str(i) + ".txt", "r")
    hash_mem_data[0] += float(hash_mem_100.readline().rstrip("\n"))

    hash_mem_1000 = open("hash_mem_1000_" + str(i) + ".txt", "r")
    hash_mem_data[1] += float(hash_mem_1000.readline().rstrip("\n"))

    hash_mem_10000 = open("hash_mem_10000_" + str(i) + ".txt", "r")
    hash_mem_data[2] += float(hash_mem_10000.readline().rstrip("\n"))

    hash_mem_30000 = open("hash_mem_30000_" + str(i) + ".txt", "r")
    hash_mem_data[3] += float(hash_mem_30000.readline().rstrip("\n"))

    hash_mem_60000 = open("hash_mem_60000_" + str(i) + ".txt", "r")
    hash_mem_data[4] += float(hash_mem_60000.readline().rstrip("\n"))

    hash_mem_100000 = open("hash_mem_100000_" + str(i) + ".txt", "r")
    hash_mem_data[5] += float(hash_mem_100000.readline().rstrip("\n"))

    ## SELECTION ##
    selection_cpu_max_100 = open("selection_cpu_100_" + str(i) + ".txt", "r")
    selection_cpu_data[0] += float(selection_cpu_max_100.readline().rstrip("\n"))/divisor
    selection_max_data[0] += float(selection_cpu_max_100.readline().rstrip("\n"))/numberOfCores

    selection_cpu_max_1000 = open("selection_cpu_1000_" + str(i) + ".txt", "r")
    selection_cpu_data[1] += float(selection_cpu_max_1000.readline().rstrip("\n"))/divisor
    selection_max_data[1] += float(selection_cpu_max_1000.readline().rstrip("\n"))/numberOfCores

    selection_cpu_max_10000 = open("selection_cpu_10000_" + str(i) + ".txt", "r")
    selection_cpu_data[2] += float(selection_cpu_max_10000.readline().rstrip("\n"))/divisor
    selection_max_data[2] += float(selection_cpu_max_10000.readline().rstrip("\n"))/numberOfCores

    selection_cpu_max_30000 = open("selection_cpu_30000_" + str(i) + ".txt", "r")
    selection_cpu_data[3] += float(selection_cpu_max_30000.readline().rstrip("\n"))/divisor
    selection_max_data[3] += float(selection_cpu_max_30000.readline().rstrip("\n"))/numberOfCores

    selection_cpu_max_60000 = open("selection_cpu_60000_" + str(i) + ".txt", "r")
    selection_cpu_data[4] += float(selection_cpu_max_60000.readline().rstrip("\n"))/divisor
    selection_max_data[4] += float(selection_cpu_max_60000.readline().rstrip("\n"))/numberOfCores

    selection_cpu_max_100000 = open("selection_cpu_100000_" + str(i) + ".txt", "r")
    selection_cpu_data[5] += float(selection_cpu_max_100000.readline().rstrip("\n"))/divisor
    selection_max_data[5] += float(selection_cpu_max_100000.readline().rstrip("\n"))/numberOfCores

    selection_mem_100 = open("selection_mem_100_" + str(i) + ".txt", "r")
    selection_mem_data[0] += float(selection_mem_100.readline().rstrip("\n"))

    selection_mem_1000 = open("selection_mem_1000_" + str(i) + ".txt", "r")
    selection_mem_data[1] += float(selection_mem_1000.readline().rstrip("\n"))

    selection_mem_10000 = open("selection_mem_10000_" + str(i) + ".txt", "r")
    selection_mem_data[2] += float(selection_mem_10000.readline().rstrip("\n"))

    selection_mem_30000 = open("selection_mem_30000_" + str(i) + ".txt", "r")
    selection_mem_data[3] += float(selection_mem_30000.readline().rstrip("\n"))

    selection_mem_60000 = open("selection_mem_60000_" + str(i) + ".txt", "r")
    selection_mem_data[4] += float(selection_mem_60000.readline().rstrip("\n"))

    selection_mem_100000 = open("selection_mem_100000_" + str(i) + ".txt", "r")
    selection_mem_data[5] += float(selection_mem_100000.readline().rstrip("\n"))

    ## PROJECTION ##
    projection_cpu_max_100 = open("projection_cpu_100_" + str(i) + ".txt", "r")
    projection_cpu_data[0] += float(projection_cpu_max_100.readline().rstrip("\n"))/divisor
    projection_max_data[0] += float(projection_cpu_max_100.readline().rstrip("\n"))/numberOfCores

    projection_cpu_max_1000 = open("projection_cpu_1000_" + str(i) + ".txt", "r")
    projection_cpu_data[1] += float(projection_cpu_max_1000.readline().rstrip("\n"))/divisor
    projection_max_data[1] += float(projection_cpu_max_1000.readline().rstrip("\n"))/numberOfCores

    projection_cpu_max_10000 = open("projection_cpu_10000_" + str(i) + ".txt", "r")
    projection_cpu_data[2] += float(projection_cpu_max_10000.readline().rstrip("\n"))/divisor
    projection_max_data[2] += float(projection_cpu_max_10000.readline().rstrip("\n"))/numberOfCores

    projection_cpu_max_30000 = open("projection_cpu_30000_" + str(i) + ".txt", "r")
    projection_cpu_data[3] += float(projection_cpu_max_30000.readline().rstrip("\n"))/divisor
    projection_max_data[3] += float(projection_cpu_max_30000.readline().rstrip("\n"))/numberOfCores

    projection_cpu_max_60000 = open("projection_cpu_60000_" + str(i) + ".txt", "r")
    projection_cpu_data[4] += float(projection_cpu_max_60000.readline().rstrip("\n"))/divisor
    projection_max_data[4] += float(projection_cpu_max_60000.readline().rstrip("\n"))/numberOfCores

    projection_cpu_max_100000 = open("projection_cpu_100000_" + str(i) + ".txt", "r")
    projection_cpu_data[5] += float(projection_cpu_max_100000.readline().rstrip("\n"))/divisor
    projection_max_data[5] += float(projection_cpu_max_100000.readline().rstrip("\n"))/numberOfCores

    projection_mem_100 = open("projection_mem_100_" + str(i) + ".txt", "r")
    projection_mem_data[0] += float(projection_mem_100.readline().rstrip("\n"))

    projection_mem_1000 = open("projection_mem_1000_" + str(i) + ".txt", "r")
    projection_mem_data[1] += float(projection_mem_1000.readline().rstrip("\n"))

    projection_mem_10000 = open("projection_mem_10000_" + str(i) + ".txt", "r")
    projection_mem_data[2] += float(projection_mem_10000.readline().rstrip("\n"))

    projection_mem_30000 = open("projection_mem_30000_" + str(i) + ".txt", "r")
    projection_mem_data[3] += float(projection_mem_30000.readline().rstrip("\n"))

    projection_mem_60000 = open("projection_mem_60000_" + str(i) + ".txt", "r")
    projection_mem_data[4] += float(projection_mem_60000.readline().rstrip("\n"))

    projection_mem_100000 = open("projection_mem_100000_" + str(i) + ".txt", "r")
    projection_mem_data[5] += float(projection_mem_100000.readline().rstrip("\n"))

    ## JOIN ##

    join_cpu_max_100 = open("join_cpu_100_" + str(i) + ".txt", "r")
    join_cpu_data[0] += float(join_cpu_max_100.readline().rstrip("\n"))/divisor
    join_max_data[0] += float(join_cpu_max_100.readline().rstrip("\n"))/numberOfCores

    join_cpu_max_1000 = open("join_cpu_1000_" + str(i) + ".txt", "r")
    join_cpu_data[1] += float(join_cpu_max_1000.readline().rstrip("\n"))/divisor
    join_max_data[1] += float(join_cpu_max_1000.readline().rstrip("\n"))/numberOfCores

    join_cpu_max_10000 = open("join_cpu_10000_" + str(i) + ".txt", "r")
    join_cpu_data[2] += float(join_cpu_max_10000.readline().rstrip("\n"))/divisor
    join_max_data[2] += float(join_cpu_max_10000.readline().rstrip("\n"))/numberOfCores

    join_cpu_max_30000 = open("join_cpu_30000_" + str(i) + ".txt", "r")
    join_cpu_data[3] += float(join_cpu_max_30000.readline().rstrip("\n"))/divisor
    join_max_data[3] += float(join_cpu_max_30000.readline().rstrip("\n"))/numberOfCores

    join_cpu_max_60000 = open("join_cpu_60000_" + str(i) + ".txt", "r")
    join_cpu_data[4] += float(join_cpu_max_60000.readline().rstrip("\n"))/divisor
    join_max_data[4] += float(join_cpu_max_60000.readline().rstrip("\n"))/numberOfCores

    join_cpu_max_100000 = open("join_cpu_100000_" + str(i) + ".txt", "r")
    join_cpu_data[5] += float(join_cpu_max_100000.readline().rstrip("\n"))/divisor
    join_max_data[5] += float(join_cpu_max_100000.readline().rstrip("\n"))/numberOfCores

    join_mem_100 = open("join_mem_100_" + str(i) + ".txt", "r")
    join_mem_data[0] += float(join_mem_100.readline().rstrip("\n"))

    join_mem_1000 = open("join_mem_1000_" + str(i) + ".txt", "r")
    join_mem_data[1] += float(join_mem_1000.readline().rstrip("\n"))

    join_mem_10000 = open("join_mem_10000_" + str(i) + ".txt", "r")
    join_mem_data[2] += float(join_mem_10000.readline().rstrip("\n"))

    join_mem_30000 = open("join_mem_30000_" + str(i) + ".txt", "r")
    join_mem_data[3] += float(join_mem_30000.readline().rstrip("\n"))

    join_mem_60000 = open("join_mem_60000_" + str(i) + ".txt", "r")
    join_mem_data[4] += float(join_mem_60000.readline().rstrip("\n"))

    join_mem_100000 = open("join_mem_100000_" + str(i) + ".txt", "r")
    join_mem_data[5] += float(join_mem_100000.readline().rstrip("\n"))

    i += 1

j = 0

while j < num_diff_sizes:
    sort_cpu_data[j] /= trial_amount
    # print(sort_cpu_data[j])
    sort_mem_data[j] /= trial_amount
    # print(sort_mem_data[j])
    sort_max_data[j] /= trial_amount
    # print(sort_max_data[j])

    hash_cpu_data[j] /= trial_amount
    hash_mem_data[j] /= trial_amount
    hash_max_data[j] /= trial_amount

    selection_cpu_data[j] /= trial_amount
    selection_mem_data[j] /= trial_amount
    selection_max_data[j] /= trial_amount

    projection_cpu_data[j] /= trial_amount
    projection_mem_data[j] /= trial_amount
    projection_max_data[j] /= trial_amount

    join_cpu_data[j] /= trial_amount
    join_mem_data[j] /= trial_amount
    join_max_data[j] /= trial_amount

    j += 1

# print("sort")
# for num in sort_cpu_data:
#     num /= trial_amount
#     print(num)
# for num in sort_mem_data:
#     num /= trial_amount
#     print(num)
# for num in sort_max_data:
#     num /= trial_amount
#     print(num)

# for num in hash_cpu_data:
#     num /= trial_amount
# for num in hash_mem_data:
#     num /= trial_amount
# for num in hash_max_data:
#     num /= trial_amount

# for num in selection_cpu_data:
#     num /= trial_amount
# for num in selection_mem_data:
#     num /= trial_amount
# for num in selection_max_data:
#     num /= trial_amount

# for num in projection_cpu_data:
#     num /= trial_amount
# for num in projection_mem_data:
#     num /= trial_amount
# for num in projection_max_data:
#     num /= trial_amount

# x_vals = [.015, .147, 1.5, 4.4, 8.8, 14.7]
x_vals = [100, 1000, 10_000, 30_000, 60_000, 100_000]

sort_cpu_slope, sort_cpu_intercept, sort_cpu_r_value, sort_cpu_p_value, sort_cpu_std_err = stats.linregress(x_vals, sort_cpu_data)
sort_mem_slope, sort_mem_intercept, sort_mem_r_value, sort_mem_p_value, sort_mem_std_err = stats.linregress(x_vals, sort_mem_data)
sort_max_slope, sort_max_intercept, sort_max_r_value, sort_max_p_value, sort_max_std_err = stats.linregress(x_vals, sort_max_data)

hash_cpu_slope, hash_cpu_intercept, hash_cpu_r_value, hash_cpu_p_value, hash_cpu_std_err = stats.linregress(x_vals, hash_cpu_data)
hash_mem_slope, hash_mem_intercept, hash_mem_r_value, hash_mem_p_value, hash_mem_std_err = stats.linregress(x_vals, hash_mem_data)
hash_max_slope, hash_max_intercept, hash_max_r_value, hash_max_p_value, hash_max_std_err = stats.linregress(x_vals, hash_max_data)

selection_cpu_slope, selection_cpu_intercept, selection_cpu_r_value, selection_cpu_p_value, selection_cpu_std_err = stats.linregress(x_vals, selection_cpu_data)
selection_mem_slope, selection_mem_intercept, selection_mem_r_value, selection_mem_p_value, selection_mem_std_err = stats.linregress(x_vals, selection_mem_data)
selection_max_slope, selection_max_intercept, selection_max_r_value, selection_max_p_value, selection_max_std_err = stats.linregress(x_vals, selection_max_data)

projection_cpu_slope, projection_cpu_intercept, projection_cpu_r_value, projection_cpu_p_value, projection_cpu_std_err = stats.linregress(x_vals, projection_cpu_data)
projection_mem_slope, projection_mem_intercept, projection_mem_r_value, projection_mem_p_value, projection_mem_std_err = stats.linregress(x_vals, projection_mem_data)
projection_max_slope, projection_max_intercept, projection_max_r_value, projection_max_p_value, projection_max_std_err = stats.linregress(x_vals, projection_max_data)

join_cpu_slope, join_cpu_intercept, join_cpu_r_value, join_cpu_p_value, join_cpu_std_err = stats.linregress(x_vals, join_cpu_data)
join_mem_slope, join_mem_intercept, join_mem_r_value, join_mem_p_value, join_mem_std_err = stats.linregress(x_vals, join_mem_data)
join_max_slope, join_max_intercept, join_max_r_value, join_max_p_value, join_max_std_err = stats.linregress(x_vals, join_max_data)

model_data = {'sort_cpu_m': float(sort_cpu_slope), 'sort_cpu_b': float(sort_cpu_intercept), 'sort_mem_m': float(sort_mem_slope), 'sort_mem_b': float(sort_mem_intercept), 'sort_max_m': float(sort_max_slope), 'sort_max_b': float(sort_max_intercept), 'hash_cpu_m': float(hash_cpu_slope), 'hash_cpu_b': float(hash_cpu_intercept), 'hash_mem_m': float(hash_mem_slope), 'hash_mem_b': float(hash_mem_intercept), 'hash_max_m': float(hash_max_slope), 'hash_max_b': float(hash_max_intercept), 'selection_cpu_m': float(selection_cpu_slope), 'selection_cpu_b': float(selection_cpu_intercept), 'selection_mem_m': float(selection_mem_slope), 'selection_mem_b': float(selection_mem_intercept), 'selection_max_m': float(selection_max_slope), 'selection_max_b': float(selection_max_intercept), 'projection_cpu_m': float(projection_cpu_slope), 'projection_cpu_b': float(projection_cpu_intercept), 'projection_mem_m': float(projection_mem_slope), 'projection_mem_b': float(projection_mem_intercept), 'projection_max_m': float(projection_max_slope), 'projection_max_b': float(projection_max_intercept), 'join_cpu_m': float(join_cpu_slope), 'join_cpu_b': float(join_cpu_intercept), 'join_mem_m': float(join_mem_slope), 'join_mem_b': float(join_mem_intercept), 'join_max_m': float(join_max_slope), 'join_max_b': float(join_max_intercept)}

with open('model_data.yaml', 'w') as f:
    data = yaml.dump(model_data, f)
