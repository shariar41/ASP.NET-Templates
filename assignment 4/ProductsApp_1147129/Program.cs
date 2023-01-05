using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using Microsoft.EntityFrameworkCore;
using ProductsApp_1147129.Data;
using ProductsApp_1147129.DataLayer;
using ProductsApp_1147129.Models;
using ProductsApp_1147129.Utils;

var builder = WebApplication.CreateBuilder(args);

var connstr = builder.Configuration.GetConnectionString("ProductsDBConn");
ConnectionStringHelper.CONNSTR = connstr;
builder.Services.AddDbContext<ProductsBcbs1147129Context>(options =>
options.UseSqlServer(builder.Configuration["ConnectionStrings:ProductsDBConn"]));
builder.Services.AddScoped<IProductsRepository, ProductRepositoryEF>();
builder.Services.AddScoped<IProductsRepository_old, ProductRepositorySQL>();
builder.Services.AddScoped<ICartRepository, CartRepository>();

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddSingleton<WeatherForecastService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();

app.UseRouting();

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
