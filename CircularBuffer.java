/**
* Ring or circular buffer. This Circular buffer 
* is thread safe.
* 
* @author devansh.mht@gmail.com
*/
public class CircularBuffer {
    
    public CircularBuffer(int size) {
        this.size = size;
    }
    
    private int size;
}
