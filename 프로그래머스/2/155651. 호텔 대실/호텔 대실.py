from datetime import datetime, timedelta

def to_datetime(time_str):
    return datetime.strptime(time_str, "%H:%M")

def plustime(time_str):
    return to_datetime(time_str) + timedelta(minutes=10)

def solution(book_time):
    book_time.sort(key=lambda x: x[0])
    end_times = []

    for start, end in book_time:
        start_time = to_datetime(start)
        end_time_with_cleanup = plustime(end)
        
        available = False        
        for i in range(len(end_times)):
            if start_time >= end_times[i]:
                end_times[i] = end_time_with_cleanup
                available = True
                break
        
        if not available:
            end_times.append(end_time_with_cleanup)
        
    return len(end_times)



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
