# 🐍 Python DSA Journey

My personal journey through Data Structures & Algorithms — one problem at a time, all solved in Python.

This repo is where I track my practice, revisit concepts, and build a solid foundation in problem-solving. Feel free to explore, fork, or use it as a reference for your own DSA prep.

---

## 📌 Why this repo?

- To build consistency by solving problems regularly
- To keep all my solutions organized and searchable in one place
- To track progress over time and revisit weak areas
- To have a portfolio of DSA work I can point to

---



Each folder contains individual problem files named like:

```
001_two_sum.py
002_reverse_linked_list.py
```

Every file includes:
- The problem statement (as a comment) or a link to it (LeetCode / GFG / etc.)
- My solution
- Time & space complexity notes
- Occasional alternate approaches

Example:

```python
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Given an array of integers, return indices of the two numbers
that add up to a target.
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Time: O(n)  |  Space: O(n)
```

---



---


---

## 🛠️ Tech

- **Language:** Python 3.x
- **Testing:** occasional `if __name__ == "__main__":` blocks with sample inputs, or `pytest` for select problems



## 🤝 Contributing

This is primarily a personal learning log, but if you spot a bug, a better approach, or want to suggest a cleaner solution, feel free to open an issue or PR!

---

## 📬 Connect

If this repo helped you or you just want to talk DSA, feel free to reach out or star ⭐ the repo!

---

*"The only way to get better at DSA is to keep solving." — Consistency > Intensity*
