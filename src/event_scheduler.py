import heapq
from typing import List, Tuple

def can_attend_all(events: List[Tuple[int, int]]) -> bool:
    """
    Determines if a person can attend all events without overlaps.
    Adjacent events (end time == start time) are not considered overlaps.
    """
    if not events:
        return True
        
    sorted_events = sorted(events, key=lambda x: x[0])
    
    for i in range(1, len(sorted_events)):
        if sorted_events[i][0] < sorted_events[i-1][1]:
            return False
            
    return True

def min_rooms_required(events: List[Tuple[int, int]]) -> int:
    """
    Calculates the minimum number of meeting rooms required to schedule all events.
    """
    if not events:
        return 0
        
    sorted_events = sorted(events, key=lambda x: x[0])
    
    free_rooms: List[int] = []
    
    heapq.heappush(free_rooms, sorted_events[0][1])
    
    for i in range(1, len(sorted_events)):
        if free_rooms[0] <= sorted_events[i][0]:
            heapq.heappop(free_rooms) 
            
        heapq.heappush(free_rooms, sorted_events[i][1])
        
    return len(free_rooms)