from collections import deque


def lengthOfLongestSubstring(s: str) -> int:
    now_queue = deque()
    char_set = set()
    result = 0

    for char in s:
        if char in char_set:
            while now_queue[0] != char:
                removed = now_queue.popleft()
                char_set.remove(removed)
            now_queue.popleft()
            now_queue.append(char)
        else:
            now_queue.append(char)
            char_set.add(char)

        result = max(result, len(char_set))
    return result

lengthOfLongestSubstring("abcabcbb")