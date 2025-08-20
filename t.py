

def find_missing_ranges(frames):

    """
    Task requirements 

     - detect missing video frames from a list of received frame numbers
     - frames: unordered list of frame numbers
     - res = dictionary containing gaps and missing frame information

     Rules & Constraints
● Do not use sort() or similar built-in sorting functions.
● Do not use third-party libraries like NumPy or Pandas.
● Try to make the solution as efficient as possible.
● Assume there are no duplicate frame numbers in the input list
Evaluation Criteria
● Correctness of the logic.
● Handling of edge cases.
● Efficiency and code clarity.
● Respecting the constraints (especially not using .sort())
    """
    
    
    if not frames:
        return {"gaps": [], "longest_gap": [], "missing_count": 0}
    
    max_frame = frames[0]
    for frame in frames:

        if frame < 0 :
            print("frame input",frame," should be valid and positve numbers")
            continue
        if frame > max_frame:
            max_frame = frame
           # print("max frame is", max_frame)

     # converting data into a set is useful for performance.
     # in one of my previous projects, we were encoding and transferring chunks over HTTP.
     # when we needed to encode specific bytes based on API-provided keys,
     # lookups in a set were faster than in a list, since sets are implemented as hash-based structures.
     
    frame_set = set(frames)

    gaps = []
    gap_start = None
    
    max_gap_size = 0
    total_missing = 0
    longest_gap = []


    for i in range(1, max_frame + 1):

        # check if number is inside frame set cause if it not exist 
        # it should be the start of gap and also  it considered one of the missed frames
        if i not in frame_set:
            if gap_start is None:
                gap_start = i
        
        # else the number inside frames
        else:
            if gap_start is not None:
                gap_end = i - 1
                gap_size = gap_end - gap_start+ 1
                total_missing+=gap_size
                gap = [gap_start,gap_end]
                if gap_size > max_gap_size:
                    max_gap_size = gap_size
                    longest_gap = gap
                gaps.append(gap)
                gap_start = None

    
    
    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": total_missing
    }

def start():
    frames = [1, 2, 3, 5, 6, 10, 11, 16]
    result = find_missing_ranges(frames)

    print("-------------------------")
    print("Input:", frames)
    print("Result:", result)
    print("------------------------\r\n")
    expected = {
        "gaps": [[4, 4], [7, 9], [12, 15]],
        "longest_gap": [12, 15],
        "missing_count": 8
    }
    
    print("what results should be :", expected)
    print("result:", result)
    print("Passed ?", result == expected)


start()

