L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
     {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

s = set()
for dic in L:
    for key, value in dic.items():
        s.add(value)

print(s)
