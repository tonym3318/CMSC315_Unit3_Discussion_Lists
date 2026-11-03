"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

Name: Anthony Marquez
Course: CMSC 315
Assignment: Unit 3 Discussion - Lists
Date: November 2, 2026

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the specified index.
    # Existing elements at or after this index shift one position right.
    lst.insert(index, value)

    # Inserting at the beginning or middle requires shifting elements.
    # Inserting at the end generally requires less work.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate the index before attempting to remove an element.
    # This prevents an IndexError when the index is outside the list.
    if 0 <= index < len(lst):
        # Remove and return the element at the specified index.
        return lst.pop(index)

    # Return None if the index is invalid to avoid a program error.
    return None

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear search checks each element in the list sequentially
    # Start at index 0 and continue until the value is found.
    for index in range(len(lst)):
        if lst[index] == value:
            # Return the index where the matching value was found.
            return index

    # Return -1 if the entire list was searched without a match.
    return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create a list of MPEG video channels carried on VLAN 200.
    channels = ["ESPN", "Fox Sports 1", "Altitude Sports"]

    # Display the original channel list before making changes.
    print("Original VLAN 200 channel list:", channels)

    # Insert a channel at the beginning (index 0).
    insert_at(channels, 0, "CNN")
    print ("After inserting CNN at the beginning:", channels)

    # Insert a channel in the middle of the list (index 2).
    insert_at(channels, 2, "NFL Network")
    print("After inserting NFL Network in the middle:", channels)

    # Insert a channel at the end using the current list length.
    insert_at(channels, len(channels), "Discovery Channel")
    print("After inserting Discovery Channel at the end:", channels)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Delete the first channel from the list (index 0).
    removed = delete_at(channels, 0)
    print("Removed from beginning:", removed)
    print("Updated channel list:", channels)

    # Delete a channel from the middle of the list (index 2).
    removed = delete_at(channels, 1)
    print("Removed from middle:", removed)
    print("Updated channel list:", channels)

    # Delete the last channel using its current index.
    removed = delete_at(channels, len(channels) -1)
    print("Removed from end:", removed)
    print("Updated channel list:", channels)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Search for a MPEG channel that exists in the VLAN 200 list.
    # The linear search returns the index where the channel is found.
    found_index = search_value(channels, "Fox Sports 1")
    print("Searching for Fox Sports 1:")
    print("Channel found at index:", found_index)

    # Search for a channel that does not exist in the list.
    # The search returns -1 when no matching channel is found.
    missing_index = search_value(channels, "HBO")
    print("Searching for HBO:")
    print("Search result:", missing_index)
    print("-1 indicates the channel was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge Case 1: Attempt to delete a channel using an invalid index.
    # The function should return None without causing an IndexError.
    removed = delete_at(channels, 100)
    print("Attempting to delete at invalid index 100:", removed)
    print("Channel list after invalid deletion:", channels)

    # Edge Case 2: Insert a channel into an empty list.
    # An empty list can accept a new element at index 0.
    empty_channels = []
    print("Original empty channel list:", empty_channels)

    insert_at(empty_channels, 0, "NFL Network")
    print("After inserting into empty list:", empty_channels)

if __name__ == "__main__":
    main()