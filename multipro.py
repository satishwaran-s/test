import time
import multiprocessing

def basic_func(x):
	if x == 0:
		return 'zero'
	elif x%2 == 0:
		return 'even'
	else:
		return 'odd'

def multiprocessing_fun(x):
	y = x*x
	time.sleep(2)
	print('{} squared results is a/an {} number'.format(x, basic_func(y)))

if __name__== '__main__':
	starttime = time.time()
	processes = []
	for i in range (0,10):
		p = multiprocessing.Process(target=multiprocessing_fun, args=(i,))
		processes.append(p)
		p.start()

	for process in processes:
		process.join()

	print('that took {} seconds'.format(time.time() - starttime))


