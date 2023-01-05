using Microsoft.AspNetCore.Components.Server.ProtectedBrowserStorage;
using Newtonsoft.Json;
using ProductsApp_1147129.ModelsVM;

namespace ProductsApp_1147129.DataLayer
{
    public class CartRepository : ICartRepository
    {
        ProtectedLocalStorage _LocalStore; // storage, retrieval is key, value based
        public CartRepository(ProtectedLocalStorage ps)
        {
            _LocalStore = ps;
        }
        string CartKey = "CartKey1";
        public async Task<List<CartItem>> GetCart()
        {
            List<CartItem> CList = new List<CartItem>();
            var json = await _LocalStore.GetAsync<string>(CartKey);
            string jsonstr = json.Value;
            if (jsonstr != null)
                CList = JsonConvert.DeserializeObject<List<CartItem>>(jsonstr);
            return CList;
        }
        public void StoreCart(List<CartItem> CList)
        {
            string json = JsonConvert.SerializeObject(CList);
            _LocalStore.SetAsync(CartKey, json);
        }
        public async void AddItemToCart(CartItem item)
        {
            List<CartItem> CList = await GetCart();
            // if item exists, then increment its quantity, else add it to cart
            bool found = false;
            foreach (var row in CList)
            {
                if (row.ProductId == item.ProductId)
                {
                    row.Quantity = row.Quantity + 1;
                    found = true;
                    break;
                }
            }
            if (found == false)
                CList.Add(item);
            StoreCart(CList);
        }

        public async Task<int> ExistInCart(CartItem item)
        {
            List<CartItem> CList = await GetCart();
            // if item exists, then increment its quantity, else add it to cart
            int found = 0;
            foreach (var row in CList)
            {
                if (row.ProductId == item.ProductId)
                {
                    found = row.Quantity;
                    break;
                }
            }
            return found;
        }
    }

}