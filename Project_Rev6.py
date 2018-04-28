# André Roche 15-Apr-18 - testing on numpy from course notes. 
# Scripting using ipython in terminal for real time response and pasting workking code in program.
# This program does not check if the data is imported correctly. It is testing the functions in numpy.

import numpy

data = numpy.genfromtxt('data/iris_Dataset.csv', delimiter =',')
from scipy import stats
from scipy.stats import skew, kurtosis, normaltest

# Define each column. Assign data to these.
firstcol = data[:,0]
secondcol = data[:,1] 
thirdcol = data[:,2]
fourthcol = data[:,3]

# define the mean of each column of data
meanfirstcol = numpy.mean(data[:,0])
meansecondcol = numpy.mean(data[:,1])
meanthirdcol = numpy.mean(data[:,2])
meanfourthcol = numpy.mean(data[:,3])

# define the minimum of each column of data
minfirstcol = numpy.min(data[:,0])
minsecondcol = numpy.min(data[:,1])
minthirdcol = numpy.min(data[:,2])
minfourthcol = numpy.min(data[:,3])

# define the maximum of each column of data 
maxfirstcol = numpy.max(data[:,0])
maxsecondcol = numpy.max(data[:,1])
maxthirdcol = numpy.max(data[:,2])
maxfourthcol = numpy.max(data[:,3])

# define the standard deviation of each column of data
stdfirstcol = numpy.std(data[:,0])
stdsecondcol = numpy.std(data[:,1])
stdthirdcol = numpy.std(data[:,2])
stdfourthcol = numpy.std(data[:,3])

# define the median of each column of data
medianfirstcol = numpy.median(data[:,0])
mediansecondcol = numpy.median(data[:,1])
medianthirdcol = numpy.median(data[:,2])
medianfourthcol = numpy.median(data[:,3])

# define the skew of each column of data
skewfirstcol = skew(data[:,0])
skewsecondcol = skew(data[:,1])
skewthirdcol = skew(data[:,2])
skewfourthcol = skew(data[:,3])

# define the kurtosis of each column of data
kurtfirstcol = kurtosis(data[:,0])
kurtsecondcol = kurtosis(data[:,1])
kurtthirdcol = kurtosis(data[:,2])
kurtfourthcol = kurtosis(data[:,3])

normfirstcol = normaltest(data[:,0])
normsecondcol = normaltest(data[:,1])
normthirdcol = normaltest(data[:,2])
normfourthcol = normaltest(data[:,3])



print ('The Summary for the First Column is as follows:')
print ('Max =', maxfirstcol)
print ('Min =', minfirstcol)
print ('Mean =', meanfirstcol)
print ('Standard Deviation =', stdfirstcol)
print ('Median =', medianfirstcol)
print ('Skew =', skewfirstcol)
print ('Kurtosis = ', kurtfirstcol)
print ('Normality = ', normfirstcol)

print('')  # just print a line space on screen

print ('The Summary for the Second Column is as follows:')
print ('Max =', maxsecondcol)
print ('Min =', minsecondcol)
print ('Mean =', meansecondcol)
print ('Standard Deviation =', stdsecondcol)
print ('Median =', mediansecondcol)
print ('Skew =', skewsecondcol)
print ('Kurtosis = ', kurtsecondcol)
print ('Normality = ', normsecondcol)

print('')  # just print a line space on screen

print ('The Summary for the Third Column is as follows:')
print ('Max =', maxthirdcol)
print ('Min =', minthirdcol)
print ('Mean =', meanthirdcol)
print ('Standard Deviation =', stdthirdcol)
print ('Median =', medianthirdcol)
print ('Skew =', skewthirdcol)
print ('Kurtosis = ', kurtthirdcol)
print ('Normality = ', normthirdcol)

print('')  # just print a line space on screen

print ('The Summary for the Fourth Column is as follows:')
print ('Max =', maxfourthcol)
print ('Min =', minfourthcol)
print ('Mean =', meanfourthcol)
print ('Standard Deviation =', stdfourthcol)
print ('Median =', medianfourthcol)
print ('Skew =', skewfourthcol)
print ('Kurtosis = ', kurtfourthcol)
print ('Normality = ', normfourthcol)

print('')

stats.f_oneway(data[:,0],data[:,1], data[:,2],data[:,3]) # Anova test for more than two samples i.e. all features.
print( 'Anova Results Are As Follows:') 
print(stats.f_oneway(data[:,0],data[:,1], data[:,2],data[:,3]))


import matplotlib.pyplot as pl

pl.hist(firstcol)
pl.show()

pl.hist(secondcol)
pl.show()

pl.hist(thirdcol)
pl.show()

pl.hist(fourthcol)
pl.show()


