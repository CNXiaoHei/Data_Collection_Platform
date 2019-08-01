import numpy as np
import matplotlib.pyplot as plt

class Piont_solution:
    def __init__(self, theta):
        self.x0 = 0
        self.y0 = 0
        self.theta = theta
        self.r = (8+4*self.theta)/self.theta
        self.l = 5

    def solution(self):
        s1_x = self.x0 + self.r*np.sin(self.theta)
        s1_y = self.y0 - self.r + self.r*np.cos(self.theta)
        s2_x = self.x0 + self.r*np.sin(self.theta) + self.l*np.cos(self.theta)
        s2_y = self.y0 - self.r - self.l*np.sin(self.theta) + self.r*np.cos(self.theta)
        s3_x = self.x0 + self.r*np.sin(self.theta*2) + self.l*np.cos(self.theta)
        s3_y = self.y0 - self.r - self.l*np.sin(self.theta) + self.r*np.cos(self.theta*2)
        s4_x = self.x0 + self.r*np.sin(self.theta*2) + self.l*(np.cos(self.theta)+np.cos(self.theta*2))
        s4_y = self.y0 - self.r - self.l*(np.sin(self.theta) + np.sin(self.theta*2)) + self.r*np.cos(self.theta*2)
        s5_x = self.x0 + self.r*np.sin(self.theta*3) + self.l*(np.cos(self.theta)+np.cos(self.theta*2))
        s5_y = self.y0 - self.r - self.l*(np.sin(self.theta) + np.sin(self.theta*2)) + self.r*np.cos(self.theta*3)
        s6_x = self.x0 + self.r*np.sin(self.theta*3) + self.l*(np.cos(self.theta)+np.cos(self.theta*2)+np.cos(self.theta*3))
        s6_y = self.y0 - self.r - self.l*(np.sin(self.theta) + np.sin(self.theta*2)+np.sin(self.theta*3)) + self.r*np.cos(self.theta*3)
        s7_x = self.x0 + self.r*np.sin(self.theta*4) + self.l*(np.cos(self.theta)+np.cos(self.theta*2)+np.cos(self.theta*3))
        s7_y = self.y0 - self.r - self.l*(np.sin(self.theta) + np.sin(self.theta*2)+np.sin(self.theta*3)) + self.r*np.cos(self.theta*4)
        s8_x = self.x0 + self.r*np.sin(self.theta*4) + self.l*(np.cos(self.theta)+np.cos(self.theta*2)+np.cos(self.theta*3)+np.cos(self.theta*4))
        s8_y = self.y0 - self.r - self.l*(np.sin(self.theta) + np.sin(self.theta*2)+np.sin(self.theta*3)+np.sin(self.theta*4)) + self.r*np.cos(self.theta*4)
        s9_x = self.x0 + self.r*np.sin(self.theta*5) + self.l*(np.cos(self.theta)+np.cos(self.theta*2)+np.cos(self.theta*3)+np.cos(self.theta*4))
        s9_y = self.y0 - self.r - self.l*(np.sin(self.theta) + np.sin(self.theta*2)+np.sin(self.theta*3)+np.sin(self.theta*4)) + self.r*np.cos(self.theta*5)
        dicts_x = np.array([0, s1_x, s2_x, s3_x, s4_x, s5_x, s6_x, s7_x, s8_x, s9_x])
        dicts_y = np.array([0, s1_y, s2_y, s3_y, s4_y, s5_y, s6_y, s7_y, s8_y, s9_y])
        return dicts_x, dicts_y

p1 = Piont_solution(np.pi/12/5)
p2 = Piont_solution(np.pi/6/5)
p3 = Piont_solution(np.pi/3/5)
p4 = Piont_solution(np.pi/10)

x1, y1 = p1.solution()
x2, y2 = p2.solution()
x3, y3 = p3.solution()
x4, y4 = p4.solution()
plt.xlim([0, 70])
plt.ylim([-50, 10])
ax = plt.gca()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.plot(x1, y1, linewidth=1, alpha=0.6)
ax.scatter(x1, y1, marker='*', linewidths=1, alpha=0.6)
ax.plot(x2, y2, linewidth=1, alpha=0.6)
ax.scatter(x2, y2, marker='*', linewidths=1, alpha=0.6)
ax.plot(x3, y3, linewidth=1, alpha=0.6)
ax.scatter(x3, y3, marker='*', linewidths=1, alpha=0.6)
ax.plot(x4, y4, linewidth=1, alpha=0.6)
ax.scatter(x4, y4, marker='*', linewidths=1, alpha=0.6)
plt.grid(linestyle=':', color='black')
plt.show()
