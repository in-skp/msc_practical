using System.ComponentModel.DataAnnotations;

namespace prac01_core_web_app.Models
{
    public enum Genre
    {
        Drama,
        Comedy,
        Romance,
        [Display(Name = "Romantic Comedy")]
        RomCom,
        Crime,
        Mystery
    }
}
