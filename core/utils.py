import time


def time_usage(msg):
	def calc_time(func):
	    def wrapper(*args, **kwargs):
	    	print msg
	        beg_ts = time.time()
	        retval = func(*args, **kwargs)
	        end_ts = time.time()
	        print("Tempo impiegato: %f" % (end_ts - beg_ts))
	        return retval
	    return wrapper
	return calc_time



