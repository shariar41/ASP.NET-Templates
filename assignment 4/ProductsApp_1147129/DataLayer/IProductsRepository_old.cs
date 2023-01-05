using ProductsApp_1147129.Models;

namespace ProductsApp_1147129.DataLayer
{
    public interface IProductsRepository_old
    {
        bool AddProduct(Product_old prod);
        bool ApplyDiscount(int prodid, double percentDiscount);
        bool DeleteProduct(int prodid);
        List<Category_old> GetCategories();
        Product_old GetProductById(int prodid);
        List<Product_old> GetProductsByCatId(int catid);
        bool UpdateProduct(Product_old prod);
    }
}
