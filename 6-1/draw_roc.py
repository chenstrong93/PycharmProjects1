from sklearn.metrics import roc_curve

predict_result = net.predict(x_test).reshape(len(x_test))
fpr, tpr, thresholds = roc_curve(y_tesy, predict_result, pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC of LM')
fpr, tpr, thresholds = roc_curve(y_tesy, tree.predict_proba(x_test)[:,1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC of CART')

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.ylim(0, 1.05)
plt.xlim(0, 1.05)
plt.legend(loc=4)
plt.show()