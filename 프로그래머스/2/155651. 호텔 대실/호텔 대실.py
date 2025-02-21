from datetime import datetime, timedelta

def plustime(time_str):
    return datetime.strptime(time_str, "%H:%M") + timedelta(minutes=10)

def to_datetime(time_str):
    return datetime.strptime(time_str, "%H:%M")

def solution(book_time):
    # 예약 시간을 시작 시간으로 정렬
    book_time.sort(key=lambda x: x[0])
    
    # 종료 시간을 담는 리스트
    end_times = []

    for start, end in book_time:
        start_time = to_datetime(start)
        end_time_with_cleanup = plustime(end)
        
        # 방이 사용 가능 여부 확인
        available = False        
        for i in range(len(end_times)):
            if start_time >= end_times[i]:
                end_times[i] = end_time_with_cleanup
                available = True
                break
        
        if not available:
            end_times.append(end_time_with_cleanup)
        
    return len(end_times)