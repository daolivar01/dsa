class DynamicArray:
    """
    A dynamic array implementation that automatically resizes when capacity is exceeded.
    
    This class simulates the behavior of dynamic arrays (like Python lists) by managing
    capacity separately from size and doubling capacity when needed.
    
    Attributes:
        capacity (int): Maximum number of elements the array can hold without resizing
        size (int): Current number of elements in the array
        data (list): Internal storage for array elements
    """
    
    def __init__(self):
        """
        Initialize an empty dynamic array with initial capacity of 2.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.capacity = 2
        self.size = 0
        self.data = [None] * self.capacity
    
    def _resize(self):
        """
        Double the capacity of the array and copy all existing elements to new storage.
        
        This is a private method called automatically when the array reaches capacity.
        Doubling strategy ensures amortized O(1) append operations.
        
        Time Complexity: O(n) where n is the current size
        Space Complexity: O(n) for the new array
        """
        self.capacity = self.capacity * 2
        new_data = [None] * self.capacity

        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data = new_data
    
    def append(self, element):
        """
        Add an element to the end of the array.
        
        Args:
            element: The element to add to the array
            
        Time Complexity: O(1) amortized (O(n) worst case when resizing)
        Space Complexity: O(1) amortized
        """
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = element
        self.size += 1
    
    def insert(self, index, element):
        """
        Insert an element at the specified index, shifting existing elements to the right.
        
        Args:
            index (int): The index at which to insert the element (0 <= index <= size)
            element: The element to insert
            
        Raises:
            IndexError: If index is out of valid range [0, size]
            
        Time Complexity: O(n) due to element shifting
        Space Complexity: O(1) or O(n) if resizing is needed
        """
        if index < 0 or index > self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size}]")
        if self.size == self.capacity:
            self._resize()

        i = self.size-1
        while i >= index:
            self.data[i + 1] = self.data[i]
            i -= 1

        self.data[index] = element
        self.size += 1
    
    def delete(self, index):
        """
        Remove and return the element at the specified index.
        
        Elements after the deleted index are shifted left to fill the gap.
        
        Args:
            index (int): The index of the element to delete (0 <= index < size)
            
        Returns:
            The element that was removed
            
        Raises:
            IndexError: If index is out of valid range [0, size)
            
        Time Complexity: O(n) due to element shifting
        Space Complexity: O(1)
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size})")
        deleted_element = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1
        self.data[self.size] = None  # Clear the now-unused slot
        return deleted_element
    
    def get(self, index):
        """
        Return the element at the specified index.
        
        Args:
            index (int): The index of the element to retrieve (0 <= index < size)
            
        Returns:
            The element at the specified index
            
        Raises:
            IndexError: If index is out of valid range [0, size)
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size})")
        return self.data[index]
    
    def __str__(self):
        """
        Return a string representation of the array showing used and unused slots.
        
        Returns:
            str: Visual representation with size and capacity information
        """
        elements = [str(self.data[i]) for i in range(self.size)]
        empty_slots = ['_'] * (self.capacity - self.size)
        return f"[{', '.join(elements + empty_slots)}] (size: {self.size}, capacity: {self.capacity})"


def test_dynamic_array():
    """
    Comprehensive test suite for the DynamicArray class.
    Tests all methods including edge cases and error conditions.
    """
    print("🧪 Running Dynamic Array Tests...")
    
    # Test 1: Initialization
    print("\n1. Testing initialization...")
    arr = DynamicArray()
    assert arr.size == 0, "Initial size should be 0"
    assert arr.capacity == 2, "Initial capacity should be 2"
    print("   ✅ Initialization passed")
    
    # Test 2: Append operations
    print("\n2. Testing append operations...")
    arr.append(10)
    assert arr.size == 1, "Size should be 1 after first append"
    assert arr.get(0) == 10, "First element should be 10"
    
    arr.append(20)
    assert arr.size == 2, "Size should be 2 after second append"
    assert arr.capacity == 2, "Capacity should still be 2"
    
    # This should trigger resize
    arr.append(30)
    assert arr.size == 3, "Size should be 3 after third append"
    assert arr.capacity == 4, "Capacity should be 4 after resize"
    assert arr.get(2) == 30, "Third element should be 30"
    print("   ✅ Append operations passed (including resize)")
    
    # Test 3: Insert operations
    print("\n3. Testing insert operations...")
    arr.insert(1, 15)  # Insert at middle
    assert arr.size == 4, "Size should be 4 after insert"
    assert arr.get(1) == 15, "Element at index 1 should be 15"
    assert arr.get(2) == 20, "Element at index 2 should be 20 (shifted)"
    
    arr.insert(0, 5)   # Insert at beginning
    assert arr.get(0) == 5, "Element at index 0 should be 5"
    assert arr.get(1) == 10, "Element at index 1 should be 10 (shifted)"
    
    arr.insert(arr.size, 50)  # Insert at end
    assert arr.get(arr.size - 1) == 50, "Last element should be 50"
    print("   ✅ Insert operations passed")
    
    # Test 4: Delete operations
    print("\n4. Testing delete operations...")
    original_size = arr.size
    deleted = arr.delete(0)  # Delete first element
    assert deleted == 5, "Deleted element should be 5"
    assert arr.size == original_size - 1, "Size should decrease by 1"
    assert arr.get(0) == 10, "New first element should be 10"
    
    deleted = arr.delete(2)  # Delete middle element
    assert deleted == 20, "Deleted element should be 20"
    
    deleted = arr.delete(arr.size - 1)  # Delete last element
    assert deleted == 50, "Deleted element should be 50"
    print("   ✅ Delete operations passed")
    
    # Test 5: Get operations
    print("\n5. Testing get operations...")
    for i in range(arr.size):
        element = arr.get(i)
        assert element is not None, f"Element at index {i} should not be None"
    print("   ✅ Get operations passed")
    
    # Test 6: Error handling
    print("\n6. Testing error handling...")
    
    # Test invalid get indices
    try:
        arr.get(-1)
        assert False, "Should raise IndexError for negative index"
    except IndexError:
        pass
    
    try:
        arr.get(arr.size)
        assert False, "Should raise IndexError for index >= size"
    except IndexError:
        pass
    
    # Test invalid delete indices
    try:
        arr.delete(-1)
        assert False, "Should raise IndexError for negative index"
    except IndexError:
        pass
    
    try:
        arr.delete(arr.size)
        assert False, "Should raise IndexError for index >= size"
    except IndexError:
        pass
    
    # Test invalid insert indices
    try:
        arr.insert(-1, 100)
        assert False, "Should raise IndexError for negative index"
    except IndexError:
        pass
    
    try:
        arr.insert(arr.size + 2, 100)
        assert False, "Should raise IndexError for index > size"
    except IndexError:
        pass
    
    print("   ✅ Error handling passed")
    
    # Test 7: Stress test - multiple resizes
    print("\n7. Testing multiple resizes...")
    stress_arr = DynamicArray()
    initial_capacity = stress_arr.capacity
    
    # Add enough elements to trigger multiple resizes
    num_elements = 10
    for i in range(num_elements):
        stress_arr.append(i * 10)
    
    assert stress_arr.size == num_elements, f"Size should be {num_elements}"
    assert stress_arr.capacity >= num_elements, "Capacity should accommodate all elements"
    assert stress_arr.capacity > initial_capacity, "Capacity should have increased"
    
    # Verify all elements are correct
    for i in range(num_elements):
        assert stress_arr.get(i) == i * 10, f"Element at index {i} should be {i * 10}"
    
    print(f"   ✅ Stress test passed (capacity grew from {initial_capacity} to {stress_arr.capacity})")
    
    # Test 8: Empty array operations
    print("\n8. Testing empty array edge cases...")
    empty_arr = DynamicArray()
    
    try:
        empty_arr.get(0)
        assert False, "Should raise IndexError for empty array"
    except IndexError:
        pass
    
    try:
        empty_arr.delete(0)
        assert False, "Should raise IndexError for empty array"
    except IndexError:
        pass
    
    # Insert at index 0 should work for empty array
    empty_arr.insert(0, 42)
    assert empty_arr.size == 1, "Size should be 1 after insert in empty array"
    assert empty_arr.get(0) == 42, "Element should be 42"
    
    print("   ✅ Empty array edge cases passed")
    
    print("\n🎉 All tests passed! Dynamic Array implementation is correct.")
    
    # Display final state of test array
    print(f"\nFinal test array state: {arr}")


if __name__ == "__main__":
    test_dynamic_array()
