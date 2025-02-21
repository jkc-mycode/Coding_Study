from datetime import datetime, timedelta

def to_datetime(time_str):
    return datetime.strptime(time_str, "%H:%M")

def add_time(time_str):
    return to_datetime(time_str) + timedelta(minutes=10)

def solution(book_time):
    start_times = sorted([to_datetime(start) for start, end in book_time])
    end_times = sorted([add_time(end) for start, end in book_time])
    
    result = 0
    end_idx = 0
    
    for start in start_times:
        if start >= end_times[end_idx]:
            end_idx += 1
        else:
            result += 1
    
    return result



# def plustime(time_str):
#     time = datetime.strptime(time_str, "%H:%M") + timedelta(minutes=10)
#     return time.strftime("%H:%M")

# def solution(book_time):
#     book_time.sort(key=lambda x: x[0])
#     end_times = []
    
#     for start, end in book_time:
#         available = False        
#         for i in range(len(end_times)):
#             if start >= end_times[i]:
#                 end_times[i] = plustime(end)
#                 available = True
#                 break
#         if not available:
#             end_times.append(plustime(end))
        
#     return len(end_times)
