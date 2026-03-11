class Solution:
    def longestCommonPrefix(self, strs):
        lenstrs = len(strs)
        if lenstrs == 0:
            return ""
        if lenstrs == 1:
            return strs[0]
        if "" in strs:
            return ""

        i = 0
        j = 0
        holi = 1
        output = ""

        while True:

            if j >= len(strs[i]) or j >= len(strs[i + 1]):
                break

            if strs[i][j] == strs[i + 1][j]:
                i += 1
                holi += 1

            if holi == lenstrs:
                output += strs[i][j]
                j += 1
                i = 0
                holi = 1
                continue

            if j >= len(strs[i]) or j >= len(strs[i + 1]):
                break

            if strs[i][j] != strs[i + 1][j]:
                break

        return output
