class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        each_line = []
        for line in source:
            i = 0
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break  
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 1  
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 1  
                elif not in_block:
                    each_line.append(line[i])
                i += 1
            
            if each_line and not in_block:
                result.append("".join(each_line))
                each_line = []  

        return result
