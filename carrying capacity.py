"""
written for python 3.5
By: Robert Nunn
(C) 2017
Creates an interactive chart showing how growth rate, initial population and carrying capacity
affect how a population grows over time.
"""

from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.lines as lin
import numpy as np
import math
from matplotlib.widgets import Slider, Button
from pprint import pprint as pp


def make_generations(rate, pop, K, gens, gen_rate, limit=True):
    """
    Generates the population history given the following parameters
    :param rate: the growth rate of the population (1.0 = doubling pop every generation)
    :param pop: the initial population count
    :param K: carrying capacity
    :param gens: number of generations to generate
    :param gen_rate: how many data points to generate per generation (1 = 1 point per gen, 0.1 = 10 points per gen)
    :param limit: is this population growth limited by space and food?
    :return: a list containing the population count through time
    """
    generations = []
    for i in gens:
        dN = rate*gen_rate * pop
        if limit:
            dN *= ((K-pop)/K)
        pop += dN
        generations.append(pop)
    return generations


# attempt to make the population history in a different way; didn't work
def make_gen2(rate, pop0, K, gens):
    expo = (-rate * gens)
    # print(expo)
    pop_size = [K/(1+((K/pop0)-1)*math.exp(i)) for i in expo]
    return pop_size


def update(val):
    """
    Updates the graph when one of the sliders changes
    :param val: not currently used
    :return: nothing, directly updates the graph
    """
    # round values from sliders to an appropriate number of decimal places
    K = round(sK.val,0)
    rate = round(srate.val, 2)
    pop0 = round(spop0.val, 0)

    # set the new location for the carrying capacity marker
    dotted.set_ydata([K])
    ann.set_x(1)
    ann.set_y(K+200)

    # generate and set the new population history for the limited and unlimited growth curves
    l_limit.set_ydata(make_generations(rate, pop0, K, t, gen_rate))
    l_nolimit.set_ydata(make_generations(rate, pop0, K, t, gen_rate, False))

    # draw the new graph
    fig.canvas.draw_idle()


# reset the sliders when called
def reset(event):
    sK.reset()
    srate.reset()
    spop0.reset()


K = 5000  # carrying capacity
rate = .5  # growth rate
end_point = 40  # max number of generations to simulate
gen_rate = .1  # how frequently calculation are made, smaller values == more frequently
pop0 = 1  # initial population (ignores the fact that 1 individual can't reproduce sexually unless they are hermaphroditic)
t = np.arange(1, end_point, gen_rate)  # generates a list containing the timepoints to generate population counts for
pop = make_generations(rate, pop0, K, t, gen_rate)  # population history with carrying capacity limit
pop_nl = make_generations(rate, pop0, K, t, gen_rate, False)  # population history without limit
# pp(pop)
axcolor = 'lightgoldenrodyellow'  # sets background color for sliders

fig, ax = plt.subplots()  # generate the base figure

l_limit, = plt.plot(t, pop, color='red')  # create the normal population history
l_nolimit, = plt.plot(t, pop_nl, color='blue')  # create the unlimited population history
# set axis labels
plt.xlabel('Generations (t)')
plt.ylabel('Population Size (N)')

plt.axis([0, end_point, 0, 10000])  # define range of x-axis (elem 0 and 1) and y-axis (elem 2 and 3)

# create the dotted line and annotation indicating the carrying capacity on the graph
dotted = plt.axhline([K], 0, end_point, linestyle='dashed')
ann = plt.annotate('Carrying Capacity', xy=(1, K*1.02))

plt.grid(True)  # turn on the gridlines for the chart area

plt.subplots_adjust(bottom=0.4)  # positioning the sliders correctly

# add the sliders to the plot
axK = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axrate = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axpop0 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)

# add reset button
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
button.on_clicked(reset)

#  set initial values of the three sliders controlling the graph
sK = Slider(axK, 'Carrying capacity (K)', 500, 10000, K)
srate = Slider(axrate, 'Growth rate (r)', 0, 5.0, rate)
spop0 = Slider(axpop0, 'Initial population', 1, 100, pop0)

#  set what function to call when one of the sliders changes
sK.on_changed(update)
srate.on_changed(update)
spop0.on_changed(update)

# print(t)
# print(make_gen2(rate, pop0, K, t))
plt.show()  # display the chart
