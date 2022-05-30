import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def crossing():
    """This function allows the user to see where two functions intersect"""
    f = lambda x: x**5 - x**4 - 2*x**2 +1
    g = lambda x: x**2 + 2
    
    while True:
        try:
            N = eval(input("Enter the number of x values youd like for your domain: "))
        except NameError:
            print("That is not a number. Try again")
            continue
        except SyntaxError:
            print("Hmm. It seems something went wrong there. Try again.")
        else:
            if type(N) != int:
                print("That is not a whole number. Please try again!")
                continue
            else:
                if N<400:
                    print("Choose a bigger number to work with. Try a number equal to or greater than 400")
                    continue
                elif N>6000:
                    print("That will work but that is overkill, dont ya think?")
                    break
                else:
                    break
            
    while True:
        try:
            E = eval(input("Enter your epsion number: "))
        except NameError:
            print("That is not a number. Try again")
            continue
        except SyntaxError:
            print("Hmm. It seems something went wrong there. Try again.")
        else:
            if E>1:
                print("Choose a number smaller than one. Remember that this is your epsilon value! ")
                continue
            else:
                break
    
    x_values = np.linspace(-1,2,N+1)
    f_values = f(x_values)
    g_values = g(x_values)
    
    difference_values = abs(f_values-g_values)
    
    for number in x_values:
        if np.round((f(number) - g(number)),1) == 0:
            plt.vlines(x = number, ymin = 0, ymax = 10, linestyle= 'dashed', color = 'green')
    
    plt.plot(x_values, difference_values)
    plt.plot(x_values, f_values, color = "purple")
    plt.plot(x_values, g_values, color = 'red')
    plt.legend(["intersection line","|f(x)-g(x)|","f(x)","g(x)"])
    plt.title("A plot showing where the two graphs f(x) and g(x0 intersect")
    plt.show()
    
    
    return f"The diagram below shows f and g in purple and red respectively. The blue function shows the absolute value of the difference between them and the green line shows where f and g intersect. "
    
    
crossing()
