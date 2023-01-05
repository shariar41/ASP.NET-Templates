namespace ProductsApp_1147129.Models
{
    public enum ProductColor_old
    {
        RED,
        GREEN,
        PURPLE
    }
    public class Product_old
    {
        public int ProductId { get; set; }
        public string ProductName { get; set; }
        public string Description { get; set; }
        public decimal Price { get; set; }
        public int StockLevel { get; set; }
        public bool OnSale { get; set; }
        public bool Discontinued { get; set; }
        public int CategoryId { get; set; }
        public int? PColor { get; set; }
}
}