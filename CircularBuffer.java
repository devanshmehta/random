/**
* Ring or circular buffer. This Circular buffer 
* is thread safe.
* 
* @author devansh.mht@gmail.com
*/
public class CircularBuffer <E>{
    
    public CircularBuffer(int size) {
        this.size = size;
        arr = new E[size];
        count = 0;
        addPointer = 0;
        getPointer = 0;
    }
    
    public boolean isFull() {
        int diff = addPointer - getPointer;
        if (diff < 0) {
            diff *= -1;
        }
        return diff == 1 || diff == size;
    }
    
    public boolean isEmpty() {
        return addPointer == getPointer;
    }
    
    public void add(E e) {
        if (isFull()) {
            getPointer++;
        }
        int add = addPointer % size;
        arr[add] = e
        ++addPointer;
    }
    
    public E poll() {
        if (isEmpty()) {
            return null;
        }
        int get = getPointer % size;
        E e = arr[get];
        ++getPointer;
        return e;
    }
    
    private int size;
    private int getPointer;
    private int addPointer;
    private int count;
    private E[] arr;
}
