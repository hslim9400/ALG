def gcd(a, b):
    small = min(a, b)
    large = max(a, b)
    while True:
        large, small = small, large%small
        if small == 0:
            break
    return large


def solution(w,h):
    trash = 1 + (w - 1) + (h - 1) - (gcd(w, h) - 1)
    answer = w*h - trash
    return answer

print(solution(8, 12))

