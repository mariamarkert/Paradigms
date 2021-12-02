(def fp (slurp "temperatures.txt"))
(def temperatures (clojure.string/split fp #"\n"))
(def newtemperatures (map read-string temperatures))

(defn FtoC [t] (/ (* (- t 32) 5) 9))
(def celcius (map FtoC newtemperatures))

(defn avg [x] (double (/ (reduce + x) (count x))))

(println "min = " (apply min celcius))
(println "max = " (apply max celcius))
(println "average = " (avg celcius))
