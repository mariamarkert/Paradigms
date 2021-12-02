(ns taxation)

(defn tax [cost taxRate]
	(float (/ (* cost taxRate) 100)))

(ns application)

(println "the tax on this item is $"(taxation/tax 117 7))
