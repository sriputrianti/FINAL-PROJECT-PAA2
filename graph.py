import networkx as nx
import time

def tsp(graph):
    start_time = time.time()

    # Menghitung jarak terpendek antara setiap pasangan node
    shortest_path = nx.approximation.traveling_salesman_problem(graph)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return shortest_path, elapsed_time

def dijkstra(graph, start_node):
    start_time = time.time()

    # Menghitung jarak terpendek menggunakan algoritma Dijkstra
    shortest_path = nx.single_source_dijkstra_path(graph, start_node)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return shortest_path, elapsed_time

def main():
    graph = nx.Graph()
    graph.add_edges_from([('a', 'b', {'weight': 12}),
                          ('a', 'c', {'weight': 10}),
                          ('a', 'g', {'weight': 12}),
                          ('b', 'd', {'weight': 12}),
                          ('b', 'c', {'weight': 8}),
                          ('c', 'd', {'weight': 11}),
                          ('c', 'e', {'weight': 3}),
                          ('c', 'g', {'weight': 9}),
                          ('d', 'e', {'weight': 11}),
                          ('d', 'f', {'weight': 10}),
                          ('e', 'f', {'weight': 6}),
                          ('e', 'g', {'weight': 7}),
                          ('f', 'g', {'weight': 9})])

    print("=== Program Pencarian Jalur Terpendek ===")
    while True:
        print("1. Traveling Salesman Problem (TSP)")
        print("2. Dijkstra")
        print("3. Keluar")
        choice = int(input("Masukkan pilihan Anda: "))

        if choice == 1:
            shortest_path, elapsed_time = tsp(graph)
        elif choice == 2:
            start_node = input("Masukkan node awal: ")
            shortest_path, elapsed_time = dijkstra(graph, start_node)
        elif choice == 3:
            print("Program selesai. Sampai jumpa kembali.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            continue

        print("Hasil setiap iterasi:")
        for i, node in enumerate(shortest_path):
            print(f"Iterasi {i+1}: {node}")

        print(f"Waktu komputasi perhitungan path: {elapsed_time} detik")
        print("Hasil akhir (shortest path):")
        print(shortest_path)

if __name__ == "__main__":
    main()
