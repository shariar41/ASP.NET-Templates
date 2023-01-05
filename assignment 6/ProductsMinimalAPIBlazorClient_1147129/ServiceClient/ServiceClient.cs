using ProductsMinimalAPI_1147129.Models;
using ProductsMinimalAPIBlazorClient_1147129.ModelsDTO;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Formatting;
using System.Text;
using System.Threading.Tasks;

namespace ProductsMinimalAPIBlazorClient_1147129.ServiceClient
{
	public class ServiceClient
	{
		// this class communicates with the API 
		HttpClient client = new HttpClient();
		bool init = false;
		string baseurl = "https://localhost:7053/";

		public ServiceClient() // ignore SSL errors under .Net core 
		{
			var httpClientHandler = new HttpClientHandler();
			httpClientHandler.ServerCertificateCustomValidationCallback =
				(message, cert, chain, sslPolicyErrors) => { return true; };
			client = new HttpClient(httpClientHandler) { };
			init = true;
		}
		public async Task<List<Product>> GetAllProductsAsync()
		{
			string url = "myapi/allproducts";
			string path = baseurl + "myapi/allproducts";
			List<Product> products = null;
			HttpResponseMessage response = await client.GetAsync(path);
			if (response.IsSuccessStatusCode)
			{
				products = await response.Content.ReadAsAsync<List<Product>>();
			}
			return products;
		}

		public async Task<List<Category>> GetCategoriesAsync()
		{
			string path = baseurl + "myapi/categories";
			List<Category> cats = null;
			HttpResponseMessage response = await client.GetAsync(path);
			if (response.IsSuccessStatusCode)
			{
				cats = await response.Content.ReadAsAsync<List<Category>>();
			}
			return cats;
		}

		public async Task<List<Product>> GetProductsByCategoryAsync(int catid)
		{
			string path = baseurl + "myapi/productsbycatid?id=" + $"{catid}";
			List<Product> products = null;
			HttpResponseMessage response = await client.GetAsync(path);
			if (response.IsSuccessStatusCode)
			{
				products = await response.Content.ReadAsAsync<List<Product>>();
			}
			return products;
		}

		public async Task<List<ProductDTO>> GetProductsByCategoryDTOAsync(int
catid)
		{
			string path = baseurl + "myapi/productsbycatid?id=" + $"{catid}";
			List<Product> products = null;
			HttpResponseMessage response = await client.GetAsync(path);
			if (response.IsSuccessStatusCode)
			{
				products = await response.Content.ReadAsAsync<List<Product>>();
			}
			List<ProductDTO> PList = new List<ProductDTO>();
			foreach (var p in products)
			{
				ProductDTO productDTO = new ProductDTO();
				productDTO.ProductId = p.ProductId;
				productDTO.ProductName = p.ProductName;
				productDTO.Description = p.Description;
				productDTO.Price = p.Price;
				productDTO.StockLevel = p.StockLevel;
				PList.Add(productDTO);
			}
			return PList;
		}

		public async Task<Product> GetProductByIdAsync(int pid)
		{
			string path = baseurl + "myapi/productbyid?id=" + $"{pid}";
			Product prod = null;
			HttpResponseMessage response = await client.GetAsync(path);
			if (response.IsSuccessStatusCode)
			{
				prod = await response.Content.ReadAsAsync<Product>();
			}
			return prod;
		}

		public async Task<ProductDTO> GetProductByProductIdDTOAsync(int pid)
		{
			string path = baseurl + "myapi/productbyid?id=" + $"{pid}";
			Product prod = null;
			HttpResponseMessage response = await client.GetAsync(path);
			if (response.IsSuccessStatusCode)
			{
				prod = await response.Content.ReadAsAsync<Product>();
			}
			ProductDTO productDTO = null;
			if (prod != null)
			{
				productDTO = new ProductDTO();
				productDTO.ProductId = prod.ProductId;
				productDTO.ProductName = prod.ProductName;
				productDTO.Description = prod.Description;
				productDTO.Price = prod.Price;
				productDTO.StockLevel = prod.StockLevel;
			}
			return productDTO;
		}

		public async Task<bool> UpdateProductAsync(Product prod)
		{
			string url = baseurl + "myapi/updateproduct";
			HttpResponseMessage response = await client.PutAsync<Product>(url,
prod,
				new JsonMediaTypeFormatter());
			if (response.IsSuccessStatusCode)
				return true;
			else
				return false;
		}

		public async Task<bool> AddNewProductAsync(Product prod)
		{
			string url = baseurl + "myapi/addproduct";
			HttpResponseMessage response = await client.PostAsync<Product>(url,
prod,
				new JsonMediaTypeFormatter());
			if (response.IsSuccessStatusCode)
				return true;
			else
				return false;
		}

		public async Task<bool> DeleteProductAsync(int pid)
		{
			string url = baseurl + "myapi/deleteproduct?id=" + $"{pid}";
			HttpResponseMessage response = await client.DeleteAsync(url);
			if (response.IsSuccessStatusCode)
				return true;
			else
				return false;
		}
	}
}