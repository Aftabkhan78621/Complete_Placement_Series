# ============================================================
# INTERVAL PATTERN
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. MERGE INTERVALS
# ============================================================

"""
THEORY (Interview Explanation)

Interval problems me har interval ka format [start, end] hota hai.
Merge Intervals me pehle intervals ko starting time ke according sort
kiya jata hai. Fir current interval ko previous interval se compare
karte hain. Agar current interval previous interval ke end se pehle
start hota hai to dono overlap karte hain aur merge ho jate hain.
Agar overlap nahi hota to current interval ko result me add kar dete
hain. Ye scheduling, calendar aur booking systems me bahut use hota hai.
"""

def merge_intervals(intervals):

    intervals.sort()

    result = [intervals[0]]

    for start, end in intervals[1:]:

        if start <= result[-1][1]:

            result[-1][1] = max(result[-1][1], end)

        else:

            result.append([start, end])

    return result


intervals = [[1,3],[2,6],[8,10],[15,18]]

print("Merge Intervals :", merge_intervals(intervals))


# Time  : O(n log n)
# Space : O(n)



# ============================================================
# 2. INSERT INTERVAL
# ============================================================

"""
THEORY (Interview Explanation)

Insert Interval me ek naya interval sorted interval list me insert
karna hota hai. Agar overlap nahi hai to interval direct add karte hain.
Agar overlap hai to merge karte hue naya interval update karte hain.
End me merged interval aur remaining intervals result me add kar dete
hain. Ye calendar booking aur meeting scheduling systems me use hota hai.
"""

def insert_interval(intervals, new_interval):

    result = []

    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:

        result.append(intervals[i])

        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:

        new_interval[0] = min(new_interval[0], intervals[i][0])

        new_interval[1] = max(new_interval[1], intervals[i][1])

        i += 1

    result.append(new_interval)

    while i < n:

        result.append(intervals[i])

        i += 1

    return result


intervals = [[1,3],[6,9]]

print("Insert Interval :", insert_interval(intervals,[2,5]))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. MEETING ROOMS
# ============================================================

"""
THEORY (Interview Explanation)

Meeting Room problem me check karna hota hai ki ek person saari meetings
attend kar sakta hai ya nahi. Sabse pehle meetings ko start time ke
according sort karte hain. Fir har meeting ko previous meeting ke end
time se compare karte hain. Agar current meeting previous meeting ke
end se pehle start ho rahi hai to overlap hai aur answer False hoga.
Agar koi overlap nahi mila to saari meetings attend ki ja sakti hain.
"""

def can_attend_meetings(intervals):

    intervals.sort()

    for i in range(1, len(intervals)):

        if intervals[i][0] < intervals[i-1][1]:

            return False

    return True


meetings1 = [[0,30],[5,10],[15,20]]

meetings2 = [[7,10],[12,15]]

print("Meeting Rooms 1 :", can_attend_meetings(meetings1))

print("Meeting Rooms 2 :", can_attend_meetings(meetings2))


# ============================================================
# Expected Output
# ============================================================

# Merge Intervals :
# [[1,6],[8,10],[15,18]]

# Insert Interval :
# [[1,5],[6,9]]

# Meeting Rooms 1 :
# False

# Meeting Rooms 2 :
# True


# ============================================================
# Complexity
# ============================================================

# Merge Intervals
# Time  : O(n log n)
# Space : O(n)

# Insert Interval
# Time  : O(n)
# Space : O(n)

# Meeting Rooms
# Time  : O(n log n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Sort intervals first.
# ✔ Compare current interval with previous interval.
# ✔ Merge if overlapping.
# ✔ Interval Pattern = Sorting + Greedy.

# ============================================================
# INTERVAL PATTERN COMPLETE ✅
# ============================================================