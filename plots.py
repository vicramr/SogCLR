import numpy as np
from matplotlib import pyplot as plt

# top1 accuracies. [clean, robust]
run5 = [55.8, 14.89]
run2 = [53.04, 19.15]
run4 = [13.16, 9.75]
run3 = [52.12, 17.86]
run11 = [47.48, 20.49]

# image blending: buffer size 128, blend factor 0.9
plt.title('Image Blending Probability vs Accuracy')
# 5, 2, 4
blend_prob = [0.0, 0.1, 0.9]
clean_acc = [run5[0], run2[0], run4[0]]
rob_acc = [run5[1], run2[1], run4[1]]
plt.plot(blend_prob, clean_acc, label='Clean Acc')
plt.plot(blend_prob, rob_acc, label='Robust Acc')
plt.ylabel('Accuracy')
plt.xlabel('Blending Probability')
plt.legend()
plt.savefig('furthest.png')

# same but use_closest:
plt.cla()
plt.clf()

plt.title('Image Blending Probability vs Accuracy (Closest Image)')
# 5, 3, 11
blend_prob = [0.0, 0.1, 0.5]
clean_acc = [run5[0], run3[0], run11[0]]
rob_acc = [run5[1], run3[1], run11[1]]

plt.plot(blend_prob, clean_acc, label='Clean Acc')
plt.plot(blend_prob, rob_acc, label='Robust Acc')
plt.ylabel('Accuracy')
plt.xlabel('Blending Probability')
plt.legend()
plt.savefig('closest.png')



plt.cla()
plt.clf()

# clae
# top1 accuracies. [clean, robust]
plt.title('Regularization Strength vs Accuracy')
run16 = [60.7, 17.74]
run15 = [65.57, 6.94]
run14 = [63.94, 23.37]
# 5, 16, 15, 14

reg = [0.0, 0.1, 0.3, 1.0]
clean_acc = [run5[0], run16[0], run15[0], run14[0]]
rob_acc = [run5[1], run16[1], run15[1], run14[1]]

plt.plot(reg, clean_acc, label='Clean Acc')
plt.plot(reg, rob_acc, label='Robust Acc')
plt.ylabel('Accuracy')
plt.xlabel('Regularization Coefficient')
plt.legend()
plt.savefig('clae.png')
