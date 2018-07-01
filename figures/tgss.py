import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

LOF_int=[146.12,64.3,90,37.36,50.34,49,]
TGSS_int=[189.7,91.1,123.2,66,54.7,48]

plt.xlabel('LOFAR integated flux density values in mJy')
plt.ylabel("TGSS integrated flux density values in mJy")
plt.scatter(LOF_int,TGSS_int)

slope, intercept = np.polyfit(LOF_int, TGSS_int, 1)
abline_values = [slope * l + intercept for l in LOF_int]
plt.plot(LOF_int, abline_values, 'b', label='fit')
plt.savefig("Integrated_tgss.png")
plt.show()
