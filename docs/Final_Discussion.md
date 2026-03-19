# Final Discussion & Analysis

## [cite_start]1. Time & Space Complexity [cite: 25]

**Problem 1: LRU Cache**
* **Time Complexity:** O(1) for both `get` and `put` operations. The Hash Map allows O(1) lookups, and the Doubly Linked List allows O(1) insertions and deletions since we have direct node references.
* **Space Complexity:** O(N), where N is the `capacity` of the cache. The space is utilized by the Hash Map storing N keys and the Doubly Linked List storing N nodes.

**Problem 2: Event Scheduler**
* **`can_attend_all`:** * **Time:** O(N log N) due to sorting the events array. Iterating through the array takes O(N).
    * **Space:** O(1) or O(N) depending on the sorting algorithm implementation (Python's Timsort requires O(N) worst-case auxiliary space).
* **`min_rooms_required`:**
    * **Time:** O(N log N). Sorting takes O(N log N), and we perform heap push/pop operations O(log N) for each of the N elements.
    * **Space:** O(N) in the worst-case scenario where all meetings overlap, requiring all N end times to be stored in the min-heap simultaneously.

## [cite_start]2. Trade-offs: Hash Map + Doubly Linked List [cite: 26]
An array or standard queue requires O(N) time to find elements or shift them to maintain a "recently used" order. By combining a Hash Map and a Doubly Linked List, we trade spatial efficiency for temporal efficiency. 
* **The Hash Map** provides the O(1) speed for lookups. 
* **The Doubly Linked List** provides the O(1) structural manipulation required to reorder items (moving a node to the head or dropping the tail). 
* **The Trade-off:** The cost of this O(1) performance is increased memory usage, as we must store `prev` and `next` pointers for every item, alongside the dictionary keys.

## [cite_start]3. Future Proofing: Assigning Specific Rooms [cite: 27]
To assign specific room names (e.g., "Room A", "Room B"), I would introduce two new data structures:
1.  **An `available_rooms` Pool:** A Min-Heap initialized with available room identifiers (e.g., `["Room A", "Room B"]`).
2.  **Modified Ongoing Meetings Heap:** Instead of just storing `end_time`, the heap would store tuples of `(end_time, room_identifier)`.

**Logic:** When an event starts, we check the ongoing meetings heap to pop any meetings that have ended and push their `room_identifier` back into the `available_rooms` pool. Then, we pop a room from the `available_rooms` pool and assign it to the current event, pushing `(new_end_time, room_identifier)` back onto the ongoing meetings heap.

## [cite_start]4. Concurrency: Making the LRU Cache Thread-Safe [cite: 28]
Standard dictionaries and linked lists in Python are not inherently thread-safe. If multiple threads attempt to `put` or `get` simultaneously, it could result in corrupted linked list pointers or dictionary state (race conditions).
To make it thread-safe, I would introduce a **Reentrant Lock** (`threading.RLock()` in Python). 
The lock must be acquired at the very beginning of the `get` and `put` methods and released immediately before returning. This ensures that only one thread can mutate the Hash Map and the Doubly Linked List pointers at any given time.