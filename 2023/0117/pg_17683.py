def solution(m, musicinfos):
    answer = ''
    note_set = {'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'}
    m_list = []
    for i in range(len(m)):
        if m[i:i+2] in note_set:
            m_list.append(m[i:i+2])
        elif m[i] in note_set:
            m_list.append(m[i])

    playlist = []
    count = 0

    for music in musicinfos:
        count += 1
        start, end, title, notes = music.split(',')
        note_list = []
        for i in range(len(notes)):
            if notes[i:i + 2] in note_set:
                note_list.append(notes[i:i + 2])
            elif notes[i] in note_set:
                note_list.append(notes[i])
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        play_time = 60*(end_h-start_h) + (end_m-start_m)
        if play_time > len(note_list):
            played = (play_time//len(note_list))*note_list + \
                     note_list[:(play_time-(play_time//len(note_list))*len(note_list))]
        else:
            played = note_list[:play_time]
        new_info = [-play_time, count, title, played]
        playlist.append(new_info)
    playlist.sort()

    for music in playlist:
        notes = music[3]
        flag = False
        for i in range(len(notes)):
            if notes[i:i+len(m_list)] == m_list:
                answer = music[2]
                flag = True
                break
        if flag:
            break
    else:
        answer = '(None)'

    return answer

print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))