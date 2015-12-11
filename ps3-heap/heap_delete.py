#Matt Layman - CS213 - heap_delete.py

import heap

class heap_delete(heap.heap):
	"""Adds delete method to heap, starting with code from heap"""
	def delete(self, i):
		"""deletes an element at index i from heap"""
		self._swap(i, -1)                       #replace ith element with last element
		self.A.pop()                            #pop ith element off heap
		self.heapsize -= 1                      #decrement heap size
		self.min_heapify(1)                     #reheapify heap
