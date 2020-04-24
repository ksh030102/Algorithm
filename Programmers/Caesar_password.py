# 12926 시저암호

def solution(s, n):
    s = list(s)
    la = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

    sa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

    for i in range(len(s)):
        if s[i] in la:
            for idx, j in enumerate(la):
                if s[i] == j:
                    if idx + n >= len(la):
                        s[i] = la[idx + n - 26]
                        break
                    else:
                        s[i] = la[idx + n]
                        break
        elif s[i] in sa:
            for idx, j in enumerate(sa):
                if s[i] == j:
                    if idx + n >= len(sa):
                        s[i] = sa[idx + n - 26]
                        break
                    else:
                        s[i] = sa[idx + n]
                        break
        else:
            continue
        answer = ''.join(s)
    return answer