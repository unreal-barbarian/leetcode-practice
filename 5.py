class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        n = len(s)
        answer = s[0]
        longest_n = 1
        for i in range(n):
            if i == 1:
                1+1
            t_l = 1
            l = r = i
            while True:
                l -= 1
                r += 1
                if l < 0 or r >= n:
                    break
                if s[l] == s[r]:
                    t_l += 2
                    if t_l > longest_n:
                        answer = s[l: r + 1]
                        longest_n = t_l
                else:
                    break

        for i in range(1, n):
            t_l = 0
            l = i
            r = i - 1
            while True:
                l -= 1
                r += 1
                if l < 0 or r >= n:
                    break
                if s[l] == s[r]:
                    t_l += 2
                    if t_l > longest_n:
                        answer = s[l: r + 1]
                        longest_n = t_l
                else:
                    break
        return answer


a = Solution()
print(a.longestPalindrome('ccc'))
print(a.longestPalindrome('ababd'))
print(a.longestPalindrome('abccba'))
print(a.longestPalindrome("mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd"))
