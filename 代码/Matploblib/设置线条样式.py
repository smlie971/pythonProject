from matplotlib import pyplot as plt
import numpy as np
y=[np.random.randint(0,10) for x in range(10)]
plt.plot(y,lw=2,c='r',ls='--',aa=False)  #lw：直线宽度；c：颜色；linestyle：线条样式
plt.show()
