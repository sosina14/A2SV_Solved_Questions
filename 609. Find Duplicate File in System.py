class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in paths:
            i = i.split(" ")
            folder = i[0]
            for j in i[1:]:
                j = j.split(".txt")
                name = j[0]
                con = j[1]
                dic[con].append((folder,name)) 
        result = []
        for k,v in dic.items():
            if len(v) > 1:
                x = []
                for path , name in v:
                    x.append(path+'/'+name+'.txt')
                result.append(x)
        return result
