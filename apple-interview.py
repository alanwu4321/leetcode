inp = {
    'k1': {
        'k2':{
            'k3':{
                'k4': 3,
                'k5': {
                    'k6':4
                }
            }
        },
        'k4':{
            'k5':{
            }
        },
    },
}

def explore2(caller,hmap_val,cur,res):
    if isinstance(hmap_val, int):
        res.append(cur[1:] + '-' +  caller + '=>' + str(hmap_val))
        return
    for key, val in hmap_val.items():
        explore2(key, val, cur + '-' + key, res)

def explore(hmap,cur,res):
    for key, val in hmap.items():
        if isinstance(val, int):
            res.append(cur[1:] + '-' +  key + '=>' + str(val))
        else:
            explore(val,cur + '-' + key,res)

def pathToInt(inp):
    res = list()
    explore(inp,'',res)
    explore2('',inp,'',res)
    return res

print(pathToInt(inp))



# 1. talk about my Kubernetes experience
# 2. he started asking a series of tech questions
# 3. the difference is git merge and rebase
# 4. difference between class and modules in ruby
# 4. what is a container
# 5. what is a replicaset
# 6. what happens if a pod goes down
# 7. how to check the uptime of a machine

# coding question is a backtrack DFS