def run_length_encoding(word):
    encoding = ""
    count = 1
    tmp_char = word[0]
    for idx in range(len(word) - 1):
        if word[idx] == word[idx + 1]:
            count += 1
        else:
            encoding += tmp_char + str(count)
            count = 1
            tmp_char = word[idx+1]

    encoding += tmp_char + str(count)
    return encoding

print(run_length_encoding("aaabbbbcaa"))
print(run_length_encoding('aaabccaddde'))
print(run_length_encoding('milkboy'))