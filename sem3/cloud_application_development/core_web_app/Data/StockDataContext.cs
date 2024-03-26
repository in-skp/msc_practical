using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using core_web_app.Models;

namespace core_web_app.Data
{
    public class StockDataContext : DbContext
    {
        public StockDataContext (DbContextOptions<StockDataContext> options)
            : base(options)
        {
        }

        public DbSet<core_web_app.Models.StockData> StockData { get; set; } = default!;
    }
}
