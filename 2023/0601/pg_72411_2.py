def solution(orders, course):
    answer = []
    menu_dict = {}
    last = 0
    order_bins = []
    for order in orders:
        order_bin = 0
        for menu in order:
            if menu not in menu_dict.keys():
                menu_dict[menu] = last
                menu_dict[last] = menu
                last += 1
            order_bin += 1 << menu_dict[menu]
        order_bins.append(order_bin)
    
    course_dict = {}
    for volume in course:
        course_dict[volume] = {'biggest': 0, 'menus': []}

    course = set(course)
    for course_menu in range(1<<(len(menu_dict)//2)):

        counts = 0
        menu_string = []
        for menu in range(len(menu_dict)//2):
            if course_menu & (1<<menu):
                counts += 1
                menu_string.append(menu_dict[menu])
        if counts not in course:
            continue
        menu_string = ''.join(sorted(menu_string))
        serve = 0
        for order in order_bins:
            if order | course_menu == order:
                serve += 1
        
        if serve > 1:
            if serve > course_dict[counts]['biggest']:
                course_dict[counts]['biggest'] = serve
                course_dict[counts]['menus'] = [menu_string]
            elif serve == course_dict[counts]['biggest']:
                course_dict[counts]['menus'].append(menu_string)
        
    for volume in course:
        answer.extend(course_dict[volume]['menus'])
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))