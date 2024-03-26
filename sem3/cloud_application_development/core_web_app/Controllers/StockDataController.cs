using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using core_web_app.Data;
using core_web_app.Models;

namespace core_web_app.Controllers
{
    public class StockDataController : Controller
    {
        private readonly StockDataContext _context;

        public StockDataController(StockDataContext context)
        {
            _context = context;
        }

        // GET: StockData
        public async Task<IActionResult> Index()
        {
              return _context.StockData != null ? 
                          View(await _context.StockData.ToListAsync()) :
                          Problem("Entity set 'StockDataContext.StockData'  is null.");
        }

        // GET: StockData/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.StockData == null)
            {
                return NotFound();
            }

            var stockData = await _context.StockData
                .FirstOrDefaultAsync(m => m.Id == id);
            if (stockData == null)
            {
                return NotFound();
            }

            return View(stockData);
        }

        // GET: StockData/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: StockData/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,StockName,PClose,LTP,Group,ChartUrl")] StockData stockData)
        {
            if (ModelState.IsValid)
            {
                _context.Add(stockData);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(stockData);
        }

        // GET: StockData/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.StockData == null)
            {
                return NotFound();
            }

            var stockData = await _context.StockData.FindAsync(id);
            if (stockData == null)
            {
                return NotFound();
            }
            return View(stockData);
        }

        // POST: StockData/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,StockName,PClose,LTP,Group,ChartUrl")] StockData stockData)
        {
            if (id != stockData.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(stockData);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!StockDataExists(stockData.Id))
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
            return View(stockData);
        }

        // GET: StockData/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.StockData == null)
            {
                return NotFound();
            }

            var stockData = await _context.StockData
                .FirstOrDefaultAsync(m => m.Id == id);
            if (stockData == null)
            {
                return NotFound();
            }

            return View(stockData);
        }

        // POST: StockData/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.StockData == null)
            {
                return Problem("Entity set 'StockDataContext.StockData'  is null.");
            }
            var stockData = await _context.StockData.FindAsync(id);
            if (stockData != null)
            {
                _context.StockData.Remove(stockData);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool StockDataExists(int id)
        {
          return (_context.StockData?.Any(e => e.Id == id)).GetValueOrDefault();
        }
    }
}
