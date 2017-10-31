# MatPlotLib

---

### Learning Objectives
***Students will be able to...***

* Import the `matplotlib` library
* Import a text file
* Make a DataFrame
* Filter through a DataFrame

---
### Context 

* The missing limb of pandas

---
### Lessons

##### Part 1 - What is MatPlotLib

* Before we do anything lets install the library

```
pip3 install matplotlib
```
* This is a python 2D plotting library
* It will take your data and create images with that information
* You can start looking at the docs here
	* [MatPlotLib Documentation](http://matplotlib.org/)
	* [Pandas Visualization](http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html)

##### Examples

* import pandas and matplotlib

```
import pandas as pd
import matplotlib.pyplot as plt
```
* `pd.DataFrame` has a [`.plot()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html) method to generate a graph from its data.
* A Plot object has the method `get_figure`, which returns a Figure. 
* A Figure can be saved to a file with the method [`.savefig()`](http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.savefig)
* (`.savefig()` takes the arguments `*args` and `**kwargs`. You don't have to understand them yet, but be sure to notice them because you'll see them again very soon.

##### Introduction

Data Visualization is an important and exciting aspect of data science. It reveals information we otherwise wouldn't have noticed. It allows us to showcase the work we've done through visualizations, which can be stagnant or interactive. 

Unique data visualizations are more memorable. You're very quickly going to lose the attention of your audience with basic plots, which is why utilizing modules like seaborn, bokeh, and ggplot are recommended.

It's important to note that while these approaches definitely have applications, they're not as commonly used as bar graphs, line graphs, scatter plots, or even histograms. These basic visualization types can still be the best choice for certain, straightforward data stories. However, communicating complex topics — hierarchies, longitudinal data, and multi-variable comparisons, and so on — often involves more advanced visualizations. That's our focus for this tutorial. 

But before we go into code, let's overview some strategies for effective data visualization.

##### Less is More

Very often, when it comes to plotting, less is more. Data usually looks better "naked". What does this mean?

- Remove backgrounds

- Remove redundant labels

- Lighten your lines, or remove them!

- Reduce unnecessary colors

- Remove special effects

##### Colors Matter

The default library, matplotlib, is fairly ugly, as we've reviewed before. This is why using modules like seaborn, bokeh, etc, are so popular - their default color schemes are much more appealing. 

Also, keep in mind that many people are color blind, so choosing your color schemes is incredibly important so that your work is accessible to everyone. 

##### Python Modules

[matplotlib](http://matplotlib.org/) is a 2D python plotting library which allows you to generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc, with just a few lines of code.

[bokeh](http://bokeh.pydata.org/en/latest/) is an interactive visualization library for modern web browsers presentation. 

[seaborn](http://seaborn.pydata.org/introduction.html#introduction) is a library for making statistical graphics in Python. It's built on top of matplotlib and is tightly integrated with the PyData stack, including support for numpy and pandas data structures and statistical routines from scipy and statsmodels. 

[ggplot](http://ggplot.yhathq.com/) is a plotting system built for making profressional-looking plots quickly with minimal code.


##### Basic Plots with matplotlib.pyplot

`matplotlib.pyplot` is a collection of functions that make matplotlib work similar to matlab. Each pyplot function makes some change to a figure. In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes. In this section, we'll overview the basic plot types: line plots, scatter plots, and histograms.

##### Line Plots 

Line graphs are plots where a line is drawn to indicate a relationship between a particular set of x and y values.

``` python
import matplotlib.pyplot as plt
```

To be able to plot anything, we need to provide the data points, so we declare those as follows:

``` python
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
```

Using matplotlib, we can plot a line between plot x and y.
```
plt.plot(x, y)
```

And as always, we use the `show()` method to have the visualizations pop up.
``` python
plt.show()
```

##### Scatter Plots

Alternatively, you might want to plot quantities with 2 positions as data points. To do this, you first have to import the needed libraries, as always. We'll be using the same data from before:

```  python
import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
```

Next, we plot it with the `plt.plot()` method. Note that the `o` denotes the type of graph we're plotting. 

``` python
plt.plot(x, y, 'o')
```

As always, let's look at what we made:

``` python
plt.show()
```

##### Histograms

Histograms are very often used in science applications and it's highly likely that you will need to plot them at some point. They are very useful to plot distributions. As before, we'll use numpy and matplotlib.

``` python
import numpy as np
import matplotlib.pyplot as plt
```

First, we'll make the data to plot. We're going to make a normal distribution with 1000 points. 

``` python
data = np.random.normal(5.0, 3.0, 1000)
```

Now, we actually make that histogram of the data array and attach a label:

``` python
plt.hist(data)
plt.xlabel("data")
```

Lastly, let's look at what we've made: 

``` python
plt.show()
```

##### Customization

The default customization for matplotlib isn't very appealing or even helpful in data visualization tasks. 


##### Colors

When there are multiple data points or objects, they have to be able to be differentiated between one another. An easy way to do that is by using different marker styles and colors. You can do this by editing the third parameter to include a letter that indicates the color, such as: 

``` python
plt.plot(x, y, "r")
```
This will give you the same line as before, but now it'll be red. 

##### Styles

You can also customize the style of the your lines and markers. With line graphs, you can change the line to be dotted, dashed, etc, for example the following should give you a dashed line now:

``` python
plt.plot(x,y, "--")
```

You can find other linestyles you can use can be found on the [Matplotlib webpage](http://
matplotlib.sourceforge.net/api/pyplot)

``` python
plt.plot(x,y, "b*")
```

With Scatter Plots, you can customize the dots to be squares, pentagons, etc. This will get you the a scatter plot with star markers:

``` python
plt.plot(x,y, "*")
```

##### Labels

We want to always label the axes of plots to tell users what they're looking at. You can do this in matplotlib, very easily:

If we want to attach a label on the x-axis, we can do that with the `xlabel()` function: 
``` python
plt.xlabel("X Axis")
```

With a quick modification, we can also do that for the y-axis:
``` python
plt.ylabel("Y Axis")
```

What good is a visualization without a title to let us know what the visualization is showing? Luckily, matplotlib has a built in function for that:
``` python
plt.title("Title Here")
```

Lastly, we can even customize the range for the x and y axes: 
``` python
plt.xlim(0, 10)
plt.ylim(0, 10)
```
