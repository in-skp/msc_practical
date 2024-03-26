using System.Text.RegularExpressions;
using System.ComponentModel.DataAnnotations;

namespace core_web_app.Models
{
    public class StockData
    {
        public int Id { get; set; }

        [Required]
        [StringLength(maximumLength: 50, MinimumLength = 3)]
        public string StockName { get; set; }

        [Required]
        public double PClose { get; set; }

        [Required]
        public double LTP { get; set; }

        [Required]
        public Group Group { get; set; }

        [Required]
        [DataType(DataType.Url)]
        [Display(Name = "Live Data")]
        public string ChartUrl { get; set; }

    }
}
