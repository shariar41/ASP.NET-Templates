using ProductsApp_1147129.Models;

namespace ProductsApp_1147129.DataLayer
{
    public interface IProductsRepository
    {
        bool AddProduct(Product prod);
        bool ApplyDiscount(int prodid, double percentDiscount);
        bool DeleteProduct(int prodid);
        List<Category> GetCategories();
        Product GetProductById(int prodid);
        List<Product> GetProductsByCatId(int catid);
        bool UpdateProduct(Product prod);
    }
}
