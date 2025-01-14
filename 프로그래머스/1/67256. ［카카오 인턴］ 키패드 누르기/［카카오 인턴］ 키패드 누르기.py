def dist_check(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def solution(numbers, hand):
    phone = {
        "*": (0, 0), 0: (0, 1), "#": (0, 2),
        1: (3, 0), 2: (3, 1), 3: (3, 2),
        4: (2, 0), 5: (2, 1), 6: (2, 2),
        7: (1, 0), 8: (1, 1), 9: (1, 2),
    }
    
    cur_left = phone["*"]
    cur_right = phone["#"]
    
    left = [1, 4, 7]
    right = [3, 6, 9]
    
    result = ""
    
    for n in numbers:
        if n in left:
            result += "L"
            cur_left = phone[n]
        elif n in right:
            result += "R"
            cur_right = phone[n]
        elif dist_check(phone[n], cur_left) < dist_check(phone[n], cur_right):
            result += "L"
            cur_left = phone[n]
        elif dist_check(phone[n], cur_left) > dist_check(phone[n], cur_right):
            result += "R"
            cur_right = phone[n]
        else:
            if hand == "left":
                result += "L"
                cur_left = phone[n]
            else:
                result += "R"
                cur_right = phone[n]
    
    return result