import matplotlib.pyplot as plt
import numpy as np

def f(a,x):
    return a*x*(1-x)

class SpiderwebDiagram():
    def __init__(self,func_para, initial_value) -> None:
        self.func_para = func_para
        self.initial_value = initial_value
        self.x_n = []
        self.x_n1 = []

    def solve_xn(self):
        self.x_n=np.array([self.initial_value])
        for i in range(26):
            self.x_n = np.append(self.x_n,[f(self.func_para, self.x_n[i])])
        self.x_n = np.delete(self.x_n, -1)    
        
    def solve_xn1(self):
        for i in range(26):
            self.x_n1 = np.append(self.x_n1, [f(self.func_para, self.x_n[i])])
            
    def show_spiderweb(self):
        n=np.linspace(0,25,26)
        x=np.linspace(0,1,1000)
        y=f(self.func_para,x)
        self.solve_xn()
        self.solve_xn1()
        fig=plt.figure(figsize = (30,10))
        fig1= fig.add_subplot(1,2,1)
        fig1.plot(x,y,'-', color="blue")
        fig1.plot([0,1],[0,1], color="green")
        fig1.plot([self.x_n[0],self.x_n[0]],[self.x_n[0],0],linestyle="dashed",color="red")
        for j in range(25):
            fig1.plot([self.x_n[j],self.x_n1[j]],[self.x_n1[j],self.x_n1[j]],linestyle="dashed",color="red")
            fig1.plot([self.x_n[j],self.x_n[j]],[self.x_n1[j],self.x_n[j]],linestyle="dashed",color="red")

        fig1.set_xlim([0,1])
        fig1.set_ylim([0,1])
        fig1.set_ylabel(r"$x_{n+1}$")
        fig1.set_xlabel(r"$x_n$")
        
        fig2=fig.add_subplot(1,2,2)
        fig2.plot(n,self.x_n)
        fig2.set_ylim([0,1])
        
        plt.show()
            
if __name__ == '__main__':
    spider = SpiderwebDiagram(3.5, 0.1)
    spider.show_spiderweb()



        