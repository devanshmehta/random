import java.util.concurrent.AtomicInteger;
import java.util.concurrent.AtomicBoolean;

/**
* Ring or circular buffer. This Circular buffer 
* is thread safe. Please make sure that this Buffer
* is used by only two threads a) Consumer b) Producer
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
        if (isFull() && !inPoll) {
            getPointer++;
        }
        int add = addPointer % size;
        arr[add] = e
        ++addPointer;
    }
    
    public E poll() {
        inPoll = true;
        if (isEmpty()) {
            return null;
        }
        int get = getPointer % size;
        E e = arr[get];
        ++getPointer;
        inPoll = false;
        return e;
    }
    
    private int size;
    private int getPointer;
    private int addPointer;
    private int count;
    private boolean inPool;
    private E[] arr;
}
