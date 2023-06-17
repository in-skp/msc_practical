#6A : Perform testing of hypothesis using one way ANOVA

from scipy.stats import f_oneway

performance1 = [89, 89, 88, 78, 79]
performance2 = [93, 92, 94, 89, 88]
performance3 = [89, 88, 89, 93, 90]
performance4 = [81, 78, 81, 92, 82]

stat,pval = f_oneway(performance1, performance2, performance3, performance4)

if pval < 0.05:
  print("we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")
