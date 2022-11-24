from sklearn import tree

# database: Gerbang logika AND
# x = Data, y = Target
x = [[0,0], [0,1], [1,0], [1,1], [1,2], [2,1], [1,3], [3,1], [1,4], [4,1], [1,5], [5,1], [1,6], [6,1]]
y = [0,0,0,1,2,2,3,3,4,4,5,5,6,6]

# Training and classify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Desicion Tree ")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("1 2 = ", clf.predict([[1,2]]))
print ("2 1 = ", clf.predict([[2,1]]))
print ("1 3 = ", clf.predict([[1,3]]))
print ("3 1 = ", clf.predict([[3,1]]))
print ("1 4= ", clf.predict([[1,4]]))
print ("4 1= ", clf.predict([[4,1]]))
print ("1 5= ", clf.predict([[1,5]]))
print ("5 1 = ", clf.predict([[5,1]]))
