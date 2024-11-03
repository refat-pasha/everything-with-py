class ProductSearch:

    def search(self,*a):
        print(f"{a}")

product_search = ProductSearch()
product_search.search("Smartphone")
product_search.search("Smartphone", "300-600")
product_search.search("samsung", "300-600", 4.0)
