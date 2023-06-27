# FINAL-PROJECT-PAA2

# Analysis algorithm bubble sort
1. Worst case
   Worst case terjadi ketika elemen-elemen dalam array terurut secara terbalik. Dalam hal ini, setiap elemen harus melalui seluruh iterasi penukaran sehingga array benar-benar terurut. Jumlah iterasi yang dilakukan adalah n - 1, di mana n adalah jumlah elemen dalam array. Terdapat 75 iterasi yang dilakukan untuk mengurutkan array dengan 75 elemen. Kompleksitas waktu dalam worst case adalah O(n^2), di mana n adalah jumlah elemen dalam array.
2. Best case
   Best case terjadi ketika array sudah terurut secara ascending. Dalam hal ini, Bubble Sort akan memeriksa setiap pasangan elemen dan tidak melakukan pertukaran karena array sudah terurut dengan benar. Jumlah iterasi yang dilakukan adalah 1, karena hanya perlu memeriksa elemen-elemen sekali. Kompleksitas waktu dalam best case adalah O(n), di mana n adalah jumlah elemen dalam array.
4. Average case
   Rata-rata kasus terjadi ketika elemen-elemen dalam array tidak terurut secara khusus dan memiliki urutan acak. Rata-rata jumlah iterasi yang dilakukan adalah sekitar n/2, di mana n adalah jumlah elemen dalam array. Hal ini disebabkan oleh rata-rata jumlah pertukaran yang harus dilakukan dalam setiap iterasi. Kompleksitas waktu dalam average case adalah O(n^2), di mana n adalah jumlah elemen dalam array.

# Analysis algorithm insertion sort
1. Worst case
   Worst case terjadi ketika elemen-elemen dalam array terurut secara terbalik. Dalam hal ini, setiap elemen harus dimasukkan ke dalam posisi yang benar dengan membandingkannya dengan elemen-elemen sebelumnya. Pada setiap iterasi, elemen akan dibandingkan dengan seluruh elemen sebelumnya dan akan menggeser elemen-elemen yang lebih besar ke posisi yang benar. Pada kasus ini, jumlah iterasi yang dilakukan adalah n - 1, di mana n adalah jumlah elemen dalam array. Terdapat 75 iterasi yang dilakukan untuk mengurutkan array dengan 75 elemen. Kompleksitas waktu dalam worst case adalah O(n^2), di mana n adalah jumlah elemen dalam array.
2. Best case
   Best case terjadi ketika array sudah terurut secara ascending. Dalam hal ini, Insertion Sort akan memeriksa setiap elemen dan membandingkannya dengan elemen-elemen sebelumnya, tetapi tidak ada pergeseran yang diperlukan karena array sudah terurut dengan benar. Jumlah iterasi yang dilakukan adalah 1, karena hanya perlu memeriksa elemen-elemen sekali. Kompleksitas waktu dalam best case adalah O(n), di mana n adalah jumlah elemen dalam array.
4. Average case
   Rata-rata kasus terjadi ketika elemen-elemen dalam array tidak terurut secara khusus dan memiliki urutan acak. Rata-rata jumlah iterasi yang dilakukan adalah sekitar n^2/4, di mana n adalah jumlah elemen dalam array. Hal ini disebabkan oleh rata-rata jumlah pergeseran yang harus dilakukan dalam setiap iterasi. Kompleksitas waktu dalam average case adalah O(n^2), di mana n adalah jumlah elemen dalam array.
   
# Analysis algorithm TSP
1. Worst case
   Pada TSP, worst case terjadi ketika semua kemungkinan rute perlu dijelajahi untuk mencari rute terpendek. Pada grafik yang diberikan, terdapat 7 node (a, b, c, d, e, f, g) dan 13 edge yang menghubungkan node-node tersebut. Dalam hal ini, jumlah kemungkinan rute yang harus dieksplorasi adalah (n-1)!, di mana n adalah jumlah node. Terdapat 6 node (n-1) sehingga terdapat 5! = 120 kemungkinan rute yang harus dieksplorasi. Oleh karena itu, kompleksitas waktu dalam worst case adalah O((n-1)!), yang dapat menjadi sangat besar seiring dengan peningkatan jumlah node.
2. Best case
   Pada TSP, best case terjadi ketika rute terpendek dapat ditemukan dengan cepat tanpa perlu mencari semua kemungkinan rute. Namun, karena TSP adalah permasalahan NP-hard, tidak ada algoritma yang dapat menyelesaikan TSP dalam waktu polinomial untuk semua kasus. Oleh karena itu, tidak ada best case yang signifikan dalam hal waktu eksekusi.
4. Average case
   Analisis average case pada TSP lebih kompleks dan tergantung pada variasi algoritma yang digunakan. Terdapat beberapa pendekatan untuk menyelesaikan TSP, seperti algoritma brute force, algoritma heuristik (seperti Nearest Neighbor atau 2-Opt), dan algoritma optimasi (seperti Simulated Annealing atau Genetic Algorithm). Setiap pendekatan memiliki kompleksitas waktu dan performa yang berbeda dalam kasus-kasus rata-rata. Namun, secara umum, kompleksitas waktu untuk mencari solusi optimal dalam average case pada TSP adalah eksponensial terhadap jumlah node.
   
# Analysis algorithm Djikstra 
Dengan node awal yaitu b
1. Worst case
   Worst case pada algoritma Dijkstra terjadi ketika graf memiliki banyak node dan edge yang saling terhubung, sehingga terdapat banyak kemungkinan jalur yang harus diperiksa. Kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah node (vertices) dan E adalah jumlah edge. Terdapat 7 node dan 13 edge dalam graf, sehingga kompleksitas waktu dapat dianggap sebagai O((7 + 13) log 7), yang dapat disederhanakan menjadi O(20 log 7).
2. Best case
   Pada algoritma Dijkstra, skenario best case terjadi ketika node tujuan dapat langsung dicapai dari node awal tanpa perlu memeriksa node lainnya. Kompleksitas waktu Dijkstra dalam kasus ini adalah O(V), di mana V adalah jumlah node (kota).
4. Average case
    Kompleksitas waktu rata-rata Dijkstra tergantung pada struktur graf dan jarak antara node-node yang terlibat. Dalam kasus terbaik, kompleksitas waktu dapat mendekati O(V), sedangkan dalam kasus terburuk, kompleksitas waktu dapat mendekati O((V + E) log V).
