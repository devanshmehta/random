import math

class SegmentTree(object):

    """Segment to update and query in log(n) time"""
    
    #the structure of the segment is similar to heap 
    #x -> index of the node, 2*x -> left son 2*x + 1 -> right son
    #Each node interval stores count for that interval

    def __init__(self, size):
        """Size is the max element which will be stored in this data 
           structure"""
        self.size = size
        self.num_nodes = int(math.pow(2, int(math.log(size + 1)) + 1))
        self.segment_tree = [0] * self.num_nodes

    def increment_count(self, num, low, high, subtree = 0, increment = 1):
        """Increments the count for the given value"""
        mid = int((low + high)) / 2
        if num == high:
            self.segment_tree[subtree] += 1
        elif num <= mid:
            self.increment_count(num, low, mid, 2 * subtree)
        else:
            self.increment_count(num, mid + 1, high, 2 * subtree + 1)
        
    def query(self, num, low, high, subtree = 0):
        """Finds the number of elements <= num"""        
        mid = int((low + high)) / 2
        if num == high:
            return self.segment_tree[subtree]
        elif num <= mid:
            return self.query(num, low, mid, subtree * 2)
        else:
            return (self.segment_tree[subtree] + 
                    self.query(num, mid + 1, high, subtree * 2 + 1))
