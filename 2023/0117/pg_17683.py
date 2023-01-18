import heapq
def solution(m, musicinfos):
    answer = ''
    playlist = []
    count = 0

    for music in musicinfos:
        count += 1
        start, end, title, notes = music.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, start.split(':'))
        play_time =60*(end_h-start_h) + (end_m-start_m)
        if play_time > len(notes):
            played = (play_time//len(notes))*notes + notes[:(play_time-(play_time//len(notes))*notes)]
        else:
            played = notes[:play_time]
        new_info = [-play_time, count, title, played]
        heapq.heappush(playlist, new_info)

    print(playlist)

    return answer

solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])