using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using prac01_core_web_app.Models;

namespace prac01_core_web_app
{
    public class TvShowsContext : DbContext
    {
        public TvShowsContext (DbContextOptions<TvShowsContext> options)
            : base(options)
        {
        }

        public DbSet<prac01_core_web_app.Models.TvShows> TvShows { get; set; } = default!;
    }
}
