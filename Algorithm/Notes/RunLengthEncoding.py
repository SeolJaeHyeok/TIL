def run_length_encoding(str_list):
    encoding = ""
    seq = 1
    tmp_char = str_list[0]
    for idx in range(len(str_list)-1):
        if str_list[idx] == str_list[idx+1]:
            seq += 1
        else:
            encoding += tmp_char + str(seq)
            seq = 1
            tmp_char = str_list[idx+1]

    encoding += tmp_char + str(seq)
    return encoding

print(run_length_encoding("aaabbbbcaa"))
print(run_length_encoding('aaabccaddde'))
print(run_length_encoding('milkboy'))