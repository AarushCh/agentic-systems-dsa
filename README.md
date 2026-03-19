# SE Intern Assessment - Data Structures & Systems Design

[cite_start]This repository contains the solutions for the SE Intern Data Structures & Systems Design assessment[cite: 1, 2]. It is structured to reflect production-ready standards, including source code separation, unit testing, and technical documentation.

## Problem Logic Overview

### [cite_start]Problem 1: LRU Cache Implementation [cite: 5]
[cite_start]**Logic and Approach:** To achieve the required O(1) time complexity[cite: 11, 13], I utilized a Hash Map (dictionary) combined with a Doubly Linked List. The Hash Map provides instant O(1) lookups for any key. However, Hash Maps do not maintain temporal order efficiently. To solve this, the dictionary values point directly to nodes in a Doubly Linked List. When an item is accessed or added, manipulating a few pointers allows us to move it to the "head" (most recently used) in O(1) time. [cite_start]The item at the "tail" is always the least recently used, allowing for O(1) eviction when capacity is reached[cite: 9, 12].

### [cite_start]Problem 2: Event Scheduler [cite: 14]
**Logic and Approach:** * **`can_attend_all`:** I sort the events chronologically by start time. [cite_start]A person can attend all events if no single event starts strictly before the previous one has ended[cite: 17]. 
* [cite_start]**`min_rooms_required`:** I track room availability dynamically[cite: 22]. After sorting events by start time, I use a Min-Heap (priority queue) to store the *end times* of ongoing meetings. For each new event, I check the top of the heap (the earliest finishing meeting). [cite_start]If it finishes before or when the new event starts[cite: 21], I pop it (room freed) and push the new end time. Otherwise, I just push the new end time (allocating an additional room). [cite_start]The maximum size of the heap represents the minimum rooms required[cite: 18].

## Project Structure
* `src/`: Contains the core implementation (`lru_cache.py`, `event_scheduler.py`).
* `tests/`: Contains `unittest` files to verify constraints and edge cases.
* `docs/`: Contains the Final Discussion & Analysis.

## How to Run Tests
Navigate to the root directory of the project and execute the built-in unittest module:

```bash
python -m unittest discover tests