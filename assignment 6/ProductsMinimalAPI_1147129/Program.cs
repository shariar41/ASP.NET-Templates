using Microsoft.EntityFrameworkCore;
using ProductsMinimalAPI_1147129.Models;
using ProductsMinimalAPI_1147129.MyModels;
using System.Linq;
using System.Net;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<ProductsBcbs1147129Context>(options =>
options.UseSqlServer(builder.Configuration["ConnectionStrings:ProductsDBConn"])
);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddCors(options =>
{
	options.AddDefaultPolicy(builder =>
	builder.WithOrigins("https://localhost:7259")
	.AllowAnyHeader()
	.AllowAnyMethod());
});

var app = builder.Build();
app.UseCors();  // abovv bold lines added to allow cross-origin requests

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
	app.UseSwagger();
	app.UseSwaggerUI();
}

app.UseHttpsRedirection();

var summaries = new[]
{
	"Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
};

app.MapGet("/weatherforecast", () =>
{
	var forecast = Enumerable.Range(1, 5).Select(index =>
		new WeatherForecast
		(
			DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
			Random.Shared.Next(-20, 55),
			summaries[Random.Shared.Next(summaries.Length)]
		))
		.ToArray();
	return forecast;
})
.WithName("GetWeatherForecast")
.WithOpenApi();

//-------------------------API related functions--------------------------- 

// get all products 
app.MapGet("/myapi/Products", (ProductsBcbs1147129Context db) =>
{
	return db.Products.ToList();
});

// get all categories 
app.MapGet("/myapi/categories", (ProductsBcbs1147129Context db) =>
{
	return db.Categories.ToList();
});

// get products By Categoryid 
app.MapGet("/myapi/productsbycatid", (ProductsBcbs1147129Context db, int id) =>
{
	var prods = db.Products.Where(p => p.CategoryId == id).ToList<Product>();
	return Results.Ok(prods);
});

// product By Id 
app.MapGet("/myapi/productbyid", (ProductsBcbs1147129Context db, int id) =>
{
	var prod = db.Products.Find(id);
	return Results.Ok(prod);
});

// get products with supliers 

/*app.MapGet("/myapi/productsuppliers", (ProductsBcbs1147129Context db) =>
{
	var prodsSups = db.Suppliers.Include(s => s.Products).
	Select(s => new MyProductSupplier()
	{
		ProductId = s.Products.ToList().Count > 0 ? s.Products.ToList()[0].ProductId:0,
		ProductName = s.Products.ToList().Count > 0 ? s.Products.ToList()[0].ProductName: "",
		SupplierAddress = s.Address,
		SupplierName = s.SupplierName,
		Price = s.Products.ToList().Count > 0 ? s.Products.ToList()[0].Price :0
	}).ToList<MyProductSupplier>();
	return Results.Ok(prodsSups);
});*/

// add product 
app.MapPost("/myapi/addproduct", (ProductsBcbs1147129Context db, Product prod) =>
{
	db.Products.Add(prod);
	db.SaveChanges();
	return Results.Created($"/myapi/productsbyid/{prod.ProductId}", prod);
});

// update product 
app.MapPut("/myapi/updateproduct/", (ProductsBcbs1147129Context db, Product prod) =>
{
	var prodindb = db.Products.FirstOrDefault(x => x.ProductId ==
prod.ProductId);
	if (prodindb != null)
	{
		prodindb.ProductName = prod.ProductName;
		prodindb.Price = prod.Price;
		prodindb.Description = prod.Description;
		prodindb.StockLevel = prod.StockLevel;
		prodindb.CategoryId = prod.CategoryId;
		db.Products.Update(prodindb);
		db.SaveChanges();
		return Results.NoContent();
	}
	else return Results.NotFound();

});

// apply discount to a product 
app.MapPut("/myapi/applydiscount/", (ProductsBcbs1147129Context db, Product prod,
double percentDiscount) =>
{
	var prodindb = db.Products.FirstOrDefault(x => x.ProductId ==
prod.ProductId);
	if (prodindb != null)
	{
		prodindb.Price = prodindb.Price - prodindb.Price *
(decimal)(percentDiscount / 100.0);
		db.Products.Update(prodindb);
		db.SaveChanges();
		return Results.NoContent();
	}
	else
		return Results.NotFound();
});


// delete product 
app.MapDelete("/myapi/deleteproduct/", (ProductsBcbs1147129Context db, int id) =>
{
	var prodindb = db.Products.Find(id);
	if (prodindb != null)
	{
		db.Products.Remove(prodindb);
		db.SaveChanges();
		return Results.NoContent();
	}
	else
		return Results.NotFound();
});

//-------------------------------------------------------
app.Run();

internal record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
	public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
