#Matt Layman - CS213 - bstselect.py
import bstsize

class BST(bstsize.BST):
    """
    Adds select method to BST, starting with code from bstsize.   
    """
    
    def select(self, index):
        """
        Takes a 1-based index, and returns the element at that index,
        or None if the index is out-of-bounds.
        """
        node = self.root
        def maketreelist(node):         #make unsorted list of tree elements
            if node is None: return []  #base case
            return maketreelist(node.left) + [node] + maketreelist(node.right)  #go down tree recursively returning each node in a list&concatenating them at the root

        def Sort(treelist):             #sort unsorted list of tree elements
            sorted = False

            while not sorted:           #while sorted is false
                sorted = True           #exit loop condition
                for i in range(len(treelist)-1):      #scale range to length of tree list
                    if treelist[i].key > treelist[i+1].key:    #compare element.key
                        sorted = False
                        treelist[i], treelist[i+1] = treelist[i+1], treelist[i]    #switch element indices
            return treelist             #return sorted list

        treelist = maketreelist(node)   #call recursive treelist function, returns unsorted list of tree elments
        sortedtreelist = Sort(treelist) #sort tree elements based on their key sizes

        if index in range(1, len(sortedtreelist)+1):
            return sortedtreelist[index-1]  #scale BST index to python list index to return correct tree element

        else:
        	return None                 #return None if index is out of range
