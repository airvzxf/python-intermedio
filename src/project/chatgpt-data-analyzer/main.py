import matplotlib.pyplot as plt

from src.data_analyzer import DataAnalyzer
from src.utils import load_data


def main():
    # Cargar los datos
    data = load_data("data/extended_example.csv")
    analyzer = DataAnalyzer(data)

    # Análisis de categorías
    print("Conteo de categorías:")
    category_counts = analyzer.count_categories()
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    # Cálculo de promedios
    print("\nPromedio de precios:")
    average_price = analyzer.calculate_average("price")
    print(f"Promedio: {average_price:.2f}")

    # Filtrado de datos
    print("\nFiltrar datos por categoría 'Tipo A':")
    filtered_data = analyzer.filter_data(category="Tipo A")
    for item in filtered_data:
        print(item)

    plot_category_counts(category_counts)


def plot_category_counts(counts):
    categories = list(counts.keys())
    values = list(counts.values())

    plt.bar(categories, values)
    plt.title("Conteo de Categorías")
    plt.xlabel("Categoría")
    plt.ylabel("Cantidad")
    plt.show()


if __name__ == "__main__":
    main()
