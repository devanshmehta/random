
__author__ = 'devansh.mht@gmail.com'

class RateLimiter:
    '''Uses an approach similar to bucket tocken 
       model to calculate the rate. This approach 
       uses constant memory and constant time to 
       limit the rate.
    '''

    def __init__(self, rate, interval):        
        self.score = 0
        #assumes the rate is always > 0
        self.rate = rate
        #assumes the interval is always > 0
        #and it is in seconds
        self.interval = interval

    def allow(self, now):
        tmp_score = self.score
        #calculates the tmp score
        increment = self.interval / self.rate
        if self.score == 0:
            tmp_score = now + increment
        else:
            tmp_score += increment
        #checks if the tmp_score is conformant
        if tmp_score < now:
            self.score = now + increment
            return True
        elif tmp_score < now + self.interval:
            self.score = tmp_score
            return True
        else:
            return False

def main():
    #4 accesses in 10 seconds or 1 in 2.5 seconds.
    #1 token in the bucket every 2.5 seconds.
    rate_limiter = RateLimiter(4.0, 10.0)
    print rate_limiter.allow(0) #True
    print rate_limiter.allow(11) #True
    print rate_limiter.allow(12) #True
    print rate_limiter.allow(12) #True
    print rate_limiter.allow(12) #True
    print rate_limiter.allow(13) #False
    print rate_limiter.allow(15) #True we can add one more token between 11 and 15
    print rate_limiter.allow(17) #True we can add two more tokens between 11 and 17
    print rate_limiter.allow(18) #False
    print rate_limiter.allow(19) #True we can add three more tokens between 11 and 19
    print rate_limiter.allow(20) #False

    #number of True / number of seconds elapsed
    #number of True = 8
    #number of seconds elapsed = 20
    #overall rate = 20 / 8 which is what we want

if __name__ == '__main__':
    main()
