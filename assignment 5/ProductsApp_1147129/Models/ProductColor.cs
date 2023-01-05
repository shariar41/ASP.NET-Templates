using System;
using System.Collections.Generic;

namespace ProductsApp_1147129.Models;

public partial class ProductColor
{
    public int ColorId { get; set; }

    public string ColorName { get; set; } = null!;

    public virtual ICollection<Product> Products { get; } = new List<Product>();
}
