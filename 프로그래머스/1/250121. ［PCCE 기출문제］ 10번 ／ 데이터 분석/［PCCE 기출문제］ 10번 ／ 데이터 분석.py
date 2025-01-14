def solution(data, ext, val_ext, sort_by):
    ext_index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    val_data = [d for d in data if d[ext_index[ext]] <= val_ext]
    
    return sorted(val_data, key=lambda x: x[ext_index[sort_by]])
    