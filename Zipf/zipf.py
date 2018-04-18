import numpy as np

parameter = 2
zipf = np.random.zipf(parameter, 500)
zipf_sorted = sorted(zipf, reverse=True)
zipf_sorted_float = [float(i) for i in zipf_sorted]

# for i in range (0,499):
# 	print "%f" % zipf_sorted_float[i]

total = float(sum(zipf))
print "\n%f\n" % total 

zipf_sorted_float_prob = [x/total for x in zipf_sorted_float]

# for i in range (0,499):
# 	print "%f" % zipf_sorted_float_prob[i]

p = zipf_sorted_float_prob

website_file = "Top 500 Pages"

with open(website_file) as f:
    content = f.readlines()

websites = [x.strip() for x in content]

trace = np.random.choice(websites, int(total), zipf_sorted_float_prob)

trace_file = open('trace', 'w')
for item in trace:
  trace_file.write("%s\n" % item)
