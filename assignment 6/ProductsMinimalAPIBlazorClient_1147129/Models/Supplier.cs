using System;
using System.Collections.Generic;

namespace ProductsMinimalAPI_1147129.Models;

public partial class Supplier
{
    public int SupplierId { get; set; }

    public string? SupplierName { get; set; }

    public string? Address { get; set; }

    public virtual ICollection<Product> Products { get; } = new List<Product>();
}