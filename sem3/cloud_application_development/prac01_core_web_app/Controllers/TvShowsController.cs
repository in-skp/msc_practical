using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using prac01_core_web_app;
using prac01_core_web_app.Models;

namespace prac01_core_web_app.Controllers
{
    public class TvShowsController : Controller
    {
        private readonly TvShowsContext _context;

        public TvShowsController(TvShowsContext context)
        {
            _context = context;
        }

        // GET: TvShows
        public async Task<IActionResult> Index()
        {
              return _context.TvShows != null ? 
                          View(await _context.TvShows.ToListAsync()) :
                          Problem("Entity set 'TvShowsContext.TvShows'  is null.");
        }

        // GET: TvShows/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.TvShows == null)
            {
                return NotFound();
            }

            var tvShows = await _context.TvShows
                .FirstOrDefaultAsync(m => m.Id == id);
            if (tvShows == null)
            {
                return NotFound();
            }

            return View(tvShows);
        }

        // GET: TvShows/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: TvShows/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Title,Genre,Rating,ImdbUrl,ImageUrl")] TvShows tvShows)
        {
            if (ModelState.IsValid)
            {
                _context.Add(tvShows);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(tvShows);
        }

        // GET: TvShows/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.TvShows == null)
            {
                return NotFound();
            }

            var tvShows = await _context.TvShows.FindAsync(id);
            if (tvShows == null)
            {
                return NotFound();
            }
            return View(tvShows);
        }

        // POST: TvShows/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Title,Genre,Rating,ImdbUrl,ImageUrl")] TvShows tvShows)
        {
            if (id != tvShows.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(tvShows);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!TvShowsExists(tvShows.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(tvShows);
        }

        // GET: TvShows/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.TvShows == null)
            {
                return NotFound();
            }

            var tvShows = await _context.TvShows
                .FirstOrDefaultAsync(m => m.Id == id);
            if (tvShows == null)
            {
                return NotFound();
            }

            return View(tvShows);
        }

        // POST: TvShows/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.TvShows == null)
            {
                return Problem("Entity set 'TvShowsContext.TvShows'  is null.");
            }
            var tvShows = await _context.TvShows.FindAsync(id);
            if (tvShows != null)
            {
                _context.TvShows.Remove(tvShows);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool TvShowsExists(int id)
        {
          return (_context.TvShows?.Any(e => e.Id == id)).GetValueOrDefault();
        }
    }
}
