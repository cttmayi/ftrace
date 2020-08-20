import ftrace
from ftrace import Ftrace, Interval

import sys
from logbook import StreamHandler
StreamHandler(sys.stdout).push_application()

trace = Ftrace(r'test_data\\trace_1.html')
print('--------------------')

FILTERS = ['performTraversals', 'Choreographer#doFrame']
TASKS = 'com.android.systemui'
do_frame = (trace.android.event_intervals(name=FILTERS)) # postFramebuffer events only.

print('++++++++++++++++++++')
print(type(do_frame))
print(do_frame)