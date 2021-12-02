(def n (Integer/parseInt (first *command-line-args*)))
(def List (range 1 (+ n 1)))
(defn Map [x] (* x x))
(def List2 (map Map List))
(run! println List2)

(def sum (reduce + List2))
(println "Sum =" sum)

