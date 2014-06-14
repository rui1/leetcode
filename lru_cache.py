class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.keys = {}
        self.MRU=None
        self.LRU = None
        self.cap = capacity

    # @return an integer
    def get(self, key):
        t=self.cache.get(key)
        if t is None:
            return -1
        else:
            pre, post = self.keys[key]
            if pre is not None:
                if post is None:
                    self.keys[pre][1]=None
                    self.LRU = pre
                else:
                    self.keys[pre][1]=post
                    self.keys[post][0]=pre
                self.keys[self.MRU][0]=key
                self.keys[key]=[None,self.MRU]
                self.MRU= key
            return t
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if len(self.cache)==0:
            self.keys[key]=[None, None]
            self.MRU = self.LRU = key
        else:
            t = self.cache.get(key)
            if t is None:
                if len(self.cache)>=self.cap:
                    tmp =self.LRU
                    #print 'tmp',tmp
                    if self.cap ==1:
                        self.keys[key]=[None, None]
                        MRU = LRU= key
                    else:
                        preLRU = self.keys[tmp][0]
                        self.LRU = preLRU
                        self.keys[self.LRU][1]=None
                        self.keys[key]=[None, self.MRU]
                        self.keys[self.MRU][0]=key
                        self.MRU = key
                    del self.keys[tmp]
                    del self.cache[tmp]
                else:
                    self.keys[key]=[None, self.MRU]
                    self.keys[self.MRU][0]=key
                    self.MRU = key
                    
            else:
                pre, post = self.keys[key]
                if pre is not None:
                    if post is None:
                        self.keys[pre][1]=None
                        self.LRU = pre
                    else:
                        self.keys[pre][1]=post
                        self.keys[post][0]=pre
                    self.keys[self.MRU][0]=key
                    self.keys[key]=[None,self.MRU]
                    self.MRU= key
        self.cache[key]=value

test = LRUCache(2)
test.set(2,1)
print "set 2,1"
print test.cache
print test.keys
print test.MRU, test.LRU


test.set(1,1)
print "set 1,1"
print test.cache
print test.keys
print test.MRU, test.LRU
#print test.get(2)

test.set(2,3)
print "set 1,1"
print test.cache
print test.keys
print test.MRU, test.LRU

test.set(4,1)
print "set 1,1"
print test.cache
print test.keys
print test.MRU, test.LRU

print test.get(1)
print"get 2"
print test.cache
print test.keys
print test.MRU, test.LRU

'''test.set(4,1)
print "set 4,1"
print test.cache
print test.keys
print test.MRU, test.LRU

print test.get(1)
print "get 1"
print test.cache
print test.keys
print test.MRU, test.LRU'''

print test.get(2)
print "get2"
print test.cache
print test.keys
print test.MRU, test.LRU
