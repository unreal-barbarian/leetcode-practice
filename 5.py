class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        rs = s[::-1]
        is_same_before = False
        rng1 = [0,1]
        rng2 = [0,1]
        answer = s[0]
        longest_p = 0
        l = len(s)
        def overlap_range(x):
            if x < 0:
                return zip(range(l + x), range(-1 * x, l))
            else:
                return zip(range(x, l), range(l - x))

        def common(rng1, rng2):
            s1, s2 = rng1
            r1, r2 = rng2
            rs1, rs2 = l - r2, l - r1
            return [max(s1, rs1), min(s2, rs2)]

        for start in range(-1 * l + 1, l):
            for i, j in overlap_range(start):
                if s[i] == rs[j]:
                    if is_same_before:
                        rng1[1] += 1
                        rng2[1] += 1
                    else:
                        is_same_before = True
                        rng1 = [i, i + 1]
                        rng2 = [j, j + 1]
                else:
                    l1, l2 = common(rng1, rng2)
                    if l2-l1 > longest_p:
                        longest_p = l2 - l1
                        answer = s[l1:l2]
                    is_same_before = False
            is_same_before = False
            l1, l2 = common(rng1, rng2)
            if l2 - l1 > longest_p:
                longest_p = l2 - l1
                answer = s[l1:l2]
        return answer

a = Solution()
print(a.longestPalindrome("mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd" ))