using ProductsApp_1147129.ModelsVM;

namespace ProductsApp_1147129.DataLayer
{
    public interface ICartRepository
    {
        void AddItemToCart(CartItem item);
        Task<List<CartItem>> GetCart();
        void StoreCart(List<CartItem> CList);
        Task<int> ExistInCart(CartItem item);
    }
}