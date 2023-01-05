using Microsoft.EntityFrameworkCore;
using ProductsApp_1147129.Models;

namespace ProductsApp_1147129.DataLayer
{
    public class ProductRepositoryEF : IProductsRepository
    {
        ProductsBcbs1147129Context _context;
        public ProductRepositoryEF(ProductsBcbs1147129Context context)
        {
            _context = context;
        }
        public bool AddProduct(Product prod)
        {
            Product pr = _context.Products.FirstOrDefault(p => p.ProductId == prod.ProductId);
            if (pr == null)
            {
                _context.Products.Add(prod);
                _context.SaveChanges();
                return true;
            }
            else
                return false;
        }
        public bool ApplyDiscount(int prodid, double percentDiscount)
        {
            Product pr = _context.Products.FirstOrDefault(p => p.ProductId == prodid);
            if (pr != null)
            {
                pr.Price = pr.Price - pr.Price * (decimal)percentDiscount / 100.0m;
                _context.Entry(pr).State = Microsoft.EntityFrameworkCore.EntityState.Modified;
                _context.SaveChanges();
                return true;
            }
            else
                return false;
        }
        public bool DeleteProduct(int prodid)
        {
            Product pr = _context.Products.FirstOrDefault(p => p.ProductId == prodid);
            if (pr != null)
            {
                _context.Products.Remove(pr);
                _context.SaveChanges();
                return true;
            }
            else
                return false;
        }
        public List<Category> GetCategories()
        {
            return _context.Categories.ToList<Category>();
        }
        public Product GetProductById(int prodid)
        {
            return _context.Products.Include(p => p.PcolorNavigation).Where(p => p.ProductId == prodid).FirstOrDefault<Product>();
        }
        public List<Product> GetProductsByCatId(int catid)
        {
            return _context.Products.Include(p => p.PcolorNavigation).Where(p => p.CategoryId == catid).ToList<Product>();
        }
        public bool UpdateProduct(Product prod)
        {
            Product pr = _context.Products.FirstOrDefault(p => p.ProductId == prod.ProductId);
            if (pr != null)
            {
                _context.Entry(pr).State = EntityState.Detached;
                _context.Products.Update(prod);
                _context.SaveChanges();
                return true;
            }
            else
                return false;
        }
    }
}