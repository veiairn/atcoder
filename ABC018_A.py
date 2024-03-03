d = {}
for i in range(3):
    d[i+1]=int(input())

sorted_dict = sorted(d.items(), key=lambda kv: kv[1],reverse=True)

for key in d.keys():
    for index, (sorted_key, sorted_value) in enumerate(sorted_dict):
        if key == sorted_key:
            print(index+1)